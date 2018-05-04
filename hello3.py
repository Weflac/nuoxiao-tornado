# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

import json
from tornado.options import options, define

define("port",default=1000, type=int, help="run server on the port.")
define("hello", default=["zhangsan","lisi"], type=str, help="hello string")

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def initialize(self):
        print("调用了initialize()")

    def prepare(self):
        print("调用了prepare()")

    def set_default_headers(self):
        print ("调用了set_default_headers()")
        # 设置get与post方式的默认响应体格式为json
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # 设置一个名为itcast、值为python的header
        self.set_header("itcast", "python")

    def write_error(self, status_code, **kwargs):
        print("调用了write_error()")

    def get(self):
        print("执行了get()")
        stu = { "name":"zhangsan", "age": 24,"gender":1 }
        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.set_header("itcast", "i love python")  # 注意此处重写了header中的itcast字段

    def post(self):
        print("执行了post()")
        stu = {
            "name": "zhangsan",
            "age": 24,
            "gender": 1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.send_error(200)  # 注意此出抛出了错误

    def on_finish(self):
        print("调用了on_finish()")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ], debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()