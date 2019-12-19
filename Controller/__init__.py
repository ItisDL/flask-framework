# -*- coding: utf-8 -*-
# by dl
from flask import Flask
from flask_cors import CORS
from flask_cache import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from Config import cache_config

app = Flask(__name__)
# 缓存
cache = Cache(app, config=cache_config.Redis, with_jinja2_ext=False)
cache.init_app(app)
# 跨域
CORS(app, supports_credentials=True)
# 访问控制
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=['200 per day', '50 per hour']
)
# 载入控制器
import Controller.BaseController
