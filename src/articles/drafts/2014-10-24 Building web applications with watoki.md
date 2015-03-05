Status: draft

I've been working for about a year now on a project named [**w**eb **a**pplication **to**ol **ki**t][watoki] (short *watoki*) and thought if I ever want anybody besides me to use it, I better write about how.

*watoki* a collection of libraries that provide infrastructure commonly needed by web applications - think loosely couple web framework. The goal of each library is to be as lightweight as possible and to make it easy for the client code to stay independent of the infrastructure. You can find an overview of all the libraries [here][watoki].

So in this article I would like to give you a step-by-step guide of how I would a simple web application with this tool kit. So here we go. Let's build a ... (drum roll) ... *blog* application (because nobody has ever done that). We're gonna take a very light-weight approach and then reduce maintenance cost by using a rendering and web delivery library. So in the end only two libraries are presented here but it should be enough to get you started.

You find the complete code of this application on [github][watoki-demo]. The section titles link to the commit that contains the code changes of the sections so you can browse the entire code at that state and play around with it.

[watoki]: http://github.com/watoki
[watoki-demo]: https://github.com/rtens/demo-blog


## [Starting Small](https://github.com/rtens/demo-blog/tree/01761ba184a3922e647d804fe5c878198bafcb01) ##

Since we are all hip and lean and agile, let's build an MVP version (Minimal Viable Product, *not* Most Valuable Player) of our blog consisting of an overview and a single article. Here is the entire directory structure:

	demo-blog
	|- index.html
	'- articles
	   '- 2011-12-13__watoki_tutorial.html

That's pretty minimal (and ugly, visually). But it works and we can put it online and people can read it and that's what counts.

Now if I want to write another article, we'd have to

1. copy the last article and change its content
2. add it to the `index.html`

The second step gets annoying pretty quickly especially if I forget to do it and then wonder why nobody reads about my newest epiphany. But we can use computer technology to fix this.


## [PHP to the rescue](https://github.com/rtens/demo-blog/tree/e448998d9c562ec84d313e362fed0156a624c14d) ##

(Did I mention that *watoki* is written in PHP? I hope you are not disappointed now that I didn't opt for a more trendy language. But PHP isn't actually half bad. So deal with it.)

It would be nice if we could just read the files in `articles` and print them as a list. In order to do so, we need an `index.php` to read the files and the `index.html` to print them.

	# index.php
	$articles = glob('articles/*.html');
	include('index.html');
		
	# index.html (excerpt)
	<? foreach ($articles as $article) { ?>
	<li><a href="<?= $article ?>"><?= str_replace(["_", ".html"], " ", basename($article)); ?></li>
	<? } ?>
	
This is as ugly as it can be but it works and people can find and read articles without us having to update the list every time and that's what's important.

We can test it locally with the built-in web server of PHP. Just execute the following command in the project root and point your browser to [`http://localhost:8000`](http://localhost:8000).

	$ php -S localhost:8000

I started with this as-simple-as-possible version because I want to demonstrate that a lot of times, you don't even need any library or much PHP code to build a minimal version of a product. Much can be faked for the sake of speed - at the cost of maintanance though.


## [Getting rid of PHP](https://github.com/rtens/demo-blog/tree/6035cca8dd7f1ca8f77662957571c109272ebf89) ##

After our last change, the front end designer of the project complains that he can't edit the HTML files any more because there are weird question marks and dollar symbols everywhere. So now we can either install PHP on his machine and teach him how to use it or we could think think of a smarter way to render a list dynamically. What if we could just write

	# index.html
	<ul>
		<li><a href="articles/some_article.html">Date and Title of article</a></li>
	</ul>
	
and some magical program would figure out that we want to repeat that `li` element for every article, filling out the hyperlink target and link caption as well. 

Well, that's almost exactly what we're gonna do, except we have to give some hints to that program because it's not that magical after all. We do this with the `property` attribute.

	# index.html
	<ul>
		<li property="article">
			<span property="date">2011, December 13th</span>
			-
			<a property="link" href="articles/some_article.html">
				<span property="title">Title of my article</span>
			</a>
		</li>
	</ul>

That's some more HTML than before but it still renders as it should when the file is opened in a browser. In order to actually render our dynamic list, we need to install our first library: a rendering engine. There are two in *watoki* but the one that does the neat HTML trick is [tempan] which is short for *Template Animation*. Installing it is a breeze thanks to [composer]. Just open your favourite console at the project's root folder and execute the following command (make sure that `composer` is installed and in your `$PATH`)

	$ composer require watoki/tempan
	
And now we need to get our `index.php` to build a proper *View Model* (an array with keys matching the `property` values of the template) and render the template using *tempan*

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
				'date' => date('Y, F dS', strtotime($date)),
				'title' => str_replace(['_', '.html'], ' ', $title)
			];
		}
		return $articles;
	}
	
