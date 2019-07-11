import json
import os
import random
import socket
from collections import OrderedDict
from time import sleep

import requests
from loguru import logger
from requests_toolbelt import MultipartEncoder

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def _set_header_default():
    header_dict = OrderedDict()
    header_dict[
        "User-Agent"] = "Rajax/1 Apple/iPhone7,1 iOS/12.1 Eleme/8.5.1 ID/3B0EE632-2E54-45F8-953F-6FB9AB9F8889; IsJailbroken/0 ASI/71CA293E-5FF6-4267-9954-D44BC8E3984E Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 AliApp(ELMC/8.5.1)"
    return header_dict


class HttpClient(object):

    def __init__(self):
        """
        :param method:
        :param headers: Must be a dict. Such as headers={'Content_Type':'text/html'}
        """
        self.initS()
        self._cdn = ["47.101.30.101", "47.102.62.122", "47.101.30.100", "39.97.7.151", "47.102.62.121"]

    def initS(self):
        self._s = requests.Session()
        self._s.headers.update(_set_header_default())
        return self

    def set_cookies(self, **kwargs):
        """
        设置cookies
        :param kwargs:
        :return:
        """
        for k, v in kwargs.items():
            self._s.cookies.set(k, v)

    def get_cookies(self):
        """
        获取cookie
        :return:
        """
        cookies = self._s.cookies.get_dict()
        logger.info("cookies: {}".format(cookies))
        return cookies

    def del_cookies(self):
        """
        删除所有的key
        :return:
        """
        self._s.cookies.clear()

    def del_cookies_by_key(self, key):
        """
        删除指定key的session
        :return:
        """
        self._s.cookies.set(key, None)

    def setHeaders(self, headers):
        self._s.headers.update(headers)
        return self

    def resetHeaders(self):
        self._s.headers.clear()
        self._s.headers.update(_set_header_default())

    def getHeadersHost(self):
        return self._s.headers["Host"]

    def setHeadersHost(self, host):
        self._s.headers.update({"Host": host})
        return self

    def getHeadersReferer(self):
        return self._s.headers["Referer"]

    def setHeadersReferer(self, referer):
        self._s.headers.update({"Referer": referer})
        return self

    @property
    def cdn(self):
        return self._cdn

    @cdn.setter
    def cdn(self, cdn):
        self._cdn = cdn

    def send(self, urls, data=None, **kwargs):
        """send request to url.If response 200,return response, else return None."""
        allow_redirects = False
        is_logger = urls["is_logger"]
        if "Referer" in urls:
            self.setHeadersReferer(urls["Referer"])
        if data:
            method = "post"
            # self.setHeaders({"Content-Length": "{0}".format(len(data))})
        else:
            method = "get"
            # self.resetHeaders()
        if "is_multipart_data" in urls and urls["is_multipart_data"]:
            data = MultipartEncoder(data)
            self.setHeaders({"Content-Type": data.content_type})
            self.setHeaders(urls.get("headers", {}))
        if is_logger:
            logger.info(
                "url: {0}\n入参: {1}\n请求方式: {2}\n".format(urls["req_url"], data, method, ))
        self.setHeadersHost(urls["Host"])
        try:
            requests.packages.urllib3.disable_warnings()
            response = self._s.request(method=method,
                                       timeout=20,
                                       url="https://" + self._cdn[random.randint(0, len(self._cdn) - 1)] + urls[
                                           "req_url"],
                                       data=data,
                                       allow_redirects=allow_redirects,
                                       verify=False,
                                       **kwargs)
            if response.status_code == 400:
                logger.info("接口状态码：{}, {}".format(response.status_code, response.content.decode()))
                if response.content:
                    if is_logger:
                        logger.info(
                            "出参：{0}".format(response.content.decode()))
                    if urls["is_json"]:
                        return json.loads(response.content.decode())
                    elif urls.get("not_decode", ""):
                        return response.content
                    else:
                        return response.content.decode()
            if response.status_code == 200 or response.status_code == 201:
                # U.Logging.info("请求{}完成，不包括请求等待和封ip等待，只考虑网络io，参考耗时: {}ms".format(urls["req_url"], (datetime.datetime.now() - startTime).microseconds / 1000))
                if response.content:
                    if is_logger:
                        logger.info(
                            "出参：{0}".format(response.content.decode()))
                    if urls["is_json"]:
                        return json.loads(response.content.decode())
                    elif urls.get("not_decode", ""):
                        return response.content
                    else:
                        return response.content.decode()
                else:
                    logger.info(
                        "url: {} 返回参数为空".format(urls["req_url"]))
            elif response.status_code == 403:
                logger.error("ip 被封, 等待2秒")
                sleep(2)
            else:
                sleep(urls["re_time"])
        except (requests.exceptions.Timeout, requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            pass
        except socket.error:
            pass


if __name__ == '__main__':
    pass
