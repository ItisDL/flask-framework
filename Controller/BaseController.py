# -*- coding: utf-8 -*-
# by dl
from flask import request
from Controller import app,cache,limiter
@app.route('/hello', methods=['get'])
# @cache.cached(timeout=5) #缓存5s过期
@limiter.limit('1 per day') #一天一次
def hello():
    print('没有使用缓存')
    return 'Hello World'

@app.route('/helloTwo', methods=['get'])
def helloTwo():
    return 'helloTwo'