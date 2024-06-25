from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
class Userout(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    # password: str
    class Config():
        from_attributes = True

class PostBase(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    owner_id: int


class for_Create_Post(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(for_Create_Post):
    pass
class Postss(BaseModel):
    id : int
    title: str
    content: str
    published : bool
    owner_id: int
    owner: Userout

    class Config:
        from_attributes = True

class PostVote(BaseModel):
    Post: Postss
    Votes: int
    class Config:
        from_attributes = True

class login(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    id: Optional[int] = None

class vote(BaseModel):
    post_id: int
    dir: int