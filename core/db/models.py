from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "lab_user"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
