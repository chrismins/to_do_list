# from server import db_handle
from server import database_engine
from models import User

if __name__ == '__main__':
    rest = database_engine.session.query(User).all()
    print(rest)