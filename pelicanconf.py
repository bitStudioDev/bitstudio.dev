#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# https://github.com/getpelican/pelican/blob/master/docs/settings.rst


# GENERAL
SITENAME = 'bitStudio.dev'
DOMAIN = 'bitstudio.dev'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = 'en'
STATIC_PATHS = ['blog', 'pages', 'extra', 'images']
DELETE_OUTPUT_DIRECTORY = True

# TIME AND DATES
DEFAULT_DATE_FORMAT = '%d %B %Y'


# SEO
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }


# ARTICLE
ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = ['extra']
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_ORDER_BY = 'reversed-date'
ARTICLE_EDIT_URL = 'https://github.com/bitStudioDev/bitstudio.dev/tree/master/content/'
ARTICLE_SUGGEST_CHANGES_URL = 'https://github.com/bitStudioDev/bitstudio.dev/issues/'


# ARCHIVES
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
ARCHIVES_SAVE_AS = 'articles/index.html'
ARCHIVES_URL = 'articles'

# AUTHORS
AUTHORS_SAVE_AS = 'authors/index.html'
AUTHOR_URL = 'author/{slug}'

# AUTHOR
AUTHOR = 'Wojciech'  # Default author
AUTHOR_MAIL = 'wojciech'
AUTHOR_MAILTO = 'wojciech@bitstudio.dev'
AUTHOR_DISCORD = 'DECS7TA'
AUTHOR_TELEGRAM = 'https://t.me/joinchat/AAAAAEyR3QNxxzZtvwUcYg'
AUTHOR_TWITTER = 'VV0JC13CH'
AUTHOR_GITHUB = 'VV0JC13CH'
AUTHOR_LINKED = 'VV0JC13CH'
AUTHOR_KO_FI = 'VV0JC13CH'
AUTHOR_BIO = 'This is my personal site. I write about the things I learn and projects I develop. ' \
             'As a language I use mainly python, sometimes its lua, c# or Go. ' \
             'Enjoy my content.'

AUTHOR_SOCIAL = (('Mail', 'mailto:' + AUTHOR_MAILTO, AUTHOR_MAIL, 'fa fa-at'),
                 ('Github', 'https://github.com/' + AUTHOR_GITHUB, AUTHOR_GITHUB, 'fab fa-github'),
                 ('Twitter', 'https://twitter.com/' + AUTHOR_TWITTER, '@' + AUTHOR_TWITTER, 'fab fa-twitter'),
                 ('Ko-Fi', 'https://ko-fi.com/' + AUTHOR_KO_FI, AUTHOR_KO_FI, 'fa fa-coffee'),
                 ('LinkedIn', 'https://www.linkedin.com/in/' + AUTHOR_LINKED, AUTHOR_LINKED, 'fab fa-linkedin'),)

# CATEGORIES
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'


# DRAFTS
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
DRAFT_PAGE_URL = 'drafts/{slug}/'
DRAFT_PAGE_SAVE_AS = 'drafts/{slug}/index.html'
WITH_FUTURE_DATES = False

# INDEX
SUMMARY_MAX_LENGTH = None

# PAGES
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = ['extra']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# TAGS
TAG_URL = '{slug}/'
TAG_SAVE_AS = '{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# PAGINATION
DEFAULT_PAGINATION = 7
DEFAULT_ORPHANS = 0
PAGINATION_PATTERNS = (
    (1, '{name}{extension}', '{name}{extension}'),
    (2, 'latest-{number}/', 'latest-{number}/index.html'),
)
PAGINATED_TEMPLATES = {'period_archives': None}


# THEME VARIABLES
THEME = 'themes/bitstudiodev'
THEME_STATIC_PATHS = ['static']
THEME_STATIC_DIR = 'theme'
TEMPLATE_EXTENSIONS = ['.html']
CSS_FILE = 'main.css'
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives']


# MENU LINKS
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Header link on the right:
LINKS_HEADER = (('Articles', ARCHIVES_URL, 'articles/index.html'),
                )

# Footer links on the left:
LINKS_FOOTER = (('Ko-Fi', 'https://ko-fi.com/' + AUTHOR_KO_FI),)

# Social widget
SOCIAL_MAIL = 'office'
SOCIAL_MAILTO = 'office@bitstudio.dev'
SOCIAL_DISCORD = AUTHOR_DISCORD
SOCIAL_YOUTUBE = 'UCmRtyJbc6MsZS86-ZZXV2JA'
SOCIAL_TWITTER = 'bitstudiodev'
SOCIAL_GITHUB = 'bitStudioDev'

SOCIAL = (('Mail', 'mailto:' + SOCIAL_MAILTO, SOCIAL_MAIL, 'fa fa-at'),
          ('Github', 'https://github.com/' + SOCIAL_GITHUB, SOCIAL_GITHUB, 'fab fa-github'),
          ('YouTube', 'https://www.youtube.com/channel/' + SOCIAL_YOUTUBE, SITENAME, 'fab fa-youtube'),
          ('Discord', 'http://discord.gg/' + SOCIAL_DISCORD, SITENAME, 'fab fa-discord'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
