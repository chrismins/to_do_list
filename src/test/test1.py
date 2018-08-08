from unittest import TestCase
import requests


class SmsTest(TestCase):
    def test_sent_message(self):
        url = "http://127.0.0.1:8000/register"
        datas = {
            "user_name": "张三",
            "password": "123456"
        }
        result = requests.post(url=url, data=datas)
        print(url)
        # result.json()
        # print(url)

