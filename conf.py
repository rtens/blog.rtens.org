from __future__ import unicode_literals

AUTHOR = 'Nikolas Martens'
SITENAME = "Blog@rtens.org"
TIMEZONE = "Europe/Berlin"
TWITTER_USERNAME = 'rtens_'
GOOGLE_ANALYTICS = 'UA-40634631-1'

GITHUB_BLOG_URL = "https://github.com/rtens/blog.rtens.org"

SOCIAL = (('twitter', 'https://twitter.com/rtens_'),
          ('github', 'https://github.com/rtens'),
          ('deviantart', 'https://nikolasalokin.deviantart.com'),
          ('linkedin', 'https://www.linkedin.com/in/nikolas-martens-803bb0112/'),
          ('web', 'https://rtens.org'),
		  ('email', 'mailto:blog@rtens.org'))

SITEURL = 'https://blog.rtens.org'
ROOT_URL = SITEURL
FEED_RSS = 'feeds/rss.xml'

REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 5

# static paths will be copied under the same name
STATIC_PATHS = ["img", "res"]

FILENAME_METADATA  = '(?P<date>\d{4}-\d{2}-\d{2}) (?P<title>.*)'
ARTICLE_DIR = ('articles/')
THEME = 'themes/tuxlite_tbs'

DELETE_OUTPUT_DIRECTORY = True