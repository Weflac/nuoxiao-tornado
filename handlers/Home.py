
import logging
import constants
import tornado.web

from handlers.BaseHandler import BaseHandler

class IndexHandler(BaseHandler):

    def get(self):
        query_args = self.get_arguments("i")
        self.render("blog/index.html", **dict(primary="nuo xiao", slide="诺晓，你的精神庄园2",  product="诺晓 Product By ObjectBin"))  # , primary="nuo xiao", slide="诺晓，你的精神庄园", product="诺晓 Product By ObjectBin"


