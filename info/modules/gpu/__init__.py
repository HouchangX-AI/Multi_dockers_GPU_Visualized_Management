# coding:utf8
from flask import Blueprint

gpu_blu = Blueprint("gpu", __name__, url_prefix='/gpu')

from . import views
