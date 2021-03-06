Last week we went oldschool at our monthly [Coding Dojo] and programmed in Assembler for the 6502 microprocessor thanks to an awesome [tutorial] by [Nick Morgan] that made me wanna try it out myself. Turned out it's a lot harder than we thought and we achieved little more during the whole session than painting the background blue. But it got me curious and I ended up knee-deep in Assembler.

[Coding Dojo]: https://github.com/researchgate/CodingDojo
[tutorial]: http://skilldrick.github.io/easy6502/
[Nick Morgan]: https://twitter.com/skilldrick

## The Coding Dojo ##

Last August, a [colleague] of mine told me about this thing called [Coding Dojo] and I since we couldn't find any active ones in Berlin, we started to organize our own at the [ResearchGate] offices. The idea is to get together with other coders (aka hackers/developers/programmers) and work on a programming challenge together in order to practice and learn from eachother. We usually pair up but other forms are possible. It's always great fun so if you are curious drop by. You can find the all the infos on [github].

By the way: in the meatime I found two other Coding Dojos or dojo-like meetups: [agile developers] and [softwarekammer]

There is a bunch of small, well-defined challenges called [Katas] which are a good starting point. A Kata is an excersice which is meant to be repeated over and over. In the martial arts, it's a movement that you repeat until it becomes second nature so you don't have to think about it during battle and concentrate on more important things like staying alive. Just like you don't have to think about all the tiny movements involved in changing gears as an experienced driver.

So sometimes we do a Kata at the Dojo but sometimes we do other tings like a simple Regular Expression matcher or drawing patterns on a Christmas tree via HTTP. And since this really nice [tutorial] inspired me to try it out myself, last week we did some Assembler for the [6502] micropocessor.

[colleague]: http://martin.holzhauer.eu/
[Coding Dojo]: http://codingdojo.org/
[ResearchGate]: http://researchgate.net
[Katas]: http://codingdojo.org/cgi-bin/index.pl?KataCatalogue
[github]: http://github.com/researchate/CodingDojo
[agile developers]: http://www.meetup.com/Agile-Developers-Berlin/
[softwarekammer]: http://www.softwerkskammer.org/
[tutorial]: http://skilldrick.github.io/easy6502/
[6502]: http://en.wikipedia.org/wiki/MOS_Technology_6502


## The Machine Code ##

What I like most about prgramming is how it turns my thoughts into reality. I imagine that this must be even more thrilling for architects that can wallk and touch their brain childs but being able to push all these pixels around at will is already pretty cool for me. Magical even. But with all the layers of abstraction, the connection between the keys I press and the pixels that light up is all but transparent.

So ever since I started programming I was fascinated with Machine Code. It's where the magic happens, where words become reality. It's that line between ideas and physics. Every line of code I write, no matter in which language is eventually distilled into a bunch of machine instructions before it becomes electrical signals that contol millions of tiny lamps just to trick my brain into thinking I'm looking at a small kitten rolling on a floor. If you are not blown out of your mind by that you haven't really thought about it yet.

So how does machine code look like? Well for example like this:

	1010 0101 0000 0001 
	0110 1001 0000 0010 
	1000 0101 0000 0011
		
These numbers can be translated into a slightly more human-readable form called Assembler:

	:::perl
	LDA $01
	ADC #$02
	STA $03
		
And if you wanted to translate these lines into english you might get something like

	Look up the number in the memory cell number one and remember it
	Add the number two to that number and remember the result
	Put the resulting number into the memory cell number three


## The Micro Processor ##

The *machine* in Machine Code is the processor. When I say "Add the number to that number you remembered and remember the result", the processor is the one that actually does that. Describing how exactly that works would definitely blow up this article but let's just say that these zeros and ones above correspond to off and on positions of many many switches. And like in a big building, if you set the right light switches at the right time to the right positions, you can suddenly do things like play pong.

I have this idea of building a *Water Computer* that uses water instead of electrons. It would be huge and slow and possibly quite wet but it would be perfect to demonstrate how a processor works because everythings would be so slow that you could actually watch it happening. Of course any liquid would do so in the future I might call it *Beer Computer* for marketing reasons.

Anyway, like my hypothetical water processor, these processors used to be huge and expensive but eventually became tiny (hence micro) and cheap enough so everybody could have one. Born was the personal computer. Nowadays we are surrounded by micro processors. They are in out computers (duh), cars, blenders, dish washers, everywhere. They are usually black and square and flat and get really hot if you watch a lot of cat videos.


## The Emulator ##

The great thing about software is that you can build anything with it. Even a computer. A computer built from software instead of silicon, gold, aluminum and stuff is called an *emulator*. So you can write a programm that behaves just like a certain processor. Such an emulator has the big advantage that you can very easily look inside it. This is very hard with a physical micro processor since it's so tiny and everything happens so fast.

For the Coding Dojo, we mostly used the emulator on [6502asm.com] which works well but has limited debugging abilities and is also rather slow. So I went looking for an emulator that is not written in JavaScript but allows the same configuration as the one in the tutorial - with display, random number generator and key input 

Since I couldn't find one within ten minutes, I did what every sane software developer would do - I wrote my one. You can find the result [here][emulator]. And although the value for humanity of this exercise is questionable, I once again felt why I'm such a big fan of reinventing the wheel. By re-building the whole processor I got to know it a lot better than by using it and it was a lot more fun than reading a 500-pages technical book. And probably took the same time (I'm a slow reader).

[6502asm.com]: http://www.6502asm.com/
[emulator]: https://github.com/rtens/6502	


## The Sphere ##

When we sat down to write some Assembler at the Coding Dojo and started wondering, what our pogramm should actually do, Rob had the idea to build a ray tracer for a sphere. In other words, to paint a circle. I loved it because it gave me a good excuse to do some actual math and it sounds cool. I was suprised by how much math I've forgotten in a couple of years. But an hour later we had roughly implemented the ray tracing algorithm. In C.

Translating the C program into Assembler is trivial of course. Or so we thought. We thought wrong. In the remaining hour we achieved little more than paining the background. In blue. But we sure had a good time doing so.