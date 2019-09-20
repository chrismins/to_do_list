from handler import main
from db import main_db_engine
from flask import request, flash, render_template
from flask_login import LoginManager
from flask_login.utils import login_user
from models.user import User
from Crypto.Hash import SHA

login_manger = LoginManager()


@main.route('/login', methods=['POST'])
def login():
    user_name = request.values.get("user_name")
    password = request.values.get("password")
    hashObj = SHA.new()
    hashObj.update(password.encode())
    pwd = hashObj.hexdigest()
    user = main_db_engine.session.query(User).filter_by(user_name=user_name, pwd=pwd).first()
    if user:
        login_user(user)
        flash("logged in successfully")
        return render_template('login.html', form=user)


@login_manger.request_loader
def load_user_from_request():
    pass
