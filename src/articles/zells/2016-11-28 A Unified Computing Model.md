In 1963, while working at the Advanced Research Project Agency, J.C.R. Licklider wrote in [his Memorandum][memo] to the *Members and Affiliates of the Intergalatic Computer Network*:

> At this extreme, the problem is essentially the one discussed by science fiction writers: "how do you get communications started among totally uncorrelated "sapient" beings?"

Alan Kay [referred to this][kay1] as the *communicating with aliens problem*. Licklider continues:

> But, I should not like to make an extreme assumption about the uncorrelatedness. (I am willing to make an extreme assumption about the sapience.)

Licklider's "Intergalatic Computer Network" became the "ARPANET" which in turn became the "Internet", which quite well fulfills his vision of connecting every single person on the planet.

In the context of the Internet, the "aliens" are two independently developed computer programs and the problem is how to get them talking to each other. Since Licklider allows us to soften the *uncorrelatedness* requirement, we can assume that there exists a common language language that both services know how to speak, albeit it probably won't be the native language of either. What should this language look like?

[memo]: http://worrydream.com/refs/Licklider-IntergalacticNetwork.pdf
[kay1]: https://vimeo.com/22463791

 
## Current State

One could argue that the "language of the Internet" is the Internet Protocol stack (TCP/IP), which allows one program on the internet to talk to any other program. But it only specifies *how* they can talk to each other, not *what* they can talk about or how to discover what the other one *means*.

It's analogous to the air, lungs and ears. Given enough those, I can certainly *speak* to any other human on the planet that is close by. And they can probably *hear* me, but that doesn't mean they *understand* me or that I can *talk* with them. This is the state that the IP stack leaves us with.

The most wide-spread *meaningful* language of the internet is the WorldWideWeb. It specifies how things can be addressed (with URIs/URLs) and how these things can present themselves (with HTML). It provides meaning by specifying *verbs* of what you can do with these resources (such as "post" and "get"). And most importantly it defines how communication is done (with HTTP).

The result is a *computing model* that turned out to be quite useful for accessing static documents but really not a good fit for doing anything more interesting. And over the last decades many million of man-hours have been poured into mitigating its design flaws.

I very much agree with Alan Kay's notion that "HTML has gone back to the dark ages and is one of the worst ideas since MS-DOS", as he said in [one of his most iconic talks in 1997][kay2]. I also remember him saying once that the web-browser "does too much and not enough". I think what he means is that there are way too many primitives in HTML which all have to be interpreted (doing too much) but it's not at all extensible (not enough). The second critique point also goes for HTTP which has a fixed number of *verbs* which just don't fit in many situations. But the worst design flaw is in HTTP, which assumes that all communication is initiated by the client and no state is preserved in the server.

How could this be done better?

[kay2]: https://youtu.be/oKg1hTOQXoY?t=1421


## Proposal

I propose to design a protocol based on a computing model that is an abstraction of all existing and conceivable models and is thus compatible with all and any of them. I would like to call this model [Qi] which means "breath" and "air" but also "energy flow".

This model could be used as a meta-language to create a meaningful but extensible vocabulary. Two uncorrelated services could use this model to discover each others capabilities and use the vocabulary to transfer meaning. The model would also be used to safely transfer not only data between services but also dynamic behaviour (code of any kind, even binary programs) without the need to manually translate either.

I believe this model could play the role of a ["universal interface language"][kay3] and make communicating with aliens possible.

[Qi]: https://en.wikipedia.org/wiki/Qi
[kay3]: https://youtu.be/oKg1hTOQXoY?t=3085 


## Model

You can find an up-to-date description of the model [here][model].

[model]: https://github.com/zells/core/blob/master/model.md


## Discussion

The purpose of this document is to invite discussion by providing a precise but readable description of a proposed unified computing model. If you find possible design flaws or contradictions, or if you have any other feedback, e.g. regarding applicability or plausibility, please don't hesitate to [let me know][contact]. You'll find a proof-of-concept implementation [on github][qi].

[contact]: http://rtens.org#contact
[qi]: https://github.com/zells/qi