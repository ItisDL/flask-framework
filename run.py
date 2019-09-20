# -*- coding: utf-8 -*-
# by dl
from Controller import app
from Config import config
from Auth.JwtAuthC import JwtAuth
from flask import request
from Common import func
# 打印所有路由
# print(app.url_map)

@app.before_request
def beforeRequest():
    auth_token = request.headers.get('OSR-BearerToken')
    print(auth_token)
    if JwtAuth.decode_auth_token(auth_token) is not True:
        return func.visitFail(code=300)
    # print(res)
    pass


if __name__ == '__main__':
    app.debug = config.app_debug
    app.run()
