#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20140121082121.6593: * @file sitebuilder.py
#@@first
#@@language python

#@+<< imports >>
#@+node:peckj.20140121082121.6637: ** << imports >>
import sys, shutil, os
from datetime import datetime, date

from flask import Flask, render_template, abort, send_from_directory
from flask_flatpages import FlatPages
from flask_frozen import Freezer
#from flask.ext.assets import Environment
from flask_assets import Environment
#from htmlmin.minify import html_minify

#from urlparse import urljoin
from flask import request
#from werkzeug.contrib.atom import AtomFeed

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

jinja2_env = app.jinja_env
#@-<< declarations >>

#@+others
#@+node:peckj.20140131081341.3987: ** jinja2 filters
#@+node:peckj.20140131081341.3988: *3* dateformat
def dateformat(d):
  return d.strftime('%B %d, %Y').replace(' 0', ' ')

jinja2_env.filters['dateformat'] = dateformat
#@+node:peckj.20140127083227.10220: ** helpers
#@+node:peckj.20140127083227.10221: *3* get_pages_by_date
def get_pages_by_date(year=None, month=None, day=None):
  out = []
  for p in pages:
    if p.meta.get('date', None) is not None:
      d = get_date(p)
      d_year = (year is None or d.year == year)
      d_month = (month is None or d.month == month)
      d_day = (day is None or d.day == day)
      if d_year and d_month and d_day:
        out.append(p)
  # sort ascending
  out.sort(key=lambda x: get_date(x))
  return out
#@+node:peckj.20140127083227.10223: *3* get_date
def get_date(page):
  page_date = page.meta['date']
  return page_date
#@+node:peckj.20150324130423.1: *3* make_external_url
def make_external_url(url):
  return urljoin(BASE_URL, url)
#@+node:peckj.20140121082121.6639: ** routes
#@+node:peckj.20140121082121.6641: *3* route '/'
@app.route("/")
def index():
  p = list(pages)
  p.sort(key=lambda x: get_date(x), reverse=True)
  new=p[:10]
  old=p[10:]
  return render_template('index.html', newpages=new, oldpages=old)
#@+node:peckj.20140121082121.6642: *3* route '/tag/<string:tag>/'
@app.route('/tag/<string:tag>/')
def tag(tag):
  tagged = [p for p in pages if tag in p.meta.get('tags', [])]
  tagged.sort(key=lambda x: get_date(x))
  return render_template('tag.html', pages=tagged, tag=tag)
#@+node:peckj.20140121082121.6643: *3* route '/<path:path>/'
@app.route('/<path:path>/')
def page(path):
  page = pages.get_or_404(path)
  return render_template('page.html', page=page)
#@+node:peckj.20150422092749.1: *4* page_generator
@freezer.register_generator
def page_generator():
  pagelist = []
  for root, dir, files in os.walk('pages'):
    for file in files:
      pagelist.append(('page', {'path' : "/".join((root[6:].replace('\\','/'),file[:-3])) }))
  return pagelist

#@+node:peckj.20140127083227.10219: *3* route '/<int:year>/'
@app.route('/<int:year>/index.html')
def year(year):
  title = '%04d' % year
  year_pages = get_pages_by_date(year=year)
  return render_template('archives.html', pages=year_pages, title=title)

#@+node:peckj.20150422092803.1: *4* year_generator
@freezer.register_generator
def year_generator():
  years = []
  for p in pages:
    d = get_date(p)
    y = '/%04d/index.html' % d.year
    if y not in years:
      years.append(y)
  return years
#@+node:peckj.20140127083227.10225: *3* route '/<int:year>/<int:month>/'
@app.route('/<int:year>/<int:month>/index.html')
def month(year, month):
  month_pages = get_pages_by_date(year=year, month=month)
  title = '%04d/%02d' % (year, month)
  return render_template('archives.html', pages=month_pages, title=title)

#@+node:peckj.20150422092827.1: *4* month_generator
@freezer.register_generator
def month_generator():
  months = []
  for p in pages:
    d = get_date(p)
    m = '/%04d/%02d/index.html' % (d.year, d.month)
    if m not in months:
      months.append(m)
  return months
#@+node:peckj.20140127083227.10227: *3* route '/<int:year>/<int:month>/<int:day>/'
@app.route('/<int:year>/<int:month>/<int:day>/index.html')
def day(year, month, day):
  day_pages = get_pages_by_date(year=year, month=month, day=day)
  title = '%04d/%02d/%02d' % (year, month, day)
  return render_template('archives.html', pages=day_pages, title=title)

#@+node:peckj.20150422092838.1: *4* day_generator
@freezer.register_generator
def day_generator():
  days = []
  for p in pages:
    d = get_date(p)
    day = '/%04d/%02d/%02d/index.html' % (d.year, d.month, d.day)
    if day not in days:
      days.append(day)
  return days
#@+node:peckj.20140123082920.4917: *3* top-level nav
#@+node:peckj.20140123082920.4911: *4* route '/about/'
@app.route("/about/")
def about():
  return render_template('about.html')
#@+node:peckj.20140123082920.4912: *4* route '/archives/'
@app.route("/archives/")
def archives():
  p = list(pages)
  p.sort(key=lambda x: get_date(x))
  return render_template('archives.html', pages=p, title='archives')
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
  return render_template('tags.html', tags=tags)
#@+node:peckj.20140123082920.4919: *3* etc
#@+node:peckj.20140121082121.6645: *4* route '/404.html'
@app.route('/404.html')
def error():
  return render_template('error.html', error=404)

@freezer.register_generator
def error_generator():
  return ['/404.html']
#@+node:peckj.20140121082121.6646: *4* route '/favicon.ico'
@app.route('/favicon.ico')
def favicon():
  return  send_from_directory(app.static_folder, 'assets/img/favicon.ico')
#@+node:peckj.20140121082121.6647: *4* route '/robots.txt'
@app.route('/robots.txt')
def robots():
  return  send_from_directory(app.static_folder, 'assets/robots.txt')
#@-others

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
    shutil.rmtree('build/static/.webassets-cache')
  else:
    app.run(port=3000)

#@-leo
