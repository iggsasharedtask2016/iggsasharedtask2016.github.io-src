#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'IGGSA'
SITENAME = u'Iggsa Shared Task 2016'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'
THEME = '/home/ruppenho/Dev/Python/pelican-themes/pelican-bootstrap3-master'
DEFAULT_LANG = u'en'

MD_EXTENSIONS = (['toc'])
# tell pelican where your custom.css file is in your content folder
STATIC_PATHS = ['extras/custom.css']



# tell pelican where it should copy that file to in your output folder
EXTRA_PATH_METADATA = {
'extras/custom.css': {'path': 'static/custom.css'}
}

# tell the pelican-bootstrap-3 theme where to find the custom.css file in your output folder
CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TYPOGRIFY = True


SUMMARY_MAX_LENGTH = None
# Blogroll
LINKS = (
	('IGGSA', 'https://sites.google.com/site/iggsahome/'),
	('STEPS 2014','https://sites.google.com/site/iggsasharedtask/task-1'),
	('Konvens2016', 'http://www.linguistics.rub.de/konvens16/'),
	('Pelican', 'http://getpelican.com/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