Now we feel a lot better since we separated logic from presentation. All data manipulation is now done by `index.php` and `index.html` contains nothing but mark-up description. Time to lean back and enjoy our beautiful code.

[tempan]: http://github.com/watoki/tempan
[composer]: http://getcomposer.org


## [Cleaning up](https://github.com/rtens/demo-blog/tree/55332545c10ecafa62b52d6e896c66962795c657) ##

But soon the code doesn't look that beautiful any more, since it's all thrown together in one file. And it's also not at all testable. So let's structure it a bit better by putting the code in a class.
	
	#index.php
	require_once 'vendor/autoload.php';
	
	class IndexResource {
	
		public function respond() {
			$renderer = new \watoki\tempan\Renderer(file_get_contents('index.html'));
			return $renderer->render([
				'article' => $this->assembleArticles()
			]);
		}
		
		function assembleArticles() {
			// ...
		}
	}
	
	$resource = new IndexResource();
	echo $resource->respond();
	
and that class better lives in its own file of course. So here is our new folder structure

	demo-blog
	|- index.php
	|- IndexResource.php
	|- index.html
	'- articles
	|  |- ...
	'- ...

	
## [Deliver it](https://github.com/rtens/demo-blog/tree/48859dd381168113589bd0025c9f6a7711984cad) ##

On their surface, web applications are all about getting a request to a resource and delivering the response back to the user. So let's use a web delivery library that handles most of it for us. The one provided by *watoki* is called *[curir]* (pronounced like "courier"). Again we can use composer to install it

	$ composer require watoki/curir
	
Now all we need to do is tell the `WebDelivery` to use the `IndexResource` as the root resource.

	#index.php
	\watoki\curir\WebDelivery::quickResponse(IndexResource::class);
	
If we run application now, it'll complain that `IndexResource` needs to implement `Responding`. So let's make sure that it does.

	#IndexResource.php
	
	class IndexResource implements \watoki\deli\Responding {

		public function respond(\watoki\deli\Request $r) {
			$renderer = new \watoki\tempan\Renderer(file_get_contents('index.html'));
			return $renderer->render([
				'article' => $this->assembleArticles()
			]);
		}
		
		// ...
	}
	
The `Responding` interface defines a method `respond` which receives a `Request` object from *curir*. We can use it to get information about the request, for example the request method or the value of a `page` parameter in case the list is paginated.

	#IndexResource.php/IndexResource
	
	public function respond(\watoki\deli\Request $r) {
		$method = $r->getMethod();
        $page = $r->getArguments()->get('page');
		// ...
	}

[curir]: http://github.com/watoki/curir


## [Easier Delivery](https://github.com/rtens/demo-blog/tree/da0fcf69f1b5580c64ce9f8dfbc4b0d29a144018) ##

But since resources almost always respond to a certain method with certain parameters and then render a template using structured data, *curir* provides an easier way to do that. By extending `Container`, we can replace the `respond` method with the following

	#IndexResource.php
	
	class IndexResource extends \watoki\curir\Container {
	
		public function doGet() {
			return [
				'article' => $this->assembleArticles()
			];
		}
		
		// ...
	}
	
*curir* maps the request to a resource to a method named `do<HTTP_METHOD>` and the returned value is used as data for the renderer which uses a file with the same name as the resource as template (in this case `index.html`). The default renderer is the `PhpRenderer` so we need to tell curir to use *tempan*.

	#index.php
	$factory = WebDelivery::init(new TempanRenderer());
	WebDelivery::quickResponse(IndexResource::class, $factory);
	
	
## [Talk to me](https://github.com/rtens/demo-blog/tree/cc8b8159c946ec4a79224fb051eeac78921ad6bb) ##

