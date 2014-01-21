import sys, shutil

from flask import Flask, render_template, abort
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.assets import Environment
from htmlmin.minify import html_minify

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

BASE_URL = 'http://www.example.com'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
assets = Environment(app)
assets.url_expire = False

@app.route("/")
def index():
  return html_minify(render_template('index.html', pages=pages))

@app.route('/tag/<string:tag>/')
def tag(tag):
  tagged = [p for p in pages if tag in p.meta.get('tags', [])]
  return html_minify(render_template('tag.html', pages=tagged, tag=tag))

@app.route('/<path:path>/')
def page(path):
  page = pages.get_or_404(path)
  return html_minify(render_template('page.html', page=page))

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
    shutil.rmtree('build/static/.webassets-cache')
  else:
    app.run(port=8000)

