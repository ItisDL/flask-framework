# -*- coding: utf-8 -*-
# by dl
from Controller import app
@app.route('/hello', methods=['get'])
def hello():
    return 'Hello World'

@app.route('/hello2', methods=['get'])
def hello():
    return 'Hello World2'