import copy
import re
import time

from loguru import logger

import Tools
from HttpUtils import HttpClient
from urlConf import urls


class redGrab:
    def __init__(self):
        self.httpClint = HttpClient()
        self.user_id = ""

    def sendRed(self, cookie):
        """
        抢红包
        :return:
        """
        time.sleep(0.8)
        for _ in range(2):
            self.httpClint.set_cookies(**Tools.StrToDict(cookie))
            user_id_re = re.compile("USERID=(\S+); ")
            self.user_id = re.search(user_id_re, cookie).group(1)
            data = {"user_id": self.user_id, "latitude": 114.06031036376953, "longitude": 22.570497512817383}
            signInUrls = copy.copy(urls["hongbao"])
            signInUrls["req_url"] = signInUrls["req_url"].format(self.user_id)
            signRsp = self.httpClint.send(urls=signInUrls, data=data)
            if signRsp and "联盟红包" in signRsp:
                print("恭喜您，十元小红包到手，快进入app查看")
            else:
                print(signRsp)


if __name__ == '__main__':
    cookie = "isg=BOLiWhcNyxiqXdZyVZYAuhHmOWxEM-ZN8YS37Sx7DdUr_4F5FMCpWvTsKf2odF7l; UTUSER=13427833; ut_ubt_ssid=esdsjykvbd6j51tpnazd6pgcxf9err7f_2019-07-10; tzyy=0e652fd568ee60d48e3d6a94b4971d3b; _utrace=57b668bd1b7ebe88b473406d60dd537d_2018-12-14; cna=ffeZFOshGXQCAbfvpoparfGj; track_id=1544751458|54c1a55c86c1a9ace6ea3e04d283945bd0c259ad9676626eac|6fce7a0c2f3ea42754a659127f065306; ubt_ssid=aucakq7qtf2n8v98iy5cs62nslkrn77b_2018-12-14; perf_ssid=91ocoxg4sesq2m126eqhernl65dsm1lc_2018-12-14; USERID=13427833; SID=bZm0fK8PjJCoKoaqmUI4lQigt63YMIEiXBSA"
    s = redGrab()
    s.sendRed(cookie=cookie)
