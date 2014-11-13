Status: draft

I've been working on my Web Application TOol Kit (short *watoki*) for a while now and thought if I ever want anybody besides me to use it, I better write a tutorial.

So here we go. Let's build a ... (drumm roll) ... *blog* application (because nobody has ever done that).

You find the complete code of this application on [github][watoki-demo]. Some section titles link to the commit that contains the code changes of the sections.

[watoki-demo]: https://github.com/rtens/watoki-demo


## Starting Small ##

Since we are all hip and lean and agile, let's build an MVP version (Minimal Viable Product, *not* Most Valuable Player) of our blog. Here is the entire directory structure:

	my_blog
	|- index.html
	'- articles
	   '- 2014-11-13__watoki_tutorial.html

That's pretty minimal. But it works and we can put it online and people can read it and that's what counts.

Now for every new aricle we need to edit the `index.html` file as well which get's annoying pretty quickly. But we can use computer technology to lift this burden.


## PHP to the rescue ##

In order to render the article list dynamically, we need a `index.php` file which reads files from the articles directory and the `index.html` to print them.

	# index.php
	$articles = glob('articles/*.html');
	include('index.html');
		
	# index.html (excerpt)
	<? foreach ($articles as $article) { ?>
	<li><a href="<?= $article ?>"><?= str_replace(["_", ".html"], "", basename($article)); ?></li>
	<? } ?>
	
This is as ugly as it can get but it works and people can read stuff and that's what's important.

We can test it locally with the built-in web server of PHP. Just execute the following in the project root.

	$ php -S localhost:8000

I just want to demonstrate that a lot of times, you don't even need any library or much PHP to build a minimal version of a product. Much can be faked at the cost of maintanance.


## Getting rid of PHP ##

After our last change, the front end designer of the project complains that he can't edit the file anymore because there are weird symbols. So now we can either install PHP on his machine or think of a smarter way to render a list dynamically. What if we could just write

	# index.html
	<ul>
		<li><a href="articles/some_article.html">Date and Title of article</a></li>
	</ul>
	
and some magical program would figure out that we want to repeat that `li` element for every article, filling out the hyperlink target and link caption as well. Well that's almost exactly what we're gonna do, except we have to give some hints to that program because it's not magical after all. We do this with the `property` attribute.

	# index.html
	<ul>
		<li proeprty="article">
			<a property="link" href="articles/some_article.html"><span property="date">Date</span> <span property="title">Title</span>
		</li>
	</ul>

That's some more HTML than before but it still renders as it should when the file is opened in a browser. Next, we're installing our first library: a rendering engine. There are two in *watoki* but the one that let's us not break the template is [tempan] which is short for *Template Animation*. Installing it is a breeze thanks to [composer]. Just open your favourite console at the project's root folder and enter the following (make sure that `composer` is in your `$PATH`)

	$ composer require watoki/tempan
	
And now we need to get our `index.php` to build a proper *View Model* and render the template using *tempan*

	# index.php
	require_once 'vendor/autoload.php';
	
	$viewModel = [
		'article' => assembleArticles()
	];
	
	$renderer = new \watoki\tempan\Renderer(file_get_contents('index.html'));
	echo $renderer->render($viewModel);
	
	function assembleArticles() {
		$articles = [];
		foreach (glob('articles/*.html') as $article) {
			list($date, $title) = explode('__', basename($article));
			
			$articles[] = [
				'link' => array('href' => $article),
				'date' => $date,
				'title' => str_replace(['_', '.html'], '', $title)
			)];
		}
		return $articles;
	}
	
Note that the values of the `proeprty` attributes in the template correspond in structure and names to the array keys of the view model.

[tempan]: http://github.com/watoki/tempan
[composer]: http://getcomposer.org


## Cleaning up ##

