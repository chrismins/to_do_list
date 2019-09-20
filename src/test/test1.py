from unittest import TestCase
import requests



class SmsTest(TestCase):
    def test_register(self):
        url = "http://127.0.0.1:8000/register"
        datas = {
            "user_name": "test222",
            "password": "123456",
            "mobile": 18625006875,
            "verify_code": 946283
        }
        result = requests.post(url=url, data=datas)
        print(result)
        # result.json()
        # print(url)

    def test_get_code(self):
        url = "http://127.0.0.1:8000/get_verify_code"
        data = {
            "mobile": 18625006875
        }
        result = requests.get(url, data=data)
        print(str(result.content, encoding='utf-8'))

    def test_check_mobile(self):
        url = "http://127.0.0.1:8000/verify_mobile"
        data = {
            "mobile": 18625006875
        }
        result = requests.get(url, data=data)
        print(str(result.content, encoding='utf-8'))

    def test_login(self):
        url = "http://127.0.0.1:8000/login"
        datas = {
            "user_name": "王五",
            "password": "786346"
        }
        result = requests.post(url=url, data=datas)
        print(result)
        # result.json()
        # print(url)

