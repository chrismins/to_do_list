import random
from . import main
from flask import request
from db import redis_engine, main_db_engine
from qcloudsms_py import SmsSingleSender
from setting import verify_code_setting
from models.user import User


@main.route("/get_verify_code", methods=["get"])
def get_verify_code():
    """
    获取验证码
    :return:
    """
    try:
        mobile = request.values.get("mobile")
        code = random.randint(100000, 999999)
        name = "verify_code: mobile:{}:".format(mobile)
        redis_engine.set(name, str(code))
        APPID = verify_code_setting["appid"]
        APPKEY = verify_code_setting["appkey"]
        template_id = verify_code_setting["template_id"]
        ssender = SmsSingleSender(APPID, APPKEY)
        code_params = [code, 1]
        result = ssender.send_with_param(86, mobile, template_id, code_params)
        if result["errmsg"] == 'OK':
            result = True
        else:
            result = False
        return result
    except Exception as ex:
        raise ex


@main.route("/verify_mobile", methods=['get'])
def check_mobile():
    """
    验证手机号是否存在
    :return:
    """
    try:
        mobile = request.values.get("mobile")
        result = main_db_engine.session.query(User).filter_by(mobile=mobile).all()
        if len(result) != 0:
            return False
        else:
            return True
    except Exception as ex:
        raise ex


def checkout_verify_code(**kwargs):
    """
    验证验证码是否正确
    :return:
    """
    try:
        mobile = kwargs.get('mobile')
        verify_code = kwargs.get('verify_code')
        name = "verify_code: mobile:{}:".format(mobile)
        in_code = redis_engine.get(name)
        in_code = in_code.decode('utf-8')
        if verify_code == in_code:
            redis_engine.delete(name)
            return True
        return False
    except Exception as ex:
        raise ex
