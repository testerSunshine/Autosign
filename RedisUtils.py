import datetime

import redis


class redisUtils:
    def __init__(self):
        self.redis_config = {
            "host": "148.70.105.137",
            "port": 6379,
            "password": "qazWSX1995!"
        }

    def redis_conn(self):
        """
        redis连接池
        :return:
        """
        redis_pool = redis.ConnectionPool(**self.redis_config)
        conn = redis.Redis(connection_pool=redis_pool)
        return conn


if __name__ == '__main__':
   pass
