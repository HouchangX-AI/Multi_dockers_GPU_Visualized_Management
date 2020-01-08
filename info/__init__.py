from flask import Flask, render_template, g
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_session import Session

# from config import Config, DevlopmentConfig, ProductionConfig, UnittestConfig
from config import configs
import logging
from logging.handlers import RotatingFileHandler

from info.utils.common import do_index_filter, user_login_data


def setup_log(level):
    """根据创建app时的配置环境，加载日志等级"""
    # 设置日志的记录等级
    logging.basicConfig(level=level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


# 创建SQLAlchemy对象
db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    """创建app的工厂方法
    参数：根据参数选择不同的配置类
    """

    # 根据创建app时的配置环境，加载日志等级
    # setup_log(configs[config_name].LEVEL_LOG)

    # info
    app = Flask(__name__)

    # 获取配置信息
    app.config.from_object(configs[config_name])

    # 创建连接到MySQL数据库的对象
    # db = SQLAlchemy(app)
    db.init_app(app)

    # 创建连接到redis数据库的对象
    # global redis_store
    # redis_store = StrictRedis(host=configs[config_name].REDIS_HOST, port=configs[config_name].REDIS_PORT,
    #                           decode_responses=True)

    # 开启CSRF保护：因为项目中的表单不再使用FlaskForm来实现，所以不会自动的开启CSRF保护，需要自己开启
    # CSRFProtect(app)

    # # 使用请求勾子，实现每个响应中写入cookie
    # @app.after_request
    # def setup_csrftoken(response):
    #     # 生成csrf_token的值
    #     csrf_token = generate_csrf()
    #
    #     # 将csrf_token的值写入到cookie
    #     response.set_cookie('csrf_token', csrf_token)
    #     return response
    #
    #     # 将过滤器添加到模板过滤器列表中
    #
    # app.add_template_filter(do_index_filter, "index_filter")

    # 指定session数据存储在后端的位置
    # Session(app)
    #
    # # 注册路由
    # # 注意点：蓝图在哪里使用，注册，就在哪里导入，避免出现由于蓝图导入过早，造成变量不存在的情况

    # 注册wx蓝图对象
    from info.modules.wx import wx_blu
    app.register_blueprint(wx_blu)

    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    from info.modules.disk import disk_blu
    app.register_blueprint(disk_blu)

    return app
