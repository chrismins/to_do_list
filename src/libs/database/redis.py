# from server import app
# from setting import redis_setting
# from flask.ext.redis import FlaskRedis
import redis


# app.config["REDIS_URL"] = redis_setting["REDIS_URL_0"]
# redis_engine = FlaskRedis(app)

class RedisEngine(object):
    def __init__(self, **kwargs):
        self.host = kwargs.get('host', '127.0.0.1')
        self.port = kwargs.get('port', 6379)
        self.db = kwargs.get('db', 0)
        self.password = kwargs.get('password', '')
        self.conn = self.get_connect()

    def get_connect(self):
        if not isinstance(self.password, (str, int)):
            return None
        if not self.password:
            conn = redis.StrictRedis(host=self.host, port=self.port, db=self.db)
        else:
            conn = redis.StrictRedis(host=self.host, port=self.port, password=self.password, db=self.db)

        return conn

    def set(self, name, code, expire=300):
        flag = self.conn.set(name, code)
        if not flag:
            return flag
        if expire is not None:
            flag = self.conn.expire(name, expire)
        return flag

    def get(self, name):
        result = self.conn.get(name)
        return result

    def delete(self, name):
        return self.conn.delete(name)
