# -*- coding: utf-8 -*-
# by dl
from Controller import app
from Config.config import app_debug
from Auth.JwtAuthC import JwtAuth
from flask import request
# 打印所有路由
# print(app.url_map)

# @app.before_request
def beforeRequest():
    auth_token = request.headers.get('OSR-BearerToken')
    JwtAuth.decode_auth_token(auth_token)
    pass


if __name__ == '__main__':
    app.debug = app_debug
    app.run(debug=True)
