from libs.database.mysql import BaseModel
from sqlalchemy import Column, String


class UserPasswordRel(BaseModel):
    __tablename__ = 'user_password_rel'

    id = Column(String(40), primary_key=True)
    user_id = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
