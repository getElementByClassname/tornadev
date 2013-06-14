import misaka as m
from base.handler import _base


class base(_base):
  pass


class index(base):
  def get(self):
    with open('readme.md') as f:
      md = m.Markdown(m.HtmlRenderer(), extensions=m.EXT_FENCED_CODE)
      markdown = md.render(f.read())
      self.render(content = markdown)


router = [
  (r"/", index),
]
