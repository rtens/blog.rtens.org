Status: draft

One of the most inspiring texts that I've ever read is Bret Victor's [What can a technologist do about climate change][climateChange]. Before reading it, I was always a bit ashamed of not spending my energy directly on this most urgent and extensive problem of humanity. Instead of working on alternative energy sources, storage or distribution, I was solving comparatively small and trivial problems.

Victor's words motivated me to think about how I can use my knowledge, skills and passion to help mitigating the global climate change, even if somewhat indirectly. I determined that the field I'm most knowledgeable in is computing and software engineering and my skills to be system analysis, software design and teaching. And the thing I'm most passionate about is this idea of a computing model that has been floating around in my head for several years but that I never dared to take seriously, apart from writing my [diploma thesis][thesis] about it.

So earlier this year, I used a two-week stay in a Buddhist monastery to think hard about what it is that drives me, why I couldn't get that computing platform idea out of my head and what the root problem might be that I want to solve with it. The result is a [manifesto] and the conviction that my mission should be **to augment the collective intelligence of humanity by Increasing _Software Literacy_**.

[climateChange]: http://worrydream.com/ClimateChange/
[thesis]: https://github.com/zells/thesis/blob/master/memoria/out/thesis.pdf
[manifesto]: https://github.com/zells/core/blob/master/manifesto.md


## Learn to Code

When I started looking for others who might share this mission, I found dozens of on-line as well as off-line courses that all make a very similar promise: to transform you into a software developer in a couple of weeks or months. Of many I've heard before but never really had a closer look. So I dug into a couple of them and was surprised to realize that something didn't feel right. There was something about their approach that irked me but I couldn't put my finger on it.

In a broad generalization, the usual process was that you choose a programming language and then do guided tasks of increasing difficulty that are automatically evaluated. The tasks were of the kind that a recruiter might use to asses an applicant's familiarity with a technology. Some courses have an instant gratification system that rewards you with batches for reaching certain levels.

Having written *Software Literacy* on my banner I was frustrated that I couldn't completely get behind this *Learn to Code* movement and even more so that I couldn't argue what bothered me about these courses. They just seemed to be focusing on the wrong thing.


## Learn to Bike

And once again it was Alan Kay describing in a [talk about CS eduction][talk] exactly what I was feeling. But once again I did not understand his message right away and I didn't connect the dots until I replied to a [comment on HackerNews][hackernews] that was part of the feedback to said manifesto.

I never thought about how different the experience of learning how to ride a bicycle must be for children nowadays compared to how I learned it. Just suddenly these tiny balance bikes seemed to be very much in vogue and I remember being surprised by how young their riders sometimes were and how well they handled it. But I just though "neat" and didn't see the didactic implications. Of course somebody would somehow have to learn to bike twice in their life to really know, but the difference must be enormous.
 
This seems to be a very intuitive and common approach when teaching something to children: Take the adult version of something, and change something so it's less likely to fail. The problem is that many times, this change destroys the essence of what you want to teach. On a bike with training wheels, it's impossible to learn the one skill you need for riding an actual bike: balancing.

I'm convinced that the opposite approach is way more effective and less frustrating. On balancing bikes, children learn the *essentials* - balancing, leaning into curves - first. It's still safe since their feet are always close to the ground. Once they've mastered these skills and feel confident, they get the pedals. These add some new concepts and require some new skills but nothing too demanding. Pedals are *not* an essential part of bikes but increase its efficiency. That much even that Steve Jobs likened computers to ["bicycle for our minds"][efficiency].

[talk]: https://youtu.be/N9c7_8Gp7gI?t=51
[hackernews]: https://news.ycombinator.com/item?id=13107281
[efficiency]: http://www.bikeboom.info/efficiency/


## Don't learn to code

Code is **not** essential for programming. Code plays the role of the pedals. It gives you a very effcient way of describing structure and behaviour and specific programming languages are suited differently well for formulating thoughts of a specific kind but all that does is increase your efficiency.

And this is exactly what has been bothering me about these programming courses. They all start and focus on the code. On a specific language even most of the times. They construct a small, well defined universe with little exercises that keep the learner from failing. But it's the same mistake as putting training wheels on a bike. The learner never gets to actually feel the ground and while it might happen sporadically, this approach impedes learning the *essential* skills of programming.

I have no definite list of what these essentials are. But my guess woul be 

- modelling
- software design
- debugging
- understanding scales
- managing complexity
- dealing with uncertanty

None of these require a student to *write code* and most of them not even to read it.


## Learn to Program

So instead of teaching to *code*, I would love to see a programming course that actually teaches to *program*, preferably without touching code at all but still providing the student tools to build running, living, buggy software. [Etoys], [Scratch] and even spreadsheets could be used for this purpose. These courses probably already exist and just spend less money on marketing.

A simple - albeit subjective - metric to know if a "balancing bike" approach to programming works is how the students feel when released into the "wild" and with how much confidence you can tell if they're ready. They should even have a good feeling for that themselves. The feeling would probably be something like "this feels too slow" as children have when they outgrow their balancing bikes.

If you only ever bike with training wheels, you are never really ready to take them off since you don't actually know how to bike. I remember my first time without them. It was a long-anticipated - but acually kinds arbitrarily chosen - moment. I felt ready and happy. My dad was pushing me to gain momentum and when he released me, it felt like flying for a moment. And then I landed face-first on the ground.

I imagine that students completing one of these courses feel the same way. You did all the exercises, collected all the badges, you feel ready and omniscient. How frustrating must it feel to realize you really only know very little. I know that people learning TDD the "training wheels" way feel like this beause I have taught them that way and saw their frustration when they couldn't apply their new skills to their real-world problems. An [article on testdouble][tdd] describes this situation very nicely although I wouldn't agree with their conclusion.

[Etoys]: http://squeakland.org/
[Scratch]: https://scratch.mit.edu/
[tdd]: http://blog.testdouble.com/posts/2014-01-25-the-failures-of-intro-to-tdd.html


## Learn to Fly

So whatever you're teaching, don't just put training wheels on your own tools but create new, simpler tools that concentrate on the essentials and let your students learn to fly by touching the ground every once in a while. And accept that they will have to fall a couple of times so give them an environment where hitting the ground is not too painful.

And whatever you're learning, find out what exactly the masters of that skill spend most of their time with. This is probably something important. And with some luck, it's something essential that let's you fly.