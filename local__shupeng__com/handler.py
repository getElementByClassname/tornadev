import misaka as m
from base.handler import _base


class base(_base):
  pass


class index(base):
  def get(self):
    with open('readme.md') as f:
      markdown = f.read()
      self.render(content = markdown)

  def _get(self):
    with open('readme.md') as f:
      md = m.Markdown(m.HtmlRenderer())
      res = ''.join('<section>%s</section>' % md.render(section)
          for section in f.read().split('\n\n\n'))
      self.render(content = res)


router = [
  (r"/", index),
]
