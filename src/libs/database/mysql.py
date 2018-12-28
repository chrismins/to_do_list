from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime, Date, Time, Numeric, DECIMAL


# BaseModel, Model To Dict
def to_dict(self, filter_fields=[]):
    item_dict = {}
    for c in self.__table__.columns:
        if c.name in filter_fields:
            continue
        if isinstance(c.type, DateTime):
            item_dict[c.name] = str(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        elif isinstance(c.type, Date):
            item_dict[c.name] = str(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        elif isinstance(c.type, Time):
            item_dict[c.name] = str(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        elif isinstance(c.type, Numeric):
            item_dict[c.name] = float(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        elif isinstance(c.type, DECIMAL):
            item_dict[c.name] = float(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        else:
            item_dict[c.name] = getattr(self, c.name, None)
    return item_dict

BaseModel = declarative_base()
metadata = BaseModel.metadata
BaseModel.to_dict = to_dict


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
        connection = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'
        connection = connection.format(self._user, self._password, self._host, self._port, self._db_name)
        return connection

    def __get_engine(self):
        return create_engine(self.db_connect, encoding=self._encoding)


class MysqlHandle(object):
    def __init__(self, **kwargs):
        super(MysqlHandle, self).__init__()
        self.engine = kwargs.get('engine', None)
