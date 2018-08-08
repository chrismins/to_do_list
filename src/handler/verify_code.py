import random
from . import main
from flask import request
# from libs.database.redis import redis_verify_code
from qcloudsms_py import SmsSingleSender
from setting import verify_code_setting


@main.route("/get_verify_code", methods=["POST"])
def get_verify_code():
    try:
        mobile = request.args.get("mobile")
        code = random.randint(100000, 999999)
        APPID = verify_code_setting["appid"]
        APPKEY = verify_code_setting["appkey"]
        template_id = verify_code_setting["template_id"]
        params = code
        ssender = SmsSingleSender(APPID, APPKEY)
        result = ssender.send_with_param(86, mobile, template_id, params)
        return result
    except Exception as ex:
        raise ex
