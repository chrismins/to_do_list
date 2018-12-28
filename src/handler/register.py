from handler import main
from flask import request
from flask.wrappers import Response
from models import User
from db import main_db_engine
from handler.verify_code import checkout_verify_code
from datetime import datetime
import uuid
from Crypto.Hash import SHA


@main.route("/register", methods=["POST"])
def serve_register():
    user_name = request.values.get("user_name")
    password = request.values.get("password")
    mobile = request.values.get("mobile")
    verify_code = request.values.get("verify_code")
    user_id = str(uuid.uuid1()).replace('-', '')
    rest = checkout_verify_code(mobile=mobile, verify_code=verify_code)
    if password is not None:
        hashObj = SHA.new()
        hashObj.update(password.encode())
        pwd = hashObj.hexdigest()
    else:
        return "密码不能为空"
    if rest:
        created = datetime.now()
        user_info = User(user_id=user_id, user_name=user_name, pwd=pwd, mobile=mobile, created=created)
        main_db_engine.session().add(user_info)
        flag = main_db_engine.session().commit()
        if not flag:
            result = "注册成功！！！"
        else:
            result = "注册失败！！！"
    else:
        result = "验证码不符合！！！"
    return result
