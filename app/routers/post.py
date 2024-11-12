
from sqlalchemy import func
from .. import models,schemas,oauth2
from ..database import get_db 
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional

router = APIRouter(
    prefix= '/posts',
    tags = ['Posts']
)

@router.get("/",response_model=List[schemas.PostVoteResponse])
def get_posts(db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user),limit:int = 10,skip:int = 0,search:Optional[str]=""):
    #using databse driver
    #cursor.execute("""SELECT * FROM posts WHERE id=%s""",(str(id)))
    #post = cursor.fetchone()
    #posts = db.query(models.Post).filter(models.Post.content.contains(search)).limit(limit).offset(skip).all()
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).outerjoin(models.Vote, models.Vote.post_id == models.Post.id).group_by(models.Post.id).filter(models.Post.content.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.get('/{id}',response_model=schemas.PostVoteResponse)
def get_post(id:int, response: Response, db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)): 
    #cursor.execute("""SELECT * FROM posts WHERE id=%s""",(str(id)))
    #post = cursor.fetchosne()
    #post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).outerjoin(models.Vote, models.Vote.post_id == models.Post.id).group_by(models.Post.id).first()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} not found')
    return post

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_posts(post:schemas.PostCreate, db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    #cursor.execute("""INSERT INTO posts(title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    #new_post = cursor.fetchone()
    #conn.commit() 
    new_post = models.Post(owner_id=current_user.id,**post.model_dump())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

       
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id:int,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    #cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    deleted_post_query = db.query(models.Post).filter(models.Post.id == id)
    deleted_post = deleted_post_query.first()
    
    if deleted_post == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} not found')   

    if deleted_post.owner_id!=current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN,detail=f'Not authorized to delete post with id:{id}')     

    deleted_post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
        

@router.put('/{id}',response_model=schemas.PostResponse)
def update_posts(id:int,post:schemas.PostUpdate,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id=%s RETURNING *""",
#   #                (post.title,post.content,post.published,str(id)))
#   # updated_post = cursor.fetchone()
#   # conn.commit()
    update_post_query = db.query(models.Post).filter(models.Post.id == id)
    update_post = update_post_query.first()
    if update_post == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} not found') 

    if update_post.owner_id!=current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN,detail=f'Not authorized to delete post with id:{id}')     
           
    update_post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    return update_post_query.first()