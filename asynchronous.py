# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.web import RequestHandler, StaticFileHandler
from tornado.options import options, define
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import coroutine

import torndb
import os
import json

define("port", default=8989, type=int, help="run server on the given port.")



class IndexHandler(RequestHandler):

    # @tornado.web.asynchronous
    # def get(self, *args, **kwargs):
    #    client =  AsyncHTTPClient()
    #    client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.130.112.24",callback = self.on_response)
    #
    # def on_response(self, response):
    #     data = json.loads(response.body)
    #
    #     if 1 == data["ret"]:
    #         self.write(u"国家：%s 省份: %s 城市: %s" % (data["country"], data["province"], data["city"]))
    #     else:
    #         self.write("查询IP信息错误")
    #
    #     self.finish()  # 发送响应信息，结束请求处理

    # # 协程异步
    # @tornado.gen.coroutine
    # def get(self):
    #     # client = AsyncHTTPClient()
    #     # response = yield client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.130.112.24")
    #     #
    #     # if(response.error):
    #     #     self.send_error(500)
    #     # else:
    #     #     data = json.loads(response.body)
    #         data = yield  self.get_ip_info("14.130.112.24")
    #         if 1 == data["ret"]:
    #             self.write(u"国家：%s 省份: %s 城市: %s" % (data["country"], data["province"], data["city"]))
    #         else:
    #             self.write("查询IP信息错误")
    #
    # @tornado.gen.coroutine
    # def get_ip_info(self, ip):
    #     client = AsyncHTTPClient()
    #     response = yield client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip="+ip)
    #     if response.error:
    #         rep = {"ret: 0"}
    #     else:
    #         rep = json.loads(response.body)
    #
    #     raise tornado.gen.Return(rep)  # 此处需要注意


    # 并行协程
    @tornado.gen.coroutine
    def get(self):
        ips = ["14.130.112.24",
               "15.130.112.24",
               "16.130.112.24",
               "17.130.112.24"]
        rep1, rep2 = yield [self.get_ip_info(ips[0]), self.get_ip_info(ips[1])]
        rep34_dict = yield dict(rep3=self.get_ip_info(ips[2]), rep4=self.get_ip_info(ips[3]))
        self.write_response(ips[0], rep1)
        self.write_response(ips[1], rep2)
        self.write_response(ips[2], rep34_dict['rep3'])
        self.write_response(ips[3], rep34_dict['rep4'])

    def write_response(self, ip, response):
        self.write(ip)
        self.write(":<br/>")
        if 1 == response["ret"]:
            self.write(u"国家：%s 省份: %s 城市: %s<br/>" % (response["country"], response["province"], response["city"]))
        else:
            self.write("查询IP信息错误<br/>")

    @tornado.gen.coroutine
    def get_ip_info(self, ip):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=" + ip)
        if response.error:
            rep = {"ret:1"}
        else:
            rep = json.loads(response.body)
        raise tornado.gen.Return(rep)

class Appcation(tornado.web.Application):
    def __init__(self):
        current_path = os.path.dirname(__file__)

        handlers = [
            (r"/", IndexHandler),
            (r"/blog", IndexHandler),
            (r"/(.*)", StaticFileHandler, {"path": os.path.join(current_path, "templates"), "default_filename": "index.html"}),
        ]

        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "statics"), # /static/css/main.css
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            cookie_sercet="FhLXI+BRRomtuaG47hoXEg3JCdi0BUi8vrpWmoxaoyI==",
            xsrf_cookies=True,
            login_url="/login",
            debug=True,
        )

        super(Appcation, self).__init__(handlers, **settings)
        # 创建全局数据库连接实例
        self.db = torndb.Connection(
            host="127.0.0.1",
            database="nuoxiao",
            user="root",
            password="123456"
        )


def main():
    tornado.options.parse_command_line()
    app = Appcation()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()