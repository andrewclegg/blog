#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrew Clegg'
SITENAME = u'The Plural of Anecdote'
SITEURL = ''
RELATIVE_URLS = True

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
          ('Blog', '/'),
          ('Snake Charmer', 'https://github.com/andrewclegg/snake-charmer'),
          )

# Social widget
SOCIAL = (
          ('GitHub', 'https://github.com/andrewclegg'),
          ('Twitter', 'https://twitter.com/andrew_clegg'),
          ('LinkedIn', 'https://www.linkedin.com/in/andrewcleggdatascientist'),
          )

DEFAULT_PAGINATION = 10

DEFAULT_DATE = 'fs'
THEME = 'themes/svbhack'
USER_LOGO_URL = SITEURL + '/theme/images/logo.jpg'
TAGLINE = 'The Plural of Anecdote'
STATIC_PATHS = ['images', 'pdfs', 'favicon.ico']
TYPOGRIFY = True

FILENAME_METADATA = '(?P<slug>.*)'  # use markdown file name as the slug meta
USE_FOLDER_AS_CATEGORY = True       # use folder name as posts' category

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
DISQUS_SITE = 'thepluralofanecdote'


