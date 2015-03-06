Status: draft

I just came across [Chris Granger][chris]'s essay ["Coding is not the new literacy"][essay] and although I strongly agree with his overall notion, I disagree with his premise "Being literate isn't simply a matter of being able to put words on the page, it's solidifying our thoughts such that they can be written." and since this is an important topic for me I didn't want to restrict my thoughts to 140 characters.

[chris]: http://twitter.com/ibdknox
[essay]: http://www.chris-granger.com/2015/01/26/coding-is-not-the-new-literacy/


## Coding *is* Literacy

As far I understood it, Chris' main point is that "Coding is not the fundamental skill", modelling is. He compares it to writing by stating that "Being literate isn't simply a matter of being able to put words on the page". And that's where I disagree. Being *literate* means exactly that: "being able to put words [from your head] on the page". It also means doing the reverse and the meaning has somewhat expanded during the last century but it also means exactly that.

In fact I would like to use the definition that [Wikipedia] claims the term's meaning has been expanded to.

	*The ability to [...] understand and use the dominant symbol systems of a culture.*

So it's really about about decoding (understand) and encoding (use) thoughts with symbols. Hence coding *is* a form of literacy. It's just not well suited for most kind of thoughts and I think that's where Chris' pain is coming from. But maybe I'm projecting since this is also my pain. But more on that later.	
	
[Wikipedia]: http://en.wikipedia.org/wiki/Literacy


## Literacy and Thinking

The second part of his premise is that "Being literate [is] solidifying our thoughts such that they can be written." Since as soon as you have solidified your thoughts sufficiently to speak them, you can write them. The thought itself doesn't gain anything from being written down. It's the putting it in words that makes a difference.

Writing down my thoughts is a strategy I use myself quite often to clarify them. This is actually a main reasons why I'm writing this peace. But I could also just tell them to my [rubber duck] instead.

I don't think, writing makes me better at thinking. Having to put my thought in words does. But not much. If there is one thing that really challenges and improves my thinking skills it's good discussions with people I respect. There is no immediate need for literacy to do that though. Two comfortable chairs in a quite room is more than enough.

But still I'm not having this particular discussion over a cup of green tea in my favourite coffee house - although I would love to. Because I am literate and fortunate enough to own a computer with internet access, I was able to read Chris' essay. This is the value of literacy. Being able to have discussions without the limits of time and space. This way I can acquire the thoughts of Chris just as I can acquire the thoughts of Aristotiles. And while it's highly improbable that I ever share a tea with the former, it's impossible with the latter. And still he can influences the way we think about the world today.

And it's reading new ideas that challenges by own ideas and make me think about them and ultimately write them down. So it's the dispute, not the writing that (hopefully) improves my thinking skills. But if I had to choose between able to read or able to write, I'd choose reading without hesitating. 

[rubber duck]: http://en.wikipedia.org/wiki/Rubber_duck_debugging


## Modelling is Key

What I completely and utterly agree with (and it turns out, my good friend and colleague [Robert Jenke] as well) is that **modelling is the fundamental skill**. And to build a model is necessary in order to put them in software. Just like formalising a thought is necessary before you can write it down. But I have to disagree with "Modelling is the new literacy". Being able to externalizing your mental models using software, that's literacy.

It's not an coincidence that Chris mentions Alan Kay, the guy who got me excited about modelling in the first place. At this point I would like to urge every programmer to absorb as much of Alan's thoughts as possible. Like him and Chris, I strongly believe that being able to play around (aka experiment) with models is probably the best way of discovering and learning complex ideas and this is exactly what Alan and others tried to do with computers.

This was decades ago. But still, ["the computer revolution hasn't happened yet."][oopsla97] Why? Because we are still using computers as better paper and pens. A lot more powerful and interconnected paper and pens that has changed the way we access and distribute information but not what *kind* of information. The single most distinguishing things that computers can do that paper can't is to externalise dynamic models of our thoughts. But yet only a tiny part of humans use the capabilities or even know how to use them.

I really want to make this clear: being able to write down your thoughts not as static words, but as dynamic (breathing) software is fundamentally different and exponentially more powerful. It's not only externalizing thoughts, but *thinking*. Or in Chris' words:

	*To put it simply, the next great advance in human ability comes from being able to externalize the mental models we spend our entire lives creating.*
	
The analogy to writing words is quite compelling. Just like writing down thoughts forces you to put them into words and thus clarify them, encoding a dynamic model forces you to think about it on a whole different level. A big part of my job as a software engineer is picking the brains of so-called *domain experts*. People who usually know very well how a something works, but most times this knowledge is implicit. My job is then to make it explicit enough to be able to encode it in the programming language of my choice.

