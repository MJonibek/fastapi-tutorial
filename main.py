from typing import Optional, List

from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import schemas
import crud


app = FastAPI()
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/user/{id}/create_blog', tags = ['blogs'])
def create(id:int, request: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db, request, id)

@app.post('/user', tags = ['users'])
def create(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, request)

@app.get('/user',  response_model = List[schemas.User], tags = ['users'])
def all_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return users

@app.get('/user/{id}', response_model = schemas.User, tags = ['users'])
def user(id:int, db: Session = Depends(get_db)):
    user = crud.get_user(db, id)
    return user

@app.get('/user/{id}/blogs', response_model = List[schemas.Blog], tags = ['users'])
def user_blog(id:int, db: Session = Depends(get_db)):
    blogs = crud.get_user_blog(db, id)
    return blogs

@app.delete('blog/delete/{id}', tags = ['blogs'])
def delete_blog(id:int, db: Session = Depends(get_db)):
    return crud.delete_blog(db ,id)