# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

import os
import torndb
from tornado.options import options, define
from tornado.web import RequestHandler
from handlers.BaseHandler import BaseHandler

define("port", default=2000, type=int, help="run server on the port.")
define("hello", default=["zhangsan", "lisi"], type=str, help="hello string")


class IndexHandler(RequestHandler):
    """主路由处理类"""
    def get(self):
        self.write('<a href="/get">hello world!</a>')


class InsertHandler(RequestHandler):
    def post(self):
        title = self.get_argument("title")
        position = self.get_argument("position")
        price = self.get_argument("price")
        score = self.get_argument("score")
        comments = self.get_argument("comments")
        try:
            ret = self.application.db.execute(
                "insert into houses(title, position, price, score, comments) values(%s, %s, %s, %s, %s)", title,
                position, price, score, comments)
        except Exception as e:
            self.write("DB error:%s" % e)
        else:
            self.write("OK %d" % ret)


class GetHandler(RequestHandler):
    def get(self):
        """访问方式为http://127.0.0.1/get?id=111"""
        hid = self.get_argument("id")
        try:
            ret = self.application.db.get("select title,position,price,score,comments from houses where id=%s", hid)
        except Exception as e:
            self.write("DB error:%s" % e)
        else:
            print(type(ret))
            print(ret)
            print(ret.title)
            print(ret['title'])
            # self.render("index.html", houses=[ret])


class QueryHandler(RequestHandler):
    def get(self):
        """访问方式为http://127.0.0.1/query"""
        try:
            ret = self.application.db.query("select title,position,price,score,comments from houses limit 10")
        except Exception as e:
            self.write("DB error:%s" % e)
        else:
            self.render("index.html", houses=ret)


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        handlers = [
            (r"/", IndexHandler),
            (r"/insert", InsertHandler),
            (r"/get", GetHandler),
            (r"/query", QueryHandler),
        ]
        settings = dict(
                template_path=os.path.join(os.path.dirname(__file__), "templates"),
                static_path=os.path.join(os.path.dirname(__file__), "statics"),
                debug=True,
        )
        super(Application, self).__init__(handlers, *args, **kwargs)
        # 创建一个全局mysql连接实例供handler使用
        self.db = torndb.Connection(
                host="127.0.0.1",
                database="nuoxiao",
                user="root",
                password="123456"
        )

if __name__ == "__main__":
    tornado.options.parse_command_line()
    # app = tornado.web.Application([
    #     (r'/', Application),
    # ], debug=True)
    app = Application()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()
