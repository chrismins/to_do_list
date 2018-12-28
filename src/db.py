from sqlalchemy.orm import scoped_session, sessionmaker
from libs.database.mysql import MysqlEngine
from libs.database.redis import RedisEngine
from setting import mysql_setting, redis_db_0_config

main_db_engine = MysqlEngine(**mysql_setting)
DBSession = scoped_session(sessionmaker(bind=main_db_engine.db_engine))
main_db_engine.session = DBSession

redis_engine = RedisEngine(**redis_db_0_config)

def session_close():
    DBSession.remove()
