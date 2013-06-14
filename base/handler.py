import os
import sys
import json
import datetime
import traceback
from bson.objectid import ObjectId
#import random
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import tornado.web
from tornado.options import options


class _base(tornado.web.RequestHandler):
  def initialize(self, **kwargs):
    if not hasattr(self, 'package'):
      self.package = self.__module__.split('.')[0]
    self.db = self.application._db[self.package]

  def set_default_headers(self):
    if options.debug:
      self.set_header("Access-Control-Allow-Origin", "*")
      self.set_header('Access-Control-Allow-Methods', 'GET, PUT, OPTIONS')

  def get_error_html(self, status_code, **kwargs):
    kwargs['exc_info'] = sys.exc_info()
    error_code_orig = ''.join(traceback.format_exception(*kwargs["exc_info"]))
    formatter = HtmlFormatter(linenos=True, cssclass="codehilite")
    kwargs['error'] = highlight(error_code_orig, PythonLexer(), formatter)
    return self.render_string("base/tpl/error.html", **kwargs)

  def render(self, template_name='', **kwargs):
    tpl_name = '%s/tpl/%s.html' % (self.package, self.__class__.__name__)
    return super(_base, self).render(tpl_name, **kwargs)

  def static_url(self, path, include_host=None):
    self.settings['static_path'] = os.path.join(self.package, 'static')
    return '/static/%s' % super(_base, self).static_url(path, include_host)

  def static_dev(self, path):
    domain = '127.0.0.1' if options.debug else '71.19.147.84'
    return '//%s:%d/static/%s' % (domain, options.port, path)

  def redirect_by_referer(self):
    redirect = self.request.headers.get('Referer', '/')
    self.redirect(redirect)

  def jsondumps(self, data):
    def type_handler(obj):
      if isinstance(obj, datetime.datetime):
        return obj.isoformat()
      elif isinstance(obj, ObjectId):
        return str(obj)
      else:
        return None
    #self.write(json.dumps(data, default=type_handler))
    #self.finish()
    return json.dumps(data, default=type_handler)

  def set_global(self, obj={}):
    return obj


class not_found2(_base):
  def get(self, uri=''):
    self.write(uri + ' File Not Found with ' + str(self.request))


class static(tornado.web.StaticFileHandler):
  # allow javascript cross domain for dev
  def set_extra_headers(self, path):
    self.set_header('Access-Control-Allow-Origin', '*')