The blog works but the code is not very well structured and not at all testable. So let's fix that by putting the code into a class
	
	#index.php
	require_once 'vendor/autoload.php';
	
	class IndexResource {
	
		public function __construct($articlesFolder) {
			$this->folder = $articlesFolder;
		}
	
		public function respond() {
			$renderer = new \watoki\tempan\Renderer(file_get_contents('index.html'));
			return $renderer->render([
				'article' => $this->assembleArticles()
			];
		}
		
		function assembleArticles() {
			// ...
		}
	}
	
	$resource = new IndexResource(__DIR__ . '/articles');
	echo $resource->respond();
	
and that class needs to have it's own file of course. So here is our new folder structure

	my_blog
	|- index.php
	|- src
	|  |- IndexResource.php
	|  '- index.html
	'- articles
	   |- ...


## Restoring structure ##

We are happy but the front-end developer is not because now the link in the static `index.html` doesn't work for him anymore. He asks to use this folder structure instead
	
	my_blog
	|- index.php
	|- src
	   |- IndexResource.php
	   |- index.html
	   '- articles
	      |- ...

but this breaks all our URLs which would make our readers very unhappy. What we would need to do is to route all requests through index.php and tell it to interpret the requests relative to `src`. This is exactly what a Web Delivery system does. Let's use [curir].

	$ composer require watoki/curir
	
All we need to do is tell *curir* where to forward the requests to.

	#index.php
	\watoki\curir\WebDelivery::quickResponse(IndexResource::class);
	
From now on all requests need to go through `index.php` so we have to start the built-in web server with

	$ php -S localhost:8000 index.php
	
When openening `http://localhost:8000` we get the error message that `IndexResource` needs to implement `Responding` so let's make sure that it does. 

[curir]: http://github.com/watoki/curir


## Some convenience ##

We can now use the infra structure of *curir* to make `IndexResource` a little bit slimmer. Since rendering templates is such a common thing, *curir* knows how to do that. We can change the `IndexResource` to

	# src/IndexResource.php
	class IndexResource extends \watoki\curir\Container {
	
		public function __construct($articlesFolder = null) {
			$this->folder = $articlesFolder ?: __DIR__ . '/articles';
		}
	
		public function doGet() {
			return [
				'article' => $this->assembleArticles()
			];
		}
		
		// ...
	}
	
*curir* forwards HTTP requests to methods with the name `do<method>` and treats a returned array as view model for a template name with the same name as the class (without the *Resource* suffix).

We still need to tell *curir* which how to render the template so `index.php` becomes

	#index.php
	\watoki\curir\WebDelivery::init(new TempanRenderer());
	\watoki\curir\WebDelivery::quickResponse(IndexResource::class);


## More dynamics: Routing ##

After successfully publishing a bunch of interesting articles, maintaining the templates gets harder and harder because of all the dublicated HTML code. It would be nice to have a `articles/ArticleResource.php` file with a template that contains the header and footer, rendering the article content dynamically. But this would break the URLs again. What we need is a way to tell *curir* to map `articles/some_article.html` to `articles/article.html?content=some_article`. This can be done with the `DynamicRouter`.

There is no global router in *curir*, as in most web delivery systems. Instead, every `Container` has its own router. By default, the `WebRouter` is used which maps the path of requests directly to the directory structure and also delivers the content of static files. But we can change that by overwriting the `createRouter` method.
	
	# src/IndexResource.php
	class IndexResource extends \watoki\curir\Container {
	
		protected function createRouter() {
			$router = new \watoki\curir\DynamicRouter();
			$router->setPath('articles/{content}', ObjectTarget::factory(ArticleResource::class));
			return $router;
		}
		
		// ...
	}
	
This achives the desired mapping. Note that the `.html` extension is omitted. *curir* doesn't treat extensions as part of the path but as format hints. Note that you can always get a JSON representation of the view model of a resource by providing the extension `.json` (e.g. "http://localhost:8000/index.json").

Now we need the `ArticleResource` class and its template `article.html`. The class looks like this.

	# src/articles/ArticleResource.php
	class ArticleResource extends \watoki\curir\Resource {
	
		public function doGet($content) {
			return [
				'content' => file_get_contents(__DIR__ . '/' . $content . '.html')
			];
		}
	}
	
Note that *curir* maps all query arguments to the method parameters, in this case the `content` query argument from the mapped request `articles/article?content=some_article`.

(Pro-Tip: at this point, nothing keeps us from writing the articles in another mark-up language, for example markdown)
	

## Throwing the right Error ##
	
If we now try to browse to an article that doesn't exist, we get an "Internal Server Error" instead of the "File Not Found" we would expect. So let's fix that.

	# src/articles/ArticleResource.php
	class ArticleResource extends \watoki\curir\Resource {
	
		public function doGet($content) {
			return [
				'content' => $this->assembleContent($content)
			];
		}
		
		private function assembleContent() {
			$file = __DIR__ . '/' . $content . '.html';
			if (!file_exists($file)) {
				throw new \watoki\curir\error\NotFoundError("Article [$content] does not exist.");
			}
			return file_get_contents($file);
		}
	}

*curir* catches all errors (including fatal ones) and exceptions and renders them as "Internal Server Errors". Other HTTP status codes can be achieved with `HttpError` and it's subclasses.


## Le Fin ##

That's it. That's our little blog. Of course a lot of more features come in mind. Comments for example. Or being able to write new articles on the website instead of uploading them as files. Maybe we still have time for the comments at least.

All we need is a simple form and show existing comments in the footer of our article template.

	# article.html
	<form method="post">
		<input name="name" placeholder="Your Name">
		<textarea name="comment" placeholder="What would you like to add?"></textarea>
	</form>
	
	<div property="comment">
		<h4 property="name">The Author</h4>
		<p property="comment">My Comment</p>
	</div>
	
A method handling the *POST* request:

	# src/articles/ArticleResource.php
	
	class ArticleResource extends \watoki\curir\Resource {
	
		public function doPost($content, $name, $comment) {
			$comments = json_decode(file_get_contents($this->commentsFile($content)), true);
			$comments[] = [
				'name' => $name,
				'comment' => $comment
			];
			file_put_contents($this->commentFile($content), json_encode($comments));
		}
	
		public function doGet($content) {
			return [
				'content' => $this->assembleContent($content),
				'comment' => $this->assembleComments($content)
			];
		}
		
		private function assembleComments($content) {
			return json_decode(file_get_contents($this->commentFile($content)), true);
		}
		
		private function commentsFile($content) {
			return __DIR__ . '/' . $content . '_comments.json';
		}
		
		// ...
	}
	
