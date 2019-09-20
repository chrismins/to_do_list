from sqlalchemy import Column, String, Integer, DateTime, text
from libs.database.mysql import BaseModel
from sqlalchemy.dialects.mysql.types import TINYINT
from flask_login import UserMixin


class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    user_id = Column(String(40), primary_key=True)
    user_name = Column(String(40), nullable=False)
    mobile = Column(String(40), nullable=False)
    pwd = Column(String(50), nullable=False)
    email = Column(String(40))
    birthday = Column(String(40))
    province = Column(String(40))
    city = Column(String(40))
    area = Column(String(200))
    address = Column(String(200))
    images = Column(String(400))
    status = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.status = 0

    def get_id(self):
        # user_id = kwargs.get("user_id")
        return self.user_id
