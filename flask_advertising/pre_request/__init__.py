# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 17:42
# @Author  : Liu Yalong
# @File    : __init__.py.py
from flask import Blueprint

bp_pre_request = Blueprint('pre_request', __name__)
from . import views
