import copy
import re

from loguru import logger

import Tools
from HttpUtils import HttpClient
from urlConf import urls


class signIn:
    def __init__(self):
        self.httpClint = HttpClient()
        self.user_id = ""

    def sendSign(self, cookie):
        """
        签到
        :return:
        """
        self.httpClint.set_cookies(**Tools.StrToDict(cookie))
        user_id_re = re.compile("USERID=(\S+); ")
        self.user_id = re.search(user_id_re, cookie).group(1)
        data = {
             "channel": 'app',
             "captcha_code": "",
             "captcha_hash": "",
             "source": "main",
             "latitude": 114.06031036376953, "longitude": 22.570497512817383
        }
        signInUrls = copy.copy(urls["sign_in"])
        signInUrls["req_url"] = signInUrls["req_url"].format(self.user_id)
        signRsp = self.httpClint.send(urls=signInUrls, data=data)
        logger.info(signRsp)
        self.daily()

    def daily(self):
        """
        签到完成之后有一次翻牌
        :return:
        """
        dailyUrls = copy.copy(urls["daily"])
        dailyUrls["req_url"] = dailyUrls["req_url"].format(self.user_id)
        data = {
             "channel": 'app',
             "index": 1,
             "latitude": 114.06031036376953, "longitude": 22.570497512817383

        }
        daily = self.httpClint.send(urls=dailyUrls, data=data)
        logger.info(daily)


if __name__ == '__main__':
    cookie = "SID=VHN1J9okuzW169ZIVw8OMfWMphHGW7HtuHIw; USERID=266977222; UTUSER=266977222; ZDS=1.0|1562813695|iX+WoCdPZQUHLdhXAsdynn7Sx3/y00zaL9veuKKVhElRP1Jc+B89xjaPj8rzik0P; isg=BJOTw8Ezypx184bIkQtINCURIBG9SCcK0r4EfUWzf7LpxLZm3BoFW-NX_rSq_38C; track_id=1562813695|6d95a00f5ee5c789a4df84fe6a7b3ff46929f913faa2a60aff|053c915f1f32c6e158272adac73efa0e; cna=65KtFd6y8F4CATr2J1qoA++8; ut_ubt_ssid=a5iqi539ne5zy4tf6fsw56qcvvjoqvq6_2019-07-11; _utrace=7ab6d79bd482aab4a92268ee4243e8f0_2019-07-11; ubt_ssid=hdx8lvl1gj3klfa0l7yvirlo255coiso_2019-07-11"
    s = signIn()
    s.sendSign(cookie=cookie)
