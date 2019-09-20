# -*- coding: utf-8 -*-
# by dl
import datetime
import decimal
import json


# 处理函数
def _handler(x):
    if isinstance(x, datetime.datetime):
        return x.strftime('%Y-%m-%d %H:%M:%S')
    if isinstance(x, decimal.Decimal):
        return float(x)


# 成功返回值函数
def visitSuccess(code=200, msg='成功', data={}, extra_data={}):
    json_str = {'code': code, 'msg': msg, 'data': data, 'extra_data': extra_data}
    return json.dumps(json_str, default=_handler)


# 失败返回值函数
def visitFail(code=-500, msg='失败', data={}, extra_data={}):
    json_str = {'code': code, 'msg': msg, 'data': data, 'extra_data': extra_data}
    return json.dumps(json_str, default=_handler)