The blog is a roaring success and tons of people read it but more and more would like to be able to comment on the articles. So we add a comment form to each article and point it to the `index.php`.

	#2011-12-13__watoki_tutorial.html
	<hr>
	<h3>Leave a comment</h3>
	<form method="post" action="../index.php">
		<input type="hidden" name="article" value="watoki tutorial">
		<input type="text" name="email" placeholder="Your Email"><br>
		<textarea name="comment"></textarea><br>
		<input type="submit">
	</form>
	
If we just try to submit that form, we'll get an error page saying "Error: 405 Method Not Allowed" and clicking on the *details* link reveals that "Method [doPost] does not exist in [IndexResource]". So let's add it.

	#IndexResource.php/IndexResource
	
	public function doPost() {
        return array_merge($this->doGet(), [
            "message" => "Thanks for your comment. I'll publish it soon."
        ]);
	}
	
This works, but we don't see the message yet because we need to add it to the template. Let's put it into the sub-header.

	#index.html
	<h4 property="message">[...]</h4>
	
If we now would like to email the comment to ourself, we need to access the submitted data. Since *curir* maps the request parameter to the method signature, we can simply do this:

	#IndexResource.php/IndexResource
	
	public function doPost($article, $email, $comment) {
        mail("me@example.com", "New comment on $article", $comment, "From: $email");
        // ...
	}


## [Dynamic Articles](https://github.com/rtens/demo-blog/tree/23a34b25647c114adfb5f2db2753fbcacce99b89) ##

The comments work great but we receive so many that adding them to each article quickly turns into a bottle neck. We want to be able to show them automatically and while we're at it, use a template for the articles so we don't have to copy the entire page for each new article. There is only one solution: articles need to become dynamic resources.

The first step is to strip the article files of all non-content HTML and put that into a template.

	#article.html
	<a href="index.php">Overview</a>

	<h1 property="title">Building Web Applications with watoki</h1>
	<h4 property="date">Tue 13 December 2011</h4>

	<div property="content">Here be content</div>

	<hr>
	<h3>Leave a comment</h3>
	<form method="post" action="index.php">
		<input property="commentOn" type="hidden" name="article" value="watoki tutorial">
		<input type="text" name="email" placeholder="Your Email"><br>
		<textarea name="comment"></textarea><br>
		<input type="submit">
	</form>
	
The second step is to create a corresponding resource class with a `doGet` method.

	#ArticleResource.php
	
	class ArticleResource extends \watoki\curir\Resource {

		public function doGet($article) {
			list($date, $title) = explode('__', $article);

			return [
				'title' => ucfirst(str_replace('_', ' ', $title)),
				'date' => date('Y, F dS', strtotime($date)),
				'content' => file_get_contents("articles/$article.html"),
				'commentOn' => ['value' => $article]
			];
		}
	}
	
The last thing we need to do is adapt the links in the overview list so they point to the new resource, e.g. `article.html?article=2011-12-13__watoki_tutorial`.

	#IndexResource.php/IndexResource::assembleArticle()
	
	return [
		'link' => array('href' => 'article.html?article=' . substr(basename($articleFile), 0, -5)),
		'date' => date('Y, F dS', strtotime($date)),
		'title' => str_replace(['_', '.html'], ' ', $title)
	];

Lastly, we need to put `WebDelivery` in charge of all requests so it can them to the dynamic resources. We can do this by passing `index.php` to the web server as "routing file" (or using `mod_rewrite` with *Apache*).

	$ php -S localhost:8000 index.php
	
To keep this tutorial short, I'm not gonna describe how to display the comments, but you can find it in the [source code] or try to do it as an exercise.
	
[source code]: https://github.com/rtens/demo-blog/tree/84e01ef1e1fa8909275301165c40509c4be2032c


## [Link Reanimation](https://github.com/rtens/demo-blog/tree/5137eadc067f04bd01e42a79a706006d9371f26d) ##

Everything seems to be working well until we realise that all links to our articles that we sent to our friends and proudly tweeted about are now broken. Because articles now have the URLs `article.html?article=foo` instead of `articles/foo.html`. We have to find a way to map the latter to the former.

