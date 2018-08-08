from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from handler import main as main_blueprint
from db import main_db_engine

# 实例化Flask应用
app = Flask(__name__)

# 注册handle
app.register_blueprint(main_blueprint)

# 初始化数据库
database_engine = main_db_engine
# app.config['SQLALCHEMY_DATABASE_URI'] = main_db_engine.db_connect
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db_handle = SQLAlchemy(app)



