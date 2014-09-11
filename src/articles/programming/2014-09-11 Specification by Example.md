Tags: TDD, BDD

In a [previous post] I argued against a testing monoculture and suggested to mix tests with different levels of integration. Since UI tests cannot test the system completey, but unit tests are often times too fine-grained to justify their investment, staying away from these extremes is often times the best solution. I called this strategy *Daedalus Testing*.

I've been using this approach for a while now and also [talked about it][talks] at several conferences so I thought it's time to write down how I implement the approach and which tools I use.

[previous post]: http://blog.rtens.org/polyamorous-tdd.html
[Specification by Example]: http://specificationbyexample.com
[talks]: http://blog.rtens.org/category/talks.html


## TDD vs BDD

In the majority of articles I read about *Test-Driven Development*, the author uses it as a synonym with *Unit Testing*, ignoring that any testing strategy can be applied in a test-driven manner. It seems to me that almost always when people get [frustrated about TDD][tdd is dead], they are actually frustrated about unit testing. 

I agree with [Justin Searls] who argues that this frustration emerges mostly from [*The Failures of "Intro to TDD"*][failures] and the false promise that unit-level TDD automatically leads to better design. So when we teach test-driven developing practice, we must be careful to not limit it to unit testing but enable writing automated test on every level of abstraction and with any amount of integration.

<img src="static/img/test_stack.png"/>

[tdd is dead]: http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html
[Justin Searls]: https://twitter.com/searls
[failures]: http://blog.testdouble.com/posts/2014-01-25-the-failures-of-intro-to-tdd.html



## Description Levels

The first question, I ask myself when I start with a new system is "What do I want to specify first?", which leads to "What part of the system should I build first?", which should be answered by "What has the biggest value?".

If the purpose of the system is to automate a process, then the most important part are probably the **business rules**. In this case, the specification should be on the level of the business logic and use the language of the process. This naturally leads to a system design where the business logic is encapsulated into something - call it [interactors] or [use-cases service]. The architecture of the production system is actually secondary. The important thing is that the behaviour of the business logic is not described on the user interface level, nor on the class/unit level but on the business process level.

Unless of course it's the behaviour of the **user interface** you would like to specify. This is usually very hard for me since often times user interface have a lot of "soft" specifications, like "it needs to feel snappy", "it needs to look consistent", and "it needs to be pleasent to the eye". I have yet to find a way to describe these requirements in a language that the computer understands. Instead I [make it really easy][tempan] to test my HTML templates manually. But sometimes there is actually logic in the UI worth an automated test. This test but only this test should be written using UI concepts like forms and clicking buttons.

Or maybe I already have a system and it's a **sub-system** or just a **single class** whose behaviour I would like to specify. This is when I can do do my old fashioned unit-testing and use concepts like exceptions and method calls in my test.

I rarely ever use full-stack HTTP-level **integration** tests so I don't have any guidelines for those yet.

Each level of abstraction targets a different kind of stake holder and uses a different language with different concepts, but should be consistent within their boundaries. The automated tests are also usually implemented using different technologies. I usually start on the level of the business domain and move up to a more integrational level if I need more confidence and down to a more unit-level if I need to locate a bug or implement a complicated algorithm.

[interactors]: http://www.youtube.com/watch?v=WpkDN78P884
[use-case service]: http://victorsavkin.com/post/42542190528/hexagonal-architecture-for-rails-developers
[tempan]: http://blog.rtens.org/codemotion-2013.html



## Test Literacy

So now that you have nice automated tests make sure that people can read them. I've heard a lot that "tests document the production system" and I'm convinced that it's true but only under the condition that you can understand the test. Any maybe that's just me, but reading code is hard (and also no fun). And even more important maybe, there are a lot of people who are not even able to read code. Think of the business stake holders. They should be part of formulating the specification of a system as well. Especially when they are about business logic.

So let's not use code to describe the test cases but a natural language that everybody, not just technical people, can understand - an **ubiquitous language**. If we normalize the language's structure just a bit, we can still implement it and execute it automatically. This strategy is commonly known as [Behaviour-Driven Development][BDD]. But since the semantic delusion of that term has reached a point where it means anything and nothing, I'm gonna use [Specification by Example (SbE)][SbE] instead.

The idea of SbE is to describe the behaviour of any system with *examples*. These examples are written collaboratively in a way that *all* stake holders can understand. They are then implemented as automated tests without changing the original formulation of the example. This way they can serve as specficiation, validation and documentation of any software system.

These examples can be formulated in any way and still be implementable. But it helps to have some structure so I usually use a [gherkin]-ish syntax with *given*, *when* and *then* but it works just as well with the *describe-context-it* structure of [rspec] and its relatives.

So instead of

	:::python
	def testIsDeliveryFree(self):
		customer = Customer()
		customer.setVip(true)
		
	    basket = Basket()
	    for i in range(5):
		    basket.getItems().append(Book())
	    
	    delivery = DeliveryManager(customer, basket)
	    
	    self.assertTrue(delivery.isDeliveryFree())

you can write

	:::python
	def scenarioVipWithFiveBooksShouldBeFree(self):
	    self.givenIAmAVipCustomer()
	    self.givenIHave_BooksInMyBasket(5)
	    self.whenICheckMyDeliveryOptions()
	    self.thenTheDeliveryShouldBeFree()

[BDD]: http://dannorth.net/introducing-bdd/
[SbE]: http://specificationbyexample.com/
[gherkin]: https://github.com/cucumber/cucumber/wiki/Gherkin
[rspec]: http://rspec.info/



## Make it accessible

Now that we have nice abstractionally-bounded specifications, implemented as automated tests and written in an ubiquitous language using examples we need a way that people can find them. Of course there are in the code base but first of all, they are still (although very niceley readable) code and second of all, not everybody is confortable with browsing through a code base.

So we need a way to browse the specifications comfortably and have them presented in an easy-to-read form. The approach of [cucumber] and [its sorts][behat] is to write the specification in plain text files and match them with code fragments when run. But for me this simply causes too much duplication and it's also one more language with yet another syntax and its own quirks and (usually) no support for code navigation and refactoring. 

As I've shown above, all you need is a simple *method extraction* to put this ugly test code into easily understandable methods with natural-language names. It's really all it takes. The mentioned tools argue with increasing the readability of the tests since they are not written in code but in my experience the gain is marginal at best.

If tests are really to play the role of documenation, they also need to be *accessible for everyone*. The code repository is not neccesarily the most accessible place for business stake holders. What they usually ask for is a PDF of HTML file they can browse and read easily. So why not export the test code to a browsable web page?

Born was *[dox]*, a browser for executable documentation. It parses the test classes, their methods, code and comments and creates HTML pages that you can browse and read. Comments are parsed as well so the can contain HTML or other mark-up languages like [markdown] in order to create beautiful living documentation. *dox* also processes test reports and indicates the status of each scenario with colors. This way you can easily see how many scenarios are already implemented and which ones are failing.

<img src="static/img/dox_diagram.png"/>

Just check out dox's [documentation] to learn more about it or [drop me a line][twitter] if you would like to try it for you project.

[cucumber]: http://cukes.info/
[behat]: http://behat.org
[dox]: http://dox.rtens.org
[markdown]: http://daringfireball.net/projects/markdown/
[documentation]: http://dox.rtens.org/projects/rtens-dox/specs/Introduction
[twitter]: https://twitter.com/rtens_