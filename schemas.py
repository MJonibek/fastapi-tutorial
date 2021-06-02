from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from database import Base



class UserBase(BaseModel):

    username: str
    email: EmailStr

class BlogBase(BaseModel):

    title: str
    body: str

class UserCreate(UserBase):

    password: str


class BlogCreate(BlogBase):
    pass

class User(UserBase):

    class Config():
        orm_mode = True

class Blog(BlogBase):

    class Config():
        orm_mode = True