This means my goal is to put a part of the mind of this person into a machine. If done well, the machine can then do the thinking for the person. Only a *lot* faster. This might sound scary to some but it's what software engineers have been doing ever since the first machine instruction was executed.

[Robert Jenke]: https://twitter.com/rjenke/status/573794551888015360
[oopsla97]: https://www.youtube.com/watch?v=oKg1hTOQXoY


## The Problem with Programming Languages

Chris seems to ignore that humanity is already "able to externalize the mental models" - through coding. There are hundreds and thousands of programming languages out there. They are just not very approachable, or easy to learn. It's like if the only "language" we would have to write down our thoughts in was mathematical notation. It's a great notation for a whole category of thoughts but it's just a little too complex to be adapted by the majority of people. Sure you can describe a circle as `(x-a)² + (y-b)² = r²` but usually it's just a lot easier to write "circle" or even draw a circle. It might not be an *exact* circle, but usually that's not a problem.

And most programming languages is to dynamic models what mathematical notation is to thoughts. They are powerful tools but just way to complex. I regularly attend the local [CoderDojo] where me and other *mentors* are trying to teach young people aged 5-15 how to program. Now it's really when you're sitting down with a ten year old that you realize how incredibly complex these languages really are. And the sad thing is that this complexity is incidental. It's a side product. It's not necessary. But it keeps us from using them.

The answer to "How do I make a rectangle with text in it and when you click on it, it becomes red?" should not be "This bunch of HTML + CSS + JS". Just like you should not need to know about Pythagoras' theorem to be able to draw a circle. All you should need is a pen and a surface to write on and your personal *idea* of a circle. We are still using languages that make it easy for the computer, instead we need to focus on making it easy for the human.

Of course a lot of people are doing exactly that. Making it easy for humans. That's why Excel is so widely used to build models. Because it's (relatively) simple and you can "touch" it and play around with it. And it's what Chris Granger and his associates are working on as well with [Light Table] and the recently announced *eve* project which sounds like Excel on steroids and I'm looking forward to hear more about. But I'm afraid that like Excel, it will be somewhat limited and only work well for a certain class of models.

[CoderDojo]: https://coderdojo.com/
[Light Table]: http://lighttable.com/


## So what Now?

It's always easier to criticise existing solutions than to come up with a better one. So I bow in front of everybody who is trying and doing something about it. I hope that some day I will join that group as well. Until then let me describe what my ideal programming environment would look like.

There is actually one piece of software that comes remarkably close: [Etoys]. And again it's no coincidence that it's designed for children and by Alan Kay. In Etoys, you can create objects by drawing them and you can give them behaviour by using tile-based programming. So it's almost trivial to "remote" control a virtual car or make the car follow a track automatically. But you can also do complex things like the Etoys environment itself since the underlying platform, Smalltalk, can be reached from anywhere.

So my ideal programming environment would use a user interface similar to Etoys (Maybe without tile-based programming or at least not the default option) but completely based on distributed, concurrent, composable and abstractable entities. I call them *zells* and wrote about them in my [Diploma Thesis]. The whole system would consist of nothing but these *zells* in a single, global address space (for easy sharing and publishing) and the only instruction would be "send *zell* to *zell* as message".

Re-usage is an important principle in software engineering but I agree with Chris that "the idea that we can reuse components without having to change them [...] has caused us more harm than good." Components need to be malleable so we can use them as a starting point but adjust them to our specific needs. We can not expect the creator of a software to account for all possible usages of his component. So if a peace of software is not exactly doing what you want it to do, you can change it. But that requires literacy. We need to be able to read and write software.

It almost stroke me as odd that when it comes to text, there has almost been a lot more reading than writing. But in the software world it seems to be the opposite. My ideal programming environment would allow us to have discussions using models. Somebody could implement a model of how he thinks a part of the society works and I could change his model to incorporate my view of the world or argue against it with a completely different model. The difference is that we wouldn't have to explain our thoughts to each other and hope that the other one understands our mental model. Instead we could send each other our mental models and experiment with the thinking of other people, not limited by space and time. We could make predictions and verify the correctness of the models. Build upon them and improve them. We could do real science and thus step by step understand the world a bit better.

This would be a computer revolution.

[Etoys]: http://www.squeakland.org/
[Diploma Thesis]: https://www.researchgate.net/publication/50841568_Design_and_implementation_of_a_distributed_software_platform_based_on_asynchronous_messages