# coding:utf-8

import logging
import constants
import tornado.web

from handlers.BaseHandler import BaseHandler
from utils.response_code import RET
from utils.commons import required_login


class IndexHandler(BaseHandler):
    def get(self):
        try:
            garden_result = self.application.db.query(
                "select id, name, introduce, cover_url,  dateTime, author_id from blogs_garden ")
        except Exception as e:
            return self.write("error garden_result", e)
        if not garden_result:
            return self.write("error garden_result not data")

        gardens = []
        for g in garden_result:
            garden = {
                "id": g["id"],
                "name": g["name"],
                "introduce": g["introduce"],
                "cover_url": g["cover_url"],
                "dateTime": g["dateTime"],
                "author_id": g["author_id"]
            }
            gardens.append(garden)

        try:
            blog_result = self.application.db.query(
                "select id,title,subtitle,introduction,imgurl,dateTime,links,`reads` from blogs_blogs")
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

        self.render("blog/garden.html", **dict(list=gardens, blogs=blogs))  # , blogs=blogs
