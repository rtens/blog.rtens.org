Tags: git, linux, python

If it wasn't for [pelican], this blog would probably not exist. So here is a brief description on the why and what and how.

[pelican]: http://github.com/getpelican/pelican

## Step 1: engine

The spark that got this blog going was my colleague showing me [pelican] yesterday which is a static blog generator written in [python]. This means that I can put my files and articles in whatever directory structure I fancy and generate the website as static files. The articles are written in a simple mark-up language (I use [markdown]) and annotated with meta-information. This has some nice advantages:

1. Speed and security
1. No internet access required (I sync across devices with [Dropbox])
1. No web editors (which annoy especially on the phone)
1. Adding custom static pages comes naturally
1. I kept a copy of my blog posts on my machine anyway

[python]: http://www.python.org/
[markdown]: http://daringfireball.net/projects/markdown/
[Dropbox]: http://www.dropbox.com/home

## Step 2: installation

I recently switched my web hosting to [uberspace] which offers all I could ever wish for and a surprising pricing model. You pay basically as much as you want with a minimum of 1€ per "space" and month. This makes it possible to have multiple accounts, which is perfect when having a bunch of independent projects as in my case. Thanks to my new hoster, installing and running pelican was simply
	
	:::bash
	[remote]$ easy_install pelican markdown
	[remote]$ pelican

This generates an empty blog in an `output` directory.

My Windows machine at home took a little more persuasion. First step is to install Python version 2. Fortunately there is a nice package with [installer]. Before we can install pelican we need easy_install first which can be obtained by running [ez_setup.py] from [this page][setuptools]. Now we can use the two commands shown above to create a local version of the blog.

[uberspace]: http://uberspace.de/
[installer]: http://www.python.org/getit/
[ez_setup.py]: https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py
[setuptools]: https://pypi.python.org/pypi/setuptools/0.9.1#installation-instructions

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
	
[out-of-the-box]: https://pelican.readthedocs.org/en/3.1.1/getting_started.html

## Step 4: deployment

I wanted to be able to bring my blog online with [git] push

	:::bash
	[local]$ git push web

and found a nice [blog post](push-deploy) with instructions.

The first step is to create a bare repository on the host. it must be bare so we can push to it.

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

Finally, on your local machine, create a repostory, add the remote repository and push once

	:::bash
	[local]$ mkdir blog && cd blog
	[local]$ git init
	[local]$ git remote add web ssh://myhost.uberspace.de/home/rtens/blog.git
	[local]$ git add *
	[local]$ git push web master

That's all

[git]: http://git-scm.com/
[push-deploy]: http://toroid.org/ams/git-website-howto

## Update: better deployment

The above approach does not react on errors during the generation. So I decided to use the pre-receive hook for deployment and abort the push if the generation does not run smoothly. I found the instructions on [codeutopia].

	:::bash
	#!/bin/sh

	home=/home/rtens
	tmp=$home/tmp/blog
	out=$home/www/blog.rtens.org
	pelican=$home/bin/pelican

	echo "Deploying to $out ..."

	if [[ -d $tmp ]] ; then
		rm -rf $tmp
	fi
	 
	mkdir $tmp

	while read oldrev newrev refname
	do
		revtmp=$tmp/$newrev
		errors=$revtmp/errors
		mkdir $revtmp
		
		echo "Extracting working copy for $newrev ..."
		git archive $newrev | tar -x -C $revtmp

		echo "Generating blog..."
		cd $revtmp
		$pelican -o $out -s conf.py src 2>$errors
		rc=$?
		
		if [[ $rc != 0 ]] ; then
			echo "ERROR: Errors while generating blog."
			exit $rc
		fi
		
		if [[ -s $errors ]] ; then
			echo "ERROR: Warnings while generating blogs."
			exit 1
		fi
	done

	echo "Done."
	exit 0

[codeutopia]: http://codeutopia.net/blog/2011/06/30/how-to-automatically-run-unit-tests-from-a-git-push/