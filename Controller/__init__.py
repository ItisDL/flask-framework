# -*- coding: utf-8 -*-
# by dl
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
import Controller.Base
