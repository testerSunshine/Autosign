# -*- coding: UTF-8 -*-


import copy
import re
from HttpUtils import HttpClient
from RedisUtils import redisUtils
from Tools import StrToDict, _get_yaml
from urlConf import urls


HASH_KEY = "wxp"


def elmRedInfo(cookie):
    """
    获取对应的优惠券
    :return:
    """
    httpClint = HttpClient()
    httpClint.set_cookies(**StrToDict(cookie))
    user_id_re = re.compile("USERID=(\S+); ")
    user_id = re.search(user_id_re, cookie).group(1)
    redInfoUrls = copy.copy(urls["hongbaos"])
    redInfoUrls["req_url"] = redInfoUrls["req_url"].format(user_id)
    return httpClint.send(redInfoUrls)


def saveElmRedInfo():
    """
    取到的值存redis
    :return:
    """
    users = _get_yaml()
    redisConn = redisUtils().redis_conn()
    data = []
    for user in users["cookies"]:
        elmRedInfoRps = elmRedInfo(user.get("cookie", ""))
        data.append({"name": user.get("name", ""), "coupon": elmRedInfoRps})
    redisConn.hset("data", HASH_KEY, str(data))
    print(redisConn.hget("data", HASH_KEY).decode())


if __name__ == '__main__':
    saveElmRedInfo()