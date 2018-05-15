# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.web import RequestHandler, StaticFileHandler
from tornado.options import options, define

import torndb
import os
import config
import redis
from urls import urls

define("port", default=8900, type= int, help="run server on the given port.")

class IndexHandler(RequestHandler):
    '''nuoxiao首页'''
    def get(self, *args, **kwargs):
        query_args = self.get_arguments("i")
        self.render("blog/index.html", **dict(primary="nuo xiao", slide="诺晓，你的精神庄园2", product="诺晓 Product By ObjectBin")) # , primary="nuo xiao", slide="诺晓，你的精神庄园", product="诺晓 Product By ObjectBin"

class GardenHandler(RequestHandler):
    '''园子'''
    def get(self):
        try:
            garden_result = self.application.db.query("select id, name, introduce, cover_url,  dateTime, author_id from blogs_garden ")
        except Exception as e:
            return self.write("error garden_result",e)
        if not garden_result:
            return self.write("error garden_result not data")

        gardens = []
        for g in garden_result:
            garden ={
                "id": g["id"],
                "name": g["name"],
                "introduce": g["introduce"],
                "cover_url": g["cover_url"],
                "dateTime": g["dateTime"],
                "author_id": g["author_id"]
            }
            gardens.append(garden)


        try:
             blog_result = self.application.db.query("select id,title,subtitle,introduction,imgurl,dateTime,links,`reads` from blogs_blogs")
        except Exception as e:
            return self.write("error blog_result", e)
        if not garden_result:
            return self.write("error blog_result not data")

        blogs = []
        for b in blog_result:
            blog = {
                "id": b["id"],
                "title": b["title"],
                "subtitle": b["subtitle"],
                "introduction": b["introduction"],
                "imgurl": b["imgurl"],
                "datetime": b["dateTime"],
                "links": b["links"],
                "reads": b["reads"]
            }
            blogs.append(blog)

        self.render("blog/garden.html",**dict(list=gardens, blogs=blogs)) #, blogs=blogs


class Appcation(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        # handlers = [
        #     (r"/", IndexHandler),
        #     (r"/blog", IndexHandler),
        #     (r"/login", IndexHandler),
        #     (r"/blog/garden", GardenHandler),
        #     (r"/(.*)", StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "templates"), "default_filename": "index.html"}),
        # ]
        #
        # settings = dict(
        #     static_path=os.path.join(os.path.dirname(__file__), "statics"), # /static/css/main.css
        #     template_path=os.path.join(os.path.dirname(__file__), "templates"),
        #     cookie_secret="FhLXI+BRRomtuaG47hoXEg3JCdi0BUi8vrpWmoxaoyI==",
        #     xsrf_cookies=True,
        #     # login_url="/login",
        #     debug=True,
        # )

        super(Appcation, self).__init__( *args, **kwargs) # handlers, **settings
        # 创建全局数据库连接实例
        # self.db = torndb.Connection(
        #     host="127.0.0.1",
        #     database="nuoxiao",
        #     user="root",
        #     password="123456"
        # )
        self.db = torndb.Connection(**config.mysql_options)
        self.redis = redis.StrictRedis(**config.redis_options)


def main():
    tornado.options.parse_command_line()
    app = Appcation(urls, **config.settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()