from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def get_all_users(db:Session):
    return db.query(models.User).all()

def get_user(db:Session, id:int):
    return db.query(models.User).filter(models.User.id == id).first()

def get_user_blog(db: Session, id: int):
    return db.query(models.Blog).filter(models.Blog.user_id == id).all()

def create_user(db: Session, request: schemas.UserCreate):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(email = request.email, username = request.username, password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_blog(db:Session, request: schemas.BlogCreate, user_id: int):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(db:Session, id: int):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session = False)
    db.commit()
    return 'Blog deleted'
