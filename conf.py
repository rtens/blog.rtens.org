from __future__ import unicode_literals

AUTHOR = 'Nikolas Martens'
SITENAME = "Nikolas.M@rtens"
SITEURL = 'http://rtens.cygnus.uberspace.de/blog'
TIMEZONE = "Europe/Berlin"

REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 5

SOCIAL = (('twitter', 'http://twitter.com/rtens_'),
          ('github', 'http://github.com/rtens'),)

# static paths will be copied under the same name
STATIC_PATHS = ["img"]

FILENAME_METADATA  = '(?P<date>\d{4}-\d{2}-\d{2}) (?P<title>.*)'
ARTICLE_DIR = ('articles/')
THEME = 'themes/waterspill-en'

DELETE_OUTPUT_DIRECTORY = True