from sqlalchemy import Column, String, Integer, DateTime, text
from libs.database.mysql import BaseModel
# from server import db_handle


class User(BaseModel):
    __tablename__ = 'user'

    user_id = Column(String(40), primary_key=True)
    user_name = Column(String(40), nullable=False)
    real_name = Column(String(40))
    mobile = Column(Integer, nullable=False)
    email = Column(String(40))
    birthday = Column(String(40))
    province = Column(String(40))
    city = Column(String(40))
    area = Column(String(200))
    images = Column(String(400))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
