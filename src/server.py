from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from handler import main as main_blueprint
from db import main_db_engine
from flask_login import LoginManager
# from flask_redis import FlaskRedis
# from setting import redis_setting

# 实例化Flask应用
app = Flask(__name__)

# 注册handle
app.register_blueprint(main_blueprint)
login_manger = LoginManager()
login_manger.init_app(app)

# 初始化数据库
database_engine = main_db_engine

# app.config["REDIS_URL"] = redis_setting["REDIS_URL_0"]
# redis_engine = FlaskRedis(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = main_db_engine.db_connect
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db_handle = SQLAlchemy(app)