As almost always, there are multiple ways to achieve one goal. For example we could do the re-routing on web server level (e.g. with `mod_rewrite`) but let's say that we want to do it in the application so we can stay environment-independent.

A design goal in all the *watoki* libraries was to avoid "magic" without compromising convenience. This is achieved by always keeping things *discoverable* but offering short-cuts for the most common use cases. This of course works best if you are using an IDE that supports code navigation (like [PhpStorm] - sorry Sublimers) so you can jump to a symbol definition by simply clicking on it. 

You can use the following approach for answering most questions of the form "How can I change X?" in all libraries of *watoki*. I suggest that, while reading the following explanation, to try retracing the described paths in the actual code.

That said, let's try to find out how *curir* routes requests so we can change it. We made sure that all requests are handled by `index.php` where we call `WebDelivery::quickResponse()`, but what happens next? With a little digging, we'll find that the call leads to the following code being executed.

	#WebDelivery.php/WebDelivery::quickResponse (in-lined & simplified)
	
	$router = new NoneRouter(RespondingTarget::factory($root));
	$builder = new WebRequestBuilder(new WebEnvironment($_SERVER, $_REQUEST, $_FILES));
	$deliverer = new WebResponseDeliverer();
	
	$delivery = new WebDelivery($router, $builder, $deliverer);
    $delivery->run();

The `WebDelivery` is instantiated with a `Router`, a `RequestBuilder` and a `ResponseDeliverer`, so a request is built, routed to its target, and the response delivered. The router is this case does nothing (hence **None**Router) and its target is a `RespondingTarget` whose `respond()` method simply invokes the `respond()` method of the *root* resource, in our case `IndexResource`. So in order to change the routing behaviour, we could exchange that `NoneRouter` with our own, configured version. By looking at sub-classes of `Router` we see a class called `DynamicRouter` which turns out to be just what we need. The result would look like this.

	#index.php
	$factory = WebDelivery::init(new TempanRenderer());
	
	$router = new \watoki\deli\router\DynamicRouter();
	$router->addObjectPath('articles/{article}', ArticleResource::class, $factory);
	$router->addObjectPath('', IndexResource::class, $factory);
	
	WebDelivery::quickRoute($router, $factory);

	
This works! But of course there is also another way (which is usually easier and also more flexible). With a little more digging we find out, that the `respond()` method of `IndexResource` is inherited by `Container` which again, uses its own router to find the target of the request. So if every `Container` has its own `Router`, we can just extend that a little and don't have to overwrite the global router of `WebDelivery`. All we need to do is overwrite the `createRouter()` method.

	#IndexResource.php/IndexResource

    protected function createRouter() {
        $router = new \watoki\deli\router\DynamicRouter();
        $router->addObjectPath('articles/{article}', ArticleResource::class, $this->factory);
        return new MultiRouter([$router, parent::createRouter()]);
    }
	
[PhpStorm]: https://www.jetbrains.com/phpstorm/
		
	
## [Article Not Found](https://github.com/rtens/demo-blog/tree/88824984e45008e4342c7132a95d93ed6c685d6b) ##
	
All our URLs work again and we're fairly happy with the whole thing. But we discover one rather annoying thing: If we now try to browse to an article that doesn't exist (e.g. [`articles/foo`](http://localhost:8000/articles/foo)), we get a weird empty article instead of the "File Not Found" error we would expect. So let's fix that.

	#ArticleResource.php/ArticleResource
	
	public function doGet($article) {
        $file = "articles/$article.html";
        if (!file_exists($file)) {
			throw new Exception("The article [$article] does not exist.");
        }
		
		// ...
	}

Now we get an "500 Internal Server Error" since *curir* catches all errors (including fatal ones) and exceptions and turns them into server errors. In order to generate other HTTP status codes and custom messages we can throw an `HttpError` instead.
	
	throw new HttpError(WebResponse::STATUS_NOT_FOUND, "The article [$article] does not exist.");
		


## Le Fin ##

So this is how you build a basic web application with *[watoki]*, or more precisely with *[curir]* and *[tempan]*. Of course this tutorial only covers a tiny part of the mentioned libraries and an even smaller part of the whole tool kit. So if you would like to give any of these libraries a try or have any comment or feedback, just drop me a line. I always appreciate any feedback.
