import os

import yaml


def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    path = os.path.join(os.path.dirname(__file__) + '/user.yaml')
    f = open(path, encoding='UTF-8')
    s = yaml.load(f)
    f.close()
    return s


def StrToDict(toStr):
    s1 = toStr.split(";")
    dict = {}
    for s in s1:
        s2 = s.split("=")
        dict[s2[0]] = s2[1]
    return dict


if __name__ == '__main__':
    print(_get_yaml())
