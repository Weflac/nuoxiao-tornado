# coding:utf-8

import logging
import constants

from handlers.BaseHandler import BaseHandler
from utils.response_code import RET
from utils.commons import required_login

class IndexHandler(BaseHandler):

    def get(self):
        return self.render("blog/garden.html")

