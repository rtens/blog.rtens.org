My opinion is probably more than a bit biased, but to me computers are incredible. Almost magical even. Like daemons from another sphere, all it takes is the right spell, and it will do your bidding (and like with these daemons, you have to be very careful which exact words you use). My favourite quote on that topic comes from [The Mythical Man-Month]:

> The programmer, like the poet, works only slightly removed from pure thought-stuff. He builds his castles in the air, from air, creating by exertion of the imagination. Few media of creation are so flexible, so easy to polish and rework [...] The magic of myth and legend has come true in our time. One types the correct incantation on a keyboard, and a display screen comes to life, showing things that never were nor could be.  
> -- Fred Brooks

Computers get this power through a property called *[Turing completeness]*, named after the probably most influential computer scientist to have ever lived. In his 1936 [paper], Turing proofed that you can construct a machine that can emulate any other conceivable machine. Or in less precise terms: a computer is not just a machine. It is *all* machines.

[The Mythical Man-Month]: https://en.wikipedia.org/wiki/The_Mythical_Man-Month
[Turing completeness]: https://en.wikipedia.org/wiki/Turing_completeness
[paper]: https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf


## Cutting the Wings

So we have these incredibly flexible machines, that can become any other machine in the blink of an eye, and we use them to emulate *static* appliances with a fixed set of actions. And because we call them *apps* and *features* we don't realize just how much we are limiting ourselves with this paradigm.

This point deserves its own essay and luckily Paul Chiusano [already wrote it][paul] in an excellent manner. So please head over and read his article, which not entirely coincidentally starts with the same Fred Brooks quote. It's a little on the wordy side but well worth the reading time. 

I mean it. Please. Read it.

One could argue that a limited, static user interface is easier to use and therefore superior even if it cripples the user. But the original designers of graphical user interfaces did not think so. [Matthias Müller-Prove][mprove] gives a very conclusive overview of the history and development of the GUI, from [Sketchpad] over the [Alto] to the [Macintosh].

Sketchpad is seen as the first graphical user interface and had for its time futuristic feats such as direct manipulation, constraint-based layouting as well as a powerful template system which was an inspiration for Smalltalk, the object-oriented programming language and user interface of the Xerox Alto. There were also no applications visible on one of the first consumer-oriented computers, the Apple Lisa, which adopted the "real office" metaphor of the Xerox Star, which lets the user manipulates *documents* in a WYSIWYG way. Double-clicking on a document opened in, dragging it into the paper bin deleted it, and a new document was created by cloning a template.

It was only the hardware limitation of the Macintosh that forced the interface designers to divert from this more natural document metaphor and settle for the concept of applications. With this metaphor, you needed not simply an empty document to write something, but a *writer* application.

> Why don’t we have the compound document model in use today? Because the Macintosh was a 128-kilobyte machine with a single disk drive. A user couldn’t possibly have more than one tool in the computer at any time because there wasn’t room. Since only one tool could be used with a document, then the tool might as well handle the opening and closing of that document.  
> -- Bruce Tognazzini argues in "Tog on Software Design"

And when computing resources became more abundant, software designers were too busy copying and extending existing user interaction models, to reconsider the decision against a more natural, more powerful document-centric model, made because of the limitation of outdated hardware.

[paul]: http://pchiusano.github.io/2013-05-22/future-of-software.html
[mprove]: http://www.mprove.de/
[Sketchpad]: http://www.mprove.de/diplom/text/3.1.2_sketchpad.html
[Alto]: http://www.mprove.de/diplom/text/3.1.5_xeroxalto.html
[Macintosh]: http://www.mprove.de/diplom/text/3.1.9_macintosh.html


## Solving the Problems

Today, personal computing is very far from what its inventors had envisioned. Instead of more or less generic objects that can easily be mixed and matched by the users to solve their problems, there is an "app" for every tiny itch. And instead of being able to adapt these solution to their own unique needs, users have to request and wait for new "features".

But not only does this scale terribly, it's also mathematically *impossible* to solve all the needs of every single user. If you manage to discover the actual needs of 80% of your total target group and then manage to build a solution that fits 80% of those needs, you are really good at your job. But you also only meet 64% of all requirements of all users. And that's for the optimistic case. More realistic numbers are probably 50% or 30%.

And things are getting rapidly worse as the Web and mobile platforms do their best to get rid of the last bastion of freedom and control - files. Venture-capital-driven companies with the-user-is-the-product business models are heavily incentivised to lock an always growing number of people into walled gardens and hinder information exchange with other systems as much as possible. The ensuing battle for users leads to almost every software product to become an inevitably bloated accumulation of ever more specialized features, diminishing the return on investment while mudding the user model with each new feature.

A prominent example of this trend is the seemingly ever increasing number of messaging services. While there was always a great number of such services, it used to be possible to use them all with a single client software. Services nowadays are closed-off silos entirely for business reasons, costing the autonomy and freedom of their users. Other symptoms are the [failure of Evernote][evernote] and [bloating of Trello][trello].

[evernote]: http://observer.com/2015/10/why-evernote-is-struggling-and-how-technology-is-moving-in-a-new-direction/
[trello]: http://pchiusano.github.io/2016-10-13/view-inspired.html


## Returning the Power

The only scalable solution is to give users the means to solve their own, unique problems. To ["treat the user as a problem solver, not merely as a process follower"][naked] as Richard Pawson puts it in his book on *Naked Objects*.

Instead of bloated silos, software should be a collection of coherent libraries that can be easily combined and modified. Business models could be based on use-based micro-payments which are paid by the end user, not by the direct service consumer. Users should be able to solve simple problems in a simple way by combining a couple of small concise libraries. In this regard, messaging and picture sharing are definitely simple problems.

Lucky for me, even such a world would not eradicate the need for professional software developers since complex problems will continue to require complex, custom-made solutions. But the proportion of time spent on essential tasks like understanding the problem, deducing a model and testing the solution would hopefully increase compared to time spent on insignificant implementation details. So the profession would be better described as *modeller* or *designer* than *coder*.

[naked]: http://www.nakedobjects.org/book/section1.html


## Managing the Tasks

I would like to use my fight against procrastination as an example. My whole life I was suffering from low self-discipline and often times found myself wasting days and weeks that I should have spent on important tasks. As a consequence, many opportunities were missed, many goals unreachable and my freelancing work always a little more stressful than necessary.

I've read every self-help book I could get my hands on and tried every productivity application I could find but could not benefit from any of them for more than a couple of weeks. Ultimately, my bad habits always caught up with me. I even started to come up with my own schemes to mitigate my low discipline. But nothing seemed to work.

It was only when I discovered Tim Urban's [thoughts on procrastination][wbw] that I started to form a useful model of my mental process and its weaknesses. And since I'm in the lucky position of knowing some of the spells to make the daemons in the magical machine do my bidding, I could express this model in software and test it on myself. It still took me three iterations but in the end I found a solution that has pretty much changed my life during the last couple of months.

Excited about my breakthrough, I was keen to share my approach with people I know are also struggling with self organisation, only to discover that my model couldn't help them since it doesn't fit their particular situations. It seems some personal problems can only be solved by the persons themselves. As software designers, our job should be to give them the power to do so, not to take it away.

[wbw]: http://waitbutwhy.com/2013/10/why-procrastinators-procrastinate.html