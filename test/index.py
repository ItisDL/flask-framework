# -*- coding: utf-8 -*-
# by dl
from common import func, redisdb
from time import time

if __name__ == '__main__':
    r = redisdb.con(0)
    # res = r.set('k3', time(), 3600 * 6)
    # print(res)
    res = r.get('k4')
    print(res)

#
# table = 'user_shop'
# data = {'name': 'DL2',
#         'account': 'DLacc',
#         'type': 'root'}
# where = {'id': '1'}
#
# res = func.pm_db(act='update', table=table, data=data,where=where)
# print(res)
