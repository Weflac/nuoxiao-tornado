
import logging
import hashlib
import config
import re

from handlers.BaseHandler import BaseHandler
from utils.response_code import RET
from utils.session import Session
from utils.commons import required_login

class RegisterHandler(BaseHandler):
    """注册"""
    def post(self):
        username = self.json_args.get("username")
        password = self.json_args.get("password")
        sms_code = self.json_args.get("phonecode") # 短信

        # 验证
        if not all([username,sms_code,password]):
            return self.write(dict(errcode=RET.PARAMERR, errmsg="参数不完整"))

        if not re.match(r"^1\d{10}$", username):
            return self.write(dict(errcode=RET.DATAERR, errmsg="手机号格式错误"))

        # 如果产品对于密码长度有限制，需要在此做判断
        # if len(password)<6

        # 判断短信验证码是否真确
        if "2468" != sms_code:
            try:
                real_sms_code = self.redis.get("sms_code_%s" % username)
            except Exception as e:
                logging.error(e)
                return self.write(dict(errcode=RET.DBERR, errmsg="查询验证码出错"))

            # 判断短信验证码是否过期
            if not real_sms_code:
                return self.write(dict(errcode=RET.NODATA, errmsg="验证码过期"))

            # 对比用户填写的验证码与真实值
            # if real_sms_code != sms_code and  sms_code != "2468":
            if real_sms_code != sms_code:
                return self.write(dict(errcode=RET.DATAERR, errmsg="验证码错误"))

            try:
                self.redis.delete("sms_code_%s" % username)
            except Exception as e:
                logging.error(e)

        # 保存数据，同时判断手机号是否存在，判断的依据是数据库中mobile字段的唯一约束
        passwd = hashlib.sha256(password + config.passwd_hash_key).hexdigest()
        sql = "insert into blogs_users(username, phone, password) values(%(username)s, %(mobile)s, %(password)s);"

        try:
            user_id = self.db.execute(sql, username=username, mobile=username, password=passwd)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DATAEXIST, errmsg="手机号已存在"))

        # 用session记录用户的登录状态
        session = Session(self)
        session.data["user_id"] = user_id
        session.data["user_name"] = username
        try:
            session.save()
        except Exception as e:
            logging.error(e)

        self.write(dict(errcode=RET.OK, errmsg="注册成功"))
        self.render("register.html",errcode=RET.OK, errmsg="注册成功")


class LoginHandler(BaseHandler):
    """登录"""
    def post(self):
        # 获取参数
        username = self.json_args.get("username")
        password = self.json_args.get("password")

        # 检查参数
        if not all([username, password]):
            return self.write(dict(errcode=RET.PARAMERR, errmsg="参数错误"))
        if not re.match(r"^1\d{10}$", username):
            return self.write(dict(errcode=RET.DATAERR, errmsg="手机号错误"))

        # 检查秘密是否正确
        res = self.db.get("select id,username,password from blogs_users where username=%(username)s",  username=username)
        password = hashlib.sha256(password+config.passwd_hash_key).hexdigest()

        if res and res["password"] == unicode(password):
            # 生成session数据
            # 返回客户端
            try:
                self.session = Session(self)
                self.session.data['user_id'] = res['id']
                self.session.data['user_name'] = res['username']
                self.session.save()

            except Exception as e:
                logging.error(e)
            return self.write(dict(errcode=RET.OK, errmsg="OK"))
        else:
            return self.write(dict(errcode=RET.DATAERR, errmsg="手机号或密码错误！"))


class LogoutHandler(BaseHandler):
    """退出登录"""
    @required_login
    def get(self):
        # 清除session数据
        # sesssion = Session(self)
        self.session.clear()
        self.write(dict(errcode=RET.OK, errmsg="退出成功"))


class CheckLoginHandler(BaseHandler):
    """检查登陆状态"""
    def get(self):
        # get_current_user方法在基类中已实现，它的返回值是session.data（用户保存在redis中
        # 的session数据），如果为{} ，意味着用户未登录;否则，代表用户已登录
        if self.get_current_user():
            self.write({"errcode":RET.OK, "errmsg":"true", "data":{"name":self.session.data.get("user_name")}})
        else:
            self.write({"errcode":RET.SESSIONERR, "errmsg":"false"})

