# coding:utf8
from functools import wraps

# 自定义模板过滤器
from flask import session, current_app, g


def do_index_filter(index):
    if index == 1:
        return "first"
    elif index == 2:
        return "second"
    elif index == 3:
        return "third"
    else:
        return ""


# 装饰器,封装用户登陆数据
def user_login_data(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):

        # 获取用户编号
        user_id = session.get("user_id")

        # 查询用户对象
        user = None
        if user_id:
            try:
                from info.models import User
                user = User.query.get(user_id)
            except Exception as e:
                current_app.logger.error(e)

        # 使用g对象保存
        g.user = user

        return view_func(*args, **kwargs)

    return wrapper
