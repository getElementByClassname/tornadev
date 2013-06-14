#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import logging
import pymongo
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, parse_config_file, parse_command_line

import base.handler
from base.static import StaticComboHandler
#print(dir(StaticComboHandler))

parse_config_file(os.path.join(os.path.dirname(__file__), "setting.py"))
parse_command_line()


class Application(tornado.web.Application):
  def __init__(self):
    _file = os.path.dirname(__file__)
    settings = {
      #"static_path": os.path.join(os.path.dirname(__file__), './static'),
      "template_path": os.path.join(_file, './'),
      "static_url_prefix": '',
      "static_handler_class": StaticComboHandler,
      # python -c 'import uuid,base64\
      # base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)'
      "cookie_secret": 'tPD0/OoZS/25XrC0x12pAjbNet+gBk3bmnUTLgmwZYM=',
      "xsrf_cookies": True,
      #"autoescape": None,
      "debug": options.debug,
    }
    tornado.web.Application.__init__(self, **settings)

    self._db = pymongo.Connection()
    self.add_handlers_by_domain()

    def_router = [
      (r"/static/(.*)", base.handler.static,
        {'path': os.path.join(os.path.dirname(__file__), 'base', "static")}),
    ]
    if options.debug:
      from base.lib.reload import static_watcher, ReloadHandler
      def_router.append((r"/debug", ReloadHandler))
      static_watcher()
    self.add_handlers(r'.*', def_router)

  def add_handlers_by_domain(self):
    for dir in os.listdir():
      # the domain dirname use '__' instead '.' for package
      # a.com -> a__com or www.a.com -> www___a__com
      if os.path.isdir(os.path.dirname(__file__) + dir) and '__' in dir:
        module = __import__(dir, fromlist = ["handler"])
        domain = dir.replace('__', '.')

        # serve static_path, favico, robots
        # https://github.com/facebook/tornado/blob/master/tornado/web.py#L1313
        static_pattern = [(pattern, tornado.web.StaticFileHandler,
            {'path': os.path.join(os.path.dirname(__file__), dir, "static")})
        for pattern in [r"/static/(.*)", r"/(favicon\.ico)", r"/(robots\.txt)"]]
        router = static_pattern + module.handler.router

        if options.debug:
          domain = re.sub(r'\.(\w+)$', '.dev', domain)
          logging.info('http://%s:%s' % (domain, options.port))

        self.add_handlers(domain, router)

if __name__ == "__main__":
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()
