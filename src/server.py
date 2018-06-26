from flask import Flask
from handler import main as main_blueprint
from db import main_db_engine

# 实例化Flask应用
app = Flask(__name__)

# 注册handle
app.register_blueprint(main_blueprint)

# 初始化数据库
database_engine = main_db_engine

