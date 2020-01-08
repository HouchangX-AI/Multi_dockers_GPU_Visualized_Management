# coding:utf8
from flask import Blueprint

wx_blu = Blueprint("wx", __name__)

from . import views
