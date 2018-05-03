# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import options, define

define("port",default=8800, type=int, help="run server on the port.")
define("hello", default=["zhangsan","lisi"], type=str, help="hello string")

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        python_url = self.reverse_url("python_url")
        self.write('<a href="%s">hello world!</a>' % python_url)


class HelloHandler(tornado.web.RequestHandler):
    def initialize(self,subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)



if __name__ == "__main__":
    tornado.options.parse_command_line()
    print (options.hello)
    app = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/cpp', HelloHandler, {"subject":"C++"}),
        tornado.web.url(r'/subject',HelloHandler,{"subject":"python"},name="python_url")
    ], debug=True)

    # app.listen(8800)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()