
import logging
import constants

from handlers.BaseHandler import BaseHandler

class IndexHandler(BaseHandler):

    def get(self):
        return self.render("index.html")

