#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20140121082121.6593: * @file sitebuilder.py
#@@first
#@@language python

#@+<< imports >>
#@+node:peckj.20140121082121.6637: ** << imports >>
import sys, shutil

from flask import Flask, render_template, abort, send_from_directory
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.assets import Environment
from htmlmin.minify import html_minify
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140121082121.6638: ** << declarations >>
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

BASE_URL = 'http://blog.suspended-chord.info'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
assets = Environment(app)
assets.url_expire = False
#@-<< declarations >>

#@+others
#@+node:peckj.20140121082121.6639: ** routes
#@+node:peckj.20140121082121.6641: *3* route '/'
@app.route("/")
def index():
  return html_minify(render_template('index.html', pages=pages))
#@+node:peckj.20140121082121.6642: *3* route '/tag/<string:tag>/'
@app.route('/tag/<string:tag>/')
def tag(tag):
  tagged = [p for p in pages if tag in p.meta.get('tags', [])]
  return html_minify(render_template('tag.html', pages=tagged, tag=tag))
#@+node:peckj.20140121082121.6643: *3* route '/<path:path>/'
@app.route('/<path:path>/')
def page(path):
  page = pages.get_or_404(path)
  return html_minify(render_template('page.html', page=page))
#@+node:peckj.20140123082920.4917: *3* top-level nav
#@+node:peckj.20140123082920.4911: *4* route '/about/'
@app.route("/about/")
def about():
  return html_minify(render_template('about.html'))
#@+node:peckj.20140123082920.4912: *4* route '/archives/'
@app.route("/archives/")
def archives():
  return html_minify(render_template('archives.html', pages=pages))
#@+node:peckj.20140123082920.4916: *4* route '/code-dump/'
@app.route('/code-dump/')
def codedump():
  return tag('code-dump')

#@+node:peckj.20140123082920.4921: *4* route '/csmm/'
@app.route('/csmm/')
def csmm():
  return tag('csmm')

#@+node:peckj.20140123082920.4922: *4* route '/tags/'
@app.route("/tags/")
def tags():
  tags = {}
  for page in pages:
    ts = page.meta.get('tags',None)
    if ts is not None and len(ts) > 0:
      for tag in ts:
        val = tags.get(tag, 0)
        val += 1
        tags[tag] = val
  return html_minify(render_template('tags.html', tags=tags))
#@+node:peckj.20140123082920.4919: *3* etc
#@+node:peckj.20140121082121.6645: *4* route '/404.html'
@app.route('/404.html')
def error():
  return html_minify(render_template('error.html', error=404))

@freezer.register_generator
def error_generator():
  return ['/404.html']
#@+node:peckj.20140121082121.6646: *4* route '/favicon.ico'
@app.route('/favicon.ico')
def favicon():
  return  send_from_directory(app.static_folder, 'assets/img/favicon.ico')
#@+node:peckj.20140121082121.6647: *4* route '/robots.txt'
@app.route('/robots.txt')
def favicon():
  return  send_from_directory(app.static_folder, 'assets/robots.txt')
#@-others

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
    shutil.rmtree('build/static/.webassets-cache')
  else:
    app.run(port=3000)

#@-leo
