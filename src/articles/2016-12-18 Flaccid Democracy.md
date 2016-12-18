I must confess I was never much interested in politics, and therefore very grateful when I found the [Wahl-o-mat] which freed me from having to read the party platforms myself. I always viewed [non-politic civic participation][democracy2] as the more effective, certainly more efficient way for changing society and have been pondering for years how the open market's incentives can be moved towards a more social and sustainable economy. Indeed I always thought of politics to be quite tedious, boring even. I now realized what a luxury that was.

I the world in a crisis? Is democracy in a crisis? It's probably too early to say but it sure looks that way. It seems to be getting from bad to worse to absolute worst. First, the success of right-wing parties in eastern Europe, then the formation and partial success of a new nationalist party in Germany, then Brexit and now Trump.

Why is this happening? I don't know and I haven't seen a satisfying answer yet. But I have a theory.

[Wahl-o-mat]: https://www.wahl-o-mat.de
[democracy2]: https://www.opendemocracy.net/ourkingdom/hendrik-wagenaar/is-democracy-in-crisis-no-there's-just-new-type-of-emerging-democracy


## Technical Debt

When I saw what is happening in these countries I experienced a familiar feeling. I was still very much convinced that the system is not to blame. But something went clearly wrong. It was the same feeling that I had when I saw or read about software development teams that were unhappy with "Agile" and are convinced that it "failed" them.

What I saw in these teams was something that Martin Fowler calls [Flaccid Scrum]. Said teams usually only adopted the managing practices of the method with less regard the technical practices. Robert C. Martin has an [interesting historical explenation][bob] on why it is this way. And they fail because the one thing doesn't work without the other. Not for long at least.

What happens is that if you decide to just release more ofter and to be more flexible about the requirements and just to "go faster", it's crucial that your code base actually lets you do all of these things. For that it has to be *clean* enough to allow easy and frequent changed. If you don't refactor mercilessly and constantly, your code base will turn into a dump with time.

The growing dump doesn't hinder you much in the beginning and you actually start to become faster and reap the benefits of agile development, but after a while, the growing amount of ad-hoc solutions make it harder and harder to extend the system, implementing new functionality and changing existing ones takes longer and longer, and you slowly grind to a halt.

Keeping the code base clean requires skills and, maybe more importantly, discipline. This is why things like TDD and Pair Programming exist. It's much like keeping your kitchen sink clean while cooking. It's not as much fun as releasing features, but it's absolutely necessary. Otherwise you will create what Ward Cunningham called [Technical Debt]. And just like financial debt, it can be a useful tool, but if not taken care of, it can also make you bancrupt.

This is what I believe is happening in many democratic countries.

[Flaccid Scrum]: http://martinfowler.com/bliki/FlaccidScrum.html
[Technical Debt]: http://martinfowler.com/bliki/TechnicalDebt.html
[bob]: https://skillsmatter.com/skillscasts/8016-the-future-of-programming


## Power and Knowledge

What is democracy? It's "power of the people". That means that "the people" are (or should be) in charge of the  government. All of them. And since that's not feasible (yet), all current implementations use a system of more or less directly appointed delegates. So the way I understand it is: The more directly "the people" can influence the law of a country, the more democratic is that country.

And of course what you really want is that whoever is in charge of your country should be able to make good decisions. How you define "good" is of course another question all together. In my opinion "long-term happiness" is still a much better metric than "money spent" but that's not what I want to talk about here.

What "being able to make good decisions" definitely means is being able to understand complex problems. Because most problems nowadays are quite complex. And the way to achieve that of course is through education. Jeffersons put this more eloquently than me:

> I know no safe depository of the ultimate powers of the society but the people themselves. And if we think them not enlightened enough to exercise their control with a wholesome discretion, the remedy is not to take it from them but to inform their discretion by education.


## Educational Debt

My theory is this: Ignoring the mandate for education but still demanding that the people are in charge is essentially the same as ignoring the need to keep your codebase clean but demand to spit out new features every two weeks.

What we have created is an Educational Debt. Too many people lack the essential skills to make or even recognise good decisions. As a consequence, they don't vote with an understanding of the complex problems that have to tackled. Instead they let themselves be guided by emotions, believes and partisan solidarity.

And I'm not talking about reading or maths skills here or a knowledge or historic events. The skills that a democratic citizen needs and that I haven't seen on any curriculum yet are

- **being compassionate**
- **having a constructive discussion**
- **exercising critical thinking**
- **applying the scientific method**
- **avoiding cognitive biases**

Possible ways of teaching compassion include Virtual Reality, which literally lets you "walk in someone else's moccassins". Discussion, critical thinking and science is probably best tackled in schools although some paradigms will have to shift. Teachers need to stop that nonesense with a "single right answer", motivate student to challenge common believes and start realizing that *science* is really just ["a negotiation between the best you can do right now and the stuff that is out there"][kay]. For that it would probably be helpful to read and discuss actual studies and learn that discussions are not about being "right", but about collaborative discovery. To learn about cognitive biases I recommend to put [Thinking Fast and Slow] on the reading list.

So instead of fighting the ignorants and their followers, let's put our energy towards creating a better education for the next generation but also for the current ones. Let's rethink if curricula with arbitrary standardized learning achievements are really the best way to motivate people. Let's reconsider if stuffing people into groups based on their birth year is the best environment for them to learn. And let's find out if we can create something better that static, linear media to express and explore their ideas in.

> It is not education, but education of a certain kind that will serve us. And the current model of western, urban-centered, school-based education, which is so often more focused on turning children into corporate units rather than curious snd open-minded adults, will only lead us further down the wrong path. 
> -- David W. Orr

We need a new kind of education. And we need it soon.

[kay]: https://www.youtube.com/watch?v=N9c7_8Gp7gI
[Thinking Fast and Slow]: https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow