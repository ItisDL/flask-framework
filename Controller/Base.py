# -*- coding: utf-8 -*-
# by dl
from Controller import app
@app.route('/hello', methods=['get'])
def hello():
    return 'Hello World'

@app.route('/helloTwo', methods=['get'])
def helloTwo():
    return 'helloTwo'