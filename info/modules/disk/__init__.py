# coding:utf8
from flask import Blueprint

disk_blu = Blueprint("disk", __name__, url_prefix='/disk')

from . import views
