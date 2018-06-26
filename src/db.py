from sqlalchemy.orm import scoped_session, sessionmaker
from libs.database.mysql import MysqlEngine

mysql_setting = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "port": 3306,
    "db_name": "dream_list"
}

main_db_engine = MysqlEngine(**mysql_setting)
DBSession = scoped_session(sessionmaker(bind=main_db_engine.db_engine))
main_db_engine.session = DBSession


def session_close():
    DBSession.remove()
