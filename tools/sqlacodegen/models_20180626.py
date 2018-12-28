# coding: utf-8
from sqlalchemy import Column, DateTime, INTEGER, String, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Dream(Base):
    __tablename__ = 'dreams'

    id = Column(String(40), primary_key=True)
    user_id = Column(String(40), nullable=False)
    title = Column(String(400), nullable=False)
    word = Column(Text, nullable=False)
    status = Column(INTEGER(11), nullable=False)
    remark = Column(String(400))
    created = Column(DateTime, nullable=False)


class User(Base):
    __tablename__ = 'user'

    user_id = Column(String(40), primary_key=True)
    user_name = Column(String(40), nullable=False)
    real_name = Column(String(40))
    mobile = Column(INTEGER(11), nullable=False)
    email = Column(String(40))
    birthday = Column(String(40))
    province = Column(String(40))
    city = Column(String(40))
    area = Column(String(200))
    images = Column(String(400))
    status = Column(INTEGER(40), nullable=False, server_default=text("'0'"))
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)


class UserPasswordRel(Base):
    __tablename__ = 'user_password_rel'

    id = Column(String(40), primary_key=True)
    user_id = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
