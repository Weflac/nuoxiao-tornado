# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import options, define

define("port",default=9000, type=int, help="run server on the port.")
define("hello", default=["zhangsan","lisi"], type=str, help="hello string")

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def post(self):
        query_arg = self.get_query_argument("a")
        query_args = self.get_query_arguments("a")
        body_arg = self.get_body_argument("a")
        body_args = self.get_body_arguments("a",strip=False)
        arg = self.get_argument("a")
        args = self.get_arguments("a")

        default_arg = self.get_argument("b","hello")
        default_args = self.get_arguments("b")

        try:
            missing_arg = self.get_argument("c")
        except tornado.web.MissingArgumentError as e:
            missing_arg = "We catched the MissingArgumentError!"
            print (e)

        missing_args = self.get_arguments("c")

        rep = "query_arg:%s<br/>" % query_arg
        rep += "query_args:%s<br/>" % query_args
        rep += "body_arg:%s<br/>" % body_arg
        rep += "body_args:%s<br/>" % body_args
        rep += "arg:%s<br/>" % arg
        rep += "args:%s<br/>" % args
        rep += "default_arg:%s<br/>" % default_arg
        rep += "default_args:%s<br/>" % default_args
        rep += "missing_arg:%s<br/>" % missing_arg
        rep += "missing_args:%s<br/>" % missing_args

        self.write(rep)

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files
        img_files = files.get('img')
        if img_files:
            img_file = img_files[0]["body"]
            file = open("./itcast", 'w+')
            file.write(img_file)
            file.close()
        self.write("OK")

class SubjectCityHandler(tornado.web.RequestHandler):
    def get(self, subject, city):
        self.write(("Subject: %s<br/>City: %s" % (subject, city)))

class SubjectDateHandler(tornado.web.RequestHandler):
    def get(self, date, subject):
        self.write(("Date: %s<br/>Subject: %s" % (date, subject)))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    print (options.hello)
    app = tornado.web.Application([
        (r'/', IndexHandler),
        (r"/upload", UploadHandler),
        (r"/sub-city/(.+)/([a-z]+)", SubjectCityHandler),  # 无名方式
        (r"/sub-date/(?P<subject>.+)/(?P<date>\d+)", SubjectDateHandler),  # 命名方式
    ])

    # app.listen(8800)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()