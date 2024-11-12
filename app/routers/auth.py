from .. import models,schemas,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

router = APIRouter(tags = ['Authentication'])

@router.post('/login')
def login_user(user_credentials:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email ==user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Invalid credentials')

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Invalid credentials')

    access_token = oauth2.create_access_token(data={"user_id": str(user.id)})
    return {"access_token":access_token,
            "token_type": "bearer"}