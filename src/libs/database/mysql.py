from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class MysqlEngine(object):
    def __init__(self, **kwargs):
        self._host = kwargs.get('host', '127.0.0.1')
        self._user = kwargs.get('user', '')
        self._password = kwargs.get('password', '')
        self._db_name = kwargs.get('db_name', '')
        self._port = kwargs.get('port', '3306')
        self._charset = kwargs.get('charset', 'utf8')
        self._encoding = kwargs.get('encoding', 'utf-8')
        self.db_connect = self.get_connect()
        self.db_engine = self.__get_engine()
        self.session = None

    def get_connect(self):
        connection = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'
        connection = connection.format(self._user, self._password, self._host, self._port, self._db_name)
        return connection

    def __get_engine(self):
        return create_engine(self.db_connect, encoding=self._encoding)
