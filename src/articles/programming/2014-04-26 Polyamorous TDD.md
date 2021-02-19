Tags: TDD, clean code, PHP

Three things happened during the last week that each increased my urge to write this article. The coincidence is almost uncanny.

* Monday: over the easter weekend I finally built a tool I've been meaning to build for over a year.
* Tuesday: I became responsible for releasing and quality of my first [Ruby on Rails] project.
* Wednesday: [David Heinemeier Hansson][dhh] wrote a [controversial article] about [TDD]

The connections between these events are actually circular. 

* The tool is part of a management method that I will employ in the Rails project. 
* David happens to be the creator of Rails.
* Both the tool and the management method evolve around automated tests and tackle precisely the problem David seems to have with TDD.

Each of these events deserves it's own article. So I'll concentrate in this one on my point of view concerning the discussion that spun around David's article.

[Ruby on Rails]: http://rubyonrails.org/
[dhh]: http://david.heinemeierhansson.com/
[controversial article]: http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html
[TDD]: http://c2.com/cgi/wiki?TestDrivenDevelopment



## Programming & Life Styles

[Robert Martin] responded to David with an article he titled *[Monogamous TDD]* in which he compares TDD with monogamy, contrasting it with David's analogy *"Test-first fundamentalism is like abstinence-only sex ed"*.

I like the metaphor. Like abstinence or monogamy, TDD is *choice* of style. And for some, strict TDD probably feels like abstinence. Unintuitive, unnatrual, morally charged and impossible to adhere to. But there are a lot of people who choose this life style - some even without any moral pressure. Other people choose monogamy (most of them nowadays in its weaker, *serial* variation) and live a happy life with it.

(Concerning the terminology here: I can't quite put my finger on it but I have the feeling that both authors mean *Unit Testing* when they speak of *Test Driven Development*. Just to be clear about my point, I'm gonna use the term *Unit Testing* from now on.)

The important thing for me is to *have a choice*. And also to consider them. And to keep in mind that there may be incompatibilities between the styles. If a monogamist starts a relationship with an abstainer, both of them will become unhappy. If somebody does not want to use a test-first development style in his project, that's fine with me. But I won't collaborate with him.

And of course there are even more alternatives. Polyamory for example. And I might be stretching the metaphor a bit here but to me, the polyamorous approach to testing would be to do Unit Testing as well as testing through the GUI as well as all the testing strategies that lie between those two extremes.

![spectrum of testing strategies](/res/testing/spectrum.png)

I often wonder why so little is said about the range in the middle and why both, David and Robert seem to ignore it.

[Robert Martin]: http://en.wikipedia.org/wiki/Robert_Cecil_Martin
[Monogamous TDD]: http://blog.8thlight.com/uncle-bob/2014/04/25/MonogamousTDD.html



## Trust

In the end it's all about one thing: **Trust**.

That's a very powerfull thing. So powerful, people tend to become quite passionate once they start working on a non-trivial code base that they could trust completely. I at least became very passionate about it.

So the most important question is: how do we achieve this level of trust? How can we be certain that a programm *works as expected* to the point that we can deploy purely on the basis of automated tests?

For TDDlers it's almost trivial to answer the question if a programm *works as expected*. They write their expectations in code. So it works if all tests pass. Problem solved. But for non-programmers it's not that easy. Their expectations are intransparently translated into something they cannot understand. They only have the GUI.

But as Uncle Bob states correctly, testing through the GUI is slow. Very slow if done manually, and still pretty slow but also very fragile if done automatically. It's fragile because the GUI changes way more than the *behaviour* of the software so GUI tests tend to give a lot of false positives and thus are maintanance heavy. The following graph shows my impression of how execution time increases with the level of integration.

![execution time over integration](/res/testing/execution_time.png)

But tests written at GUI level are very attractive for business stake holders because they can understand them and therefore *trust* them. But we can't test the entire system through the GUI so we need Unit level tests as well. Tests that the developers can trust.

In my opinion, both testing approaches are complementary and trust from all sides can only be achieved if they are both implemented. But in the right mix that keeps the balance.



## Daedalus Testing

But what about that range of testing approaches between the two extremes? Unfortunately the terminology is highly inconsistent here but I'll try to put them in order, starting at the most integrational strategy becoming more granular. Here is what this scale could look like:

* (G)UI
* End-to-end
* System
* Integration
* Module
* Component
* Unit

Since developers can't trust GUI testing and business people can't trust anything too close to Unit testing the ideal approach could be to stay in a range somewhere not high and not too low. Let's call this approach *Daedalus Testing*.

The maximum granularity of this range is where business people stop understanding the domain and the maximum of integration is where fragility and execution time become too high for practical use.

These tests need to be written in a language that developers as well as non-developers understand. I will write about how this can be done in my next article.



## Test First

There are two discussions which are often times interwinded. One is about automated testing vs. manual testing. The other one is about *Test First* vs. *Test Later*. Since this is rarely addressed explicitly, I'm not sure what the opposition to automated testing looks like or if it even exists.

But for me personally, the *only* reliable way of producing a complete suite of high quality automated tests consistently is to write them first. I also agree completely with Uncle Bob when he says that ["Tests are first in all things"][testfirst]. And I consider it proven that writing them first has a lot of positive effects on the production code but these effects are secondary to me. The most important thing by a long shot is trust.

If you want to find out if a test suite is complete just try to delete code that doesn't make any test fail.

[testfirst]: http://blog.8thlight.com/uncle-bob/2013/09/23/Test-first.html



## Up Next

As said in the beginning, I originally wanted to write about my testing approach, the tool I wrote for it and how I plan to use it as a managment strategy in my current project. And I will. But I also wanted to cover the philosophical ground which I hope to have done here.