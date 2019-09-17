# -*- coding: utf-8 -*-
# by dl
from Controller import app
@app.route('/hello', methods=['get'])
def hello():
    return 'Hello World'