#_*_coding:utf-8_*_

import django
import redis

def redis_conn(django_settings):
    #print(django_settings.REDIS_CONN)
    pool = redis.ConnectionPool(host=django_settings.REDIS_CONN['HOST'],
                                port=django_settings.REDIS_CONN['PORT'],
                                db=1)
    r = redis.Redis(connection_pool=pool)
    return  r