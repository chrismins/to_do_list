from sqlalchemy import Column, String, INTEGER, DateTime, text
from libs.database.mysql import BaseModel


class User(BaseModel):
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
