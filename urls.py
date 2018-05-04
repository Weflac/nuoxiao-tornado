# coding:utf-8
import os
from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler
from handlers import Passport, VerifyCode, Profile, Home, Garden

urls = [
    (r"/api/register", Passport.RegisterHandler),
    (r"/api/login", Passport.LoginHandler),
    (r"/api/logout", Passport.LogoutHandler),
    (r"/api/check_login", Passport.CheckLoginHandler),  # 判断用户是否登录
    (r"/api/piccode", VerifyCode.PicCodeHandler),
    (r"/api/smscode", VerifyCode.SMSCodeHandler),
    (r"/api/profile/avatar", Profile.AvatarHandler),  # 用户上传头像
    (r"/api/profile", Profile.ProfileHandler),  # 个人主页获取个人信息
    (r"/api/profile/name", Profile.NameHandler),  # 个人主页修改用户名
    (r"/api/profile/auth", Profile.AuthHandler),  # 实名认证

    (r"/api/blog/index", Home.IndexHandler),  # 首页
    (r'^/api/garden/index$', Garden.IndexHandler),  # 园子首页
    (r"/(.*)", StaticFileHandler,
     dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))
]