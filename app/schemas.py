from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing  import Optional
from pydantic.types import conint

class UserBase(BaseModel):
    email: EmailStr
    password:str

class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    id : int
    email : EmailStr
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass


class PostResponse(PostBase):
    id:int
    created_at : datetime
    owner_id : int
    owner : UserResponse

    class Config:
        orm_mode = True

class PostVoteResponse(BaseModel):
    Post: PostResponse
    votes: int
    class Config:
        orm_mode = True

class VoteBase(BaseModel):
    post_id : int
    dir : conint(le=1)



