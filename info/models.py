from datetime import datetime

from info import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class WechatUrl(BaseModel, db.Model):
    """微信公众号带参数二维码"""
    __tablename__ = "wechat_url"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    course_name = db.Column(db.String(32), nullable=False, unique=True)  # 课程名称
    params = db.Column(db.String(32), unique=True, nullable=False)  # 参数
    url = db.Column(db.String(255), unique=True, nullable=False)  # 密码

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "course_name": self.course_name,
            "params": self.params,
            "url": self.url,
        }
        return resp_dict


class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "info_user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    openid = db.Column(db.String(32), unique=True, nullable=False)  # 手机号
    nickname = db.Column(db.String(32), unique=True, nullable=False)  # 密码
    headimgurl = db.Column(db.String(255), unique=True, nullable=False)  # 密码

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "openid": self.openid,
            "nickname": self.nickname,
            "headimgurl": self.headimgurl,
        }
        return resp_dict
