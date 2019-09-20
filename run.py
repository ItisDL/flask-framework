# -*- coding: utf-8 -*-
# by dl
from Controller import app
from Config import config
from CommonClass.JwtAuthC import JwtAuth
from flask import request
from Common import func
# 打印所有路由
# print(app.url_map)

@app.before_request
def beforeRequest():
    # 是否在白名单
    if not func.dontNeedJWT(request.path):
        # token是否正确
        auth_token = request.headers.get('OSR-BearerToken')
        authRes = JwtAuth.decode_auth_token(auth_token)
        # 如果在指定的错误码范围则返回错误
        if authRes in ['JWT00001','JWT00002']:
            return func.visitFail(msg=authRes)


if __name__ == '__main__':
    app.debug = config.app_debug
    app.run()
