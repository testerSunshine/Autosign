# -*- coding: utf8 -*-

__author__ = 'MR.wen'

from configparser import ConfigParser
import subprocess
import sys
import logging
import os
import time
import logging.handlers

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))



def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def sleep(s):
    return time.sleep(s)


def cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class ConfigIni():
    def __init__(self):
        self.current_directory = os.path.split(
            os.path.realpath(sys.argv[0]))[0]
        self.path = os.path.split(__file__)[0].replace('PO', 'config.ini')
        self.cf = ConfigParser.ConfigParser()

        self.cf.read(self.path)

    def get_ini(self, title, value):
        return self.cf.get(title, value)

    def set_ini(self, title, value, text):
        self.cf.set(title, value, text)
        return self.cf.write(open(self.path, "wb"))

    def add_ini(self, title):
        self.cf.add_section(title)
        return self.cf.write(open(self.path))

    def get_options(self, data):
        # 获取所有的section
        options = self.cf.options(data)
        return options


class colour:
    @staticmethod
    def c(msg, colour):
        try:
            from termcolor import colored, cprint
            p = lambda x: cprint(x, '%s' % colour)
            return p(msg)
        except:
            print (msg)

    @staticmethod
    def show_verbose(msg):
        colour.c(msg, 'green')

    @staticmethod
    def show_debug(msg):
        colour.c(msg, 'blue')

    @staticmethod
    def show_info(msg):
        colour.c(msg, 'white')

    @staticmethod
    def show_warn(msg):
        colour.c(msg, 'yellow')

    @staticmethod
    def show_error(msg):
        colour.c(msg, 'red')


class Logging:
    def __init__(self):
        pass
    flag = True

    @staticmethod
    def error(msg):
        if Logging.flag:
            # print get_now_time() + " [Error]:" + "".join(msg)
            colour.show_error(get_now_time() + " [Error]:" + "".join(str(msg)) + "\n")

    @staticmethod
    def warn(msg):
        if Logging.flag:
            colour.show_warn(get_now_time() + " [Warn]:" + "".join(str(msg)) + "\n")

    @staticmethod
    def info(msg):
        if Logging.flag:
            colour.show_info(get_now_time() + " [Info]:" + "".join(str(msg)) + "\n")

    @staticmethod
    def debug(msg):
        if Logging.flag:
            colour.show_debug(get_now_time() + " [Debug]:" + "".join(str(msg)) + "\n")

    @staticmethod
    def success(msg):
        if Logging.flag:
            colour.show_verbose(get_now_time() + " [Success]:" + "".join(str(msg)) + "\n")


def l():
    """
    打印log
    文件名+函数名,return
    :return:
    """

    def log(func):
        def wrapper(*args, **kwargs):
            t = func(*args, **kwargs)
            filename = str(sys.argv[0]).split('/')[-1].split('.')[0]
            Logging.info('{}:{}, return:{}'.format(filename, func.__name__, t))
            return t

        return wrapper

    return log


class GetMyLog():
    @staticmethod
    def createFile():
        runpath = os.getcwd()
        if 'TestCase' in runpath:
            runpath = os.path.join(runpath, os.pardir, os.pardir, os.pardir)
        logFile = os.path.abspath(os.path.join(runpath, 'Report', day, "steps"))
        if os.path.exists(logFile):
            filename = os.path.normpath(logFile + '/' + '%s_setps.log' % day)
            return filename
        else:
            os.makedirs(logFile)
            filename = os.path.normpath(logFile + '/' + '%s_setps.log' % day)
            return filename

    @staticmethod
    def myLog():
        '''
        调取log
        :return: logger
        '''
        LOG_FILE = GetMyLog.createFile()
        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
        fmt = '%(asctime)s - %(name)s -%(levelname)s -%(message)s'
        formatter = logging.Formatter(fmt)  # 实例化formatter
        handler.setFormatter(formatter)  # 为handler添加formatter
        logger = logging.getLogger('test_steps')
        logger.addHandler(handler)  # 为logger添加handler
        logger.setLevel(logging.DEBUG)
        return logger
