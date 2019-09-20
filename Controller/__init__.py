# -*- coding: utf-8 -*-
# by dl
from flask import Flask
from flask_cors import CORS
from flask_cache import Cache
from Config import cache_config
app = Flask(__name__)
# 缓存
cache = Cache(app, config=cache_config.Redis, with_jinja2_ext=False)
cache.init_app(app)
# 跨域
CORS(app, supports_credentials=True)
# 载入控制器
import Controller.Base
