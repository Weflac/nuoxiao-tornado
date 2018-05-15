# coding:utf-8
import os
from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler
from handlers import Passport, VerifyCode, Profile, Home, Garden

urls = [
    # (r"/register", Passport.RegisterHandler),
    # (r"/login", Passport.LoginHandler),
    # (r"/logout", Passport.LogoutHandler),
    # (r"/check_login", Passport.CheckLoginHandler),  # 判断用户是否登录
    # (r"/piccode", VerifyCode.PicCodeHandler),
    # # (r"/smscode", VerifyCode.SMSCodeHandler),
    # (r"/profile/avatar", Profile.AvatarHandler),  # 用户上传头像
    # (r"/profile", Profile.ProfileHandler),  # 个人主页获取个人信息
    # (r"/profile/name", Profile.NameHandler),  # 个人主页修改用户名
    # (r"/profile/auth", Profile.AuthHandler),  # 实名认证
    #
    # (r"/blog/index", Home.IndexHandler),  # 首页
    # (r'^/garden/index$', Garden.IndexHandler),  # 园子首页
    (r"/", Home.IndexHandler),
    (r"/blog", Home.IndexHandler),
    (r"/login", Home.IndexHandler),
    (r"/blog/garden", Garden.IndexHandler),
    # (r"/(.*)", StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "templates"), "default_filename": "index.html"}),
    (r"/(.*)", StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "templates"), default_filename="index.html"))
]