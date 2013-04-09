Tags: git, bash, python
Summary: How I set this blog up with pelican and git-push-deployment

So yeah I decided to start a blog again since it's been a while. The last one was actually about [my time living in Valencia][vlc]. This one is probably gonna be mostly about software engineering stuff. This first post is gonna be about how I set this blog. I know there are at least ten gillion articles about this but then now it's ten gillion and one.

[vlc]: http://off-to-vlc.blogspot.de/

## Step 1: engine

My colleague showed [pelican] to me yesterday which is a static blog generator written in [python]. It means that I can put my files and articles in whatever directory structure I fancy and the website will be generated as static files during deployment. The articles are written in a simple mark-up language (I use [markdown]) and annotated with meta-information. This has some nice advantages:

1. I can use whatever editor I want to write articles (which is especially nice on the phone)
1. No internet access required (I sync across devices with [Dropbox])
1. Including custom static pages comes naturally
1. I just like having my stuff in my machine instead some database somewhere in the interwebs

## Step 2: installation

I recently switched my web hosting to [uberspace] which is offers a awesome service a quite unique business model. You pay as much as you want, minimum 1€ per "space". This makes it possible to have many accounts, which is perfect when having a bunch of independent projects as in my case. Uberspace also provides more languages and databases that I could think of including python which I haven't even had on my previous hoster. This made installing and running pelican easy:
	
	:::bash
	[remote]$ easy_install pelican markdown
	[remote]$ pelican

This generates an empty blog in an `output` directory.

## Step 3: configuration

Pelican works pretty well [out-of-the-box] but some configuration is eventually necessary. Here is my `config.py` with some comments.

	:::python
	from __future__ import unicode_literals

	# Information about myself
	AUTHOR = 'Nikolas Martens'
	SITENAME = "Nikolas.M@rtens"
	SITEURL = 'http://blog.rtens.org'
	TIMEZONE = "Europe/Berlin"
	GITHUB_URL = 'http://github.com/rtens/'
	SOCIAL = (('twitter', 'http://twitter.com/rtens_'),
	          ('github', 'http://github.com/rtens'),)

	# These two lines allow me to write my save my posts like 
	# "blog/articles/myCategory/2013-04-09 Some Title.md" and the category, date and 
	# title will be parsed automatically
	FILENAME_METADATA  = '(?P<date>\d{4}-\d{2}-\d{2}) (?P<title>.*)'
	ARTICLE_DIR = ('articles/')
	
[pelican]: http://github.com/getpelican/pelican
[python]: http://www.python.org/
[markdown]: http://daringfireball.net/projects/markdown/
[Dropbox]: http://www.dropbox.com/home
[out-of-the-box]: https://pelican.readthedocs.org/en/3.1.1/getting_started.html

## Step 4: deployment

I wanted to be able to bring my blog online with

	:::bash
	[local]$ git push web

and found a nice [blog post][push-deploy] about it.

The first step is to create a bare repository on the host

	:::bash
	[remote]$ mkdir blog.git && cd blog.git
	[remote]$ git init --bare

Then create and activate the post-receive hook

	:::bash
	[remote]$ cat > hooks/post-receive
	#!/bin/sh

	HOME=/home/rtens
	TMP=$HOME/tmp/blog
	OUT=$HOME/html/blog
	PELICAN=$HOME/bin/pelican

	echo "Checking-out working copy"
	rm -rf $TMP
	mkdir $TMP
	GIT_WORK_TREE=$TMP git checkout -f

	echo "Generating blog"
	$PELICAN -o $OUT -s $TMP/conf.py $TMP
	rm -rf $TMP

	echo "Done"

	[remote]$ chmod +x hooks/post-receive

Finally, on your local machine, create a repostory, add the remote one and push once

	:::bash
	[local]$ mkdir blog && cd blog
	[local]$ git init
	[local]$ git remote add web ssh://myhost.uberspace.de/home/rtens/blog.git
	[local]$ git add *
	[local]$ git push web master

That's all.

[uberspace]: http://uberspace.de/
[push-deploy]: http://toroid.org/ams/git-website-howto