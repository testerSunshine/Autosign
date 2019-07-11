# coding=utf-8
import random

import time

urls = {
    "hongbao": {  # 登录接口
        "req_url": "/restapi/member/v1/users/{}/sign_in/limit/hongbao",
        "req_type": "post",
        "Referer": "https://h5.ele.me",
        "Host": "h5.ele.me",
        "Content-Type": 1,
        "re_try": 1,
        "re_time": 0.001,
        "s_time": 0.001,
        "is_logger": False,
        "is_json": True,
    },
    "hongbaos": {  # 登录接口
        "req_url": "/restapi/promotion/v1/users/{}/coupons",
        "req_type": "get",
        "Referer": "https://h5.ele.me",
        "Host": "h5.ele.me",
        "Content-Type": 1,
        "re_try": 1,
        "re_time": 0.001,
        "s_time": 0.001,
        "is_logger": False,
        "is_json": True,
    },
    "sign_in": {  # 签到
        "req_url": "/restapi/member/v1/users/{}/sign_in",
        "req_type": "get",
        "Referer": "https://h5.ele.me",
        "Host": "h5.ele.me",
        "Content-Type": 1,
        "re_try": 1,
        "re_time": 0.001,
        "s_time": 0.001,
        "is_logger": False,
        "is_json": True,
    },
    "daily": {  # 翻牌
        "req_url": "/restapi/member/v2/users/{}/sign_in/daily/prize",
        "req_type": "get",
        "Referer": "https://h5.ele.me",
        "Host": "h5.ele.me",
        "Content-Type": 1,
        "re_try": 1,
        "re_time": 0.001,
        "s_time": 0.001,
        "is_logger": False,
        "is_json": True,
    }

}