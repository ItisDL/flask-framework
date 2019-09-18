# -*- coding: utf-8 -*-
# by dl
from Controller import app
from Config.config import app_debug

# 打印所有路由
# print(app.url_map)

# @app.before_request
def beforeRequest():
    pass


if __name__ == '__main__':
    app.debug = app_debug
    app.run(debug=True)
