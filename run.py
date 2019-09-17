# -*- coding: utf-8 -*-
# by dl
from Controller import app


# 打印所有路由
# print(app.url_map)

# @app.before_request
def beforeRequest():
    pass


if __name__ == '__main__':
    app.run(debug=True)
