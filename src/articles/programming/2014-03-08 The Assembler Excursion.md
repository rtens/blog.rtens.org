Last week we went oldschool at our monthly Coding Dojo and programmed in Assembler for the 6502 microprocessor thanks to an awesome tutorial by [tba] that made me wanna try it out myself. Turns out it's a lot harder than we thought and we achieved little more during the whole session than painting the background blue. But it got me curious and I ended up knee-deep in Assembler.

## The Coding Dojo ##

Last August, a [colleague] of mine told me about this thing called [Coding Dojo] and I since we couldn't find any active ones in Berlin, we started to organize one montly at the [ResearchGate] offices. The idea is to get together with other coders (aka hackers/developers/programmers) and work on a programming challenge together. We usually pair up but other forms are possible. It's always great fun so if you are curious drop by. You can find the all the infos on [github].

By the way: in the meatime I found two other Coding Dojos or dojo-like meetups: [agile developers] and [softwarekammer]

There is a bunch of small, well-defined challenges called [Katas] which are a good starting point. A Kata is an excersice which is meant to be repeated over and over. In the martial arts, it's a movement that you repeat until it becomes second nature so you don't have to think about it during battle and concentrate on more important things like staying alive. Just like you don't have to think about all the tiny movements involved in changing gears as an experienced driver.

So sometimes we do a kata but sometimes we do other tings like a simple Regular Expression matcher or drawing patterns on a Christmas tree via HTTP. And last week we tried to programm in Assembler for the [6502] micropocessor inspired by an awesome [tutorial] I found a couple of weeks before and made me wanna try it out myself.


## The Machine Code ##

What I like most about prgramming is how I can make my imagination become reality. I imagine that this must be even more thrilling for architects that can wallk and touch their brain childs but being able to push all these pixels around at will is already pretty cool for me. Sometimes it feels like magic. Especially with all the layers of abstraction, the connection between the keys I press and the pixels that light up is all but transparent.

So ever since I started programming I was fascinated with Machine Code. It's where the magic happens, where words become reality. It's that line between ideas and pysics. Every line of code I write, no matter in which language is eventually distilled into a bunch of machine code instructions before it becomes electrical signals that contol millions of tiny lamps just to trick my brain into thinking I'm looking at a small kitten rolling on a floor. If you are not blown out of your mind by that you haven't really thought about it yet.

So how does machine code look like? Well for example like this:

		0010 1101 1001
		0110 1110 1111
		0100 0010 1101
		
These numbers can be translated into a slightly more human-readable form called Assembler:

		LDA $01
		ADC #$02
		STA $03
		
And if you wanted to translate these lines into english you might get something like

		Look up the number in the memory cell number one and remember it
		Add the number two to that number and remember the result
		Put the resulting number into the memory cell number three


## The Micro Processor ##

The machine in Machine Code is the processor. When I say `Add the number to that number you remembered and remember the result`, the processor is the one that actually does that. Describing how exactly it does that would definitely blow up this article but let's just say that these zeros and ones above correspond to off and on positions of many many switches. And like in a big building, if you set the right light switches at the right time to the right positions, you can suddenly do things like play pong.

I have this idea of building a "Water Computer" that uses water instead of electrons. It would be huge and slow and possibly quite wet but it would be perfect to demonstrate how a processor works because everythings would be so slow that you could actually watch it happening. Of course any liquid would do so in the future I might call it "Beer Computer" for marketing reasons.

Anyway, like my hypothetical water processor, these processors used to be huge and expensive but eventually became tiny (hence micro) and cheap enough so everybody could have one. Born was the personal computer. Nowadays we are surrounded by micro processors. They are in out computers (duh), cars, blenders, dish washers, everywhere. They are usually black and square and flat and get really hot if you watch a lot of cat videos.


## The Emulator ##

The great thing about software is that you can build anything with it. And if I say anything of course I mean anything that can be built with software. But that's pretty much everything. Even a computer. A computer that is built with software and not with silicon and gold and aluminum and stuff is called an Emulator. So you can write a programm that behaves just like a certain processor. Such an emulator has the big advantage that you can very easily look inside it. This is very hard with a physical micro processor since it's so tiny and everything happens so fast.

For the Coding Dojo, we mostly used the emulator on [6502.org] which works well but has limited debugging abilities and also rather slow. So I went looking for an emulator that is not written in JavaScript but allows the same configuration as the one in the tutorial - with display, random number generator and key input 

Since I couldn't find one within ten minutes, I did what every sane software developer would do - I wrote my one. [You can find the result here][emulator]. And although the value for humanity of this exercise is questionable, I once again felt why I'm such a big fan of [reinventing the wheel]. By re-building the whole processor I got to know it a lot better than by writing code for it and it was a lot more fun than reading a 500-pages technical book about it. And probably took the same time (I'm a slow reader).


## The Sphere ##

When we sat down to write some Assembler at the Coding Dojo and started wondering, what our pogramm should actually do, Rob had the idea to build a ray tracer for a sphere. In other words, to paint a circle. I loved it because it gave me a good excuse to do some actual math. And I was suprised by how much I've forgotten in a couple of years. But an hour later we had roughly implemented the algorithm. In C.

Translating the C program into Assembler is trivial of course. Or so we thought. We thought wrong of course. In the remaining hour we achieved little more than paining the background. In blue.


[colleague]: tba
[Coding Dojo]: tba
[Katas]: tba
[github]: http://github.com/researchate/CodingDojo
[agile developers]: tba
[softwarekammer]: tba
[6502]: tba
[6502.org]: tba
[emulator]: tba
[reinventing the wheel]: tba