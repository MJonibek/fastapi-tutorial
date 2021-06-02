from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String)
    username = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates = "owner")



class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates = "blogs")

