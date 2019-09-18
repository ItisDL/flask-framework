# -*- coding: utf-8 -*-
# by dl
from Controller import app,cache
@app.route('/hello', methods=['get'])
@cache.cached(timeout=5)
def hello():
    print('没有使用缓存')
    return 'Hello World'

@app.route('/helloTwo', methods=['get'])
def helloTwo():
    return 'helloTwo'