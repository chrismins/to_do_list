from libs.database.mysql import BaseModel
from sqlalchemy import Column, String, Text, Integer, DateTime


class Dream(BaseModel):
    __tablename__ = 'dreams'

    id = Column(String(40), primary_key=True)
    user_id = Column(String(40), nullable=False)
    title = Column(String(400), nullable=False)
    word = Column(Text, nullable=False)
    status = Column(Integer, nullable=False)
    remark = Column(String(400))
    created = Column(DateTime, nullable=False)
