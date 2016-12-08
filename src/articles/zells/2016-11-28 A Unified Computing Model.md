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


## Properties

The model consists of *composable*, *dynamic*, *concurrent*, *abstractable* and *distributed* objects, called *cells*. The semantics of the model are defined by these properties.


### Composable

A cell can contain any number of other cells as children. Each *child* has name that is unique amongst its siblings. 

```text
Child := <symbol>+
```

This forms a tree where each cell is a node and can therefore be addressed by a *path* containing the *names* of each child cell.
   
```text
Path := Name+
Name := Child
```

To move up in the tree, a path can also contain a reference to the *parent* of a cell as well as the *root* of the tree.

```text
Name := ..|<parent>|<root>
```
   
#### Example
    
Given the following tree structure

```text
      °
     / \
    A   B
    |   |
    C   D
```

The canonical path of `D` is `°.B.D` where `°` denotes the root and `.` separates two names. A path from `C` to `D` would be `^.^.B.D` where `^` denotes the parent.



### Dynamic

A cell may have dynamic behaviour in the form of a *reaction* which is executed every time the cell receives a *message*. The message is always a single cell, referenced by a path relative to the sender.

```text
Message := Path
```

A reaction can cause any number of *message sends* which define the paths of a *receiver* cell and of the message to be sent.

```text
Reaction := MessageSend*
MessageSend := Receiver Message
Receiver := Path
```

#### Example

Given the following cell structure.

```text
       °
     / | \  
    A  B  C
```

If the reaction of `A` is to send `B` to `C` (written as `<receiver> <message>`),

```text
°.C °.B
```

then every time `A` receives any message, it will cause `°.B` to be sent to `°.C`.



### Concurrent

All messages of a reaction are sent *concurrently*. Furthermore, each message is sent by a *messenger* which will keep trying to deliver the message until it is received or the messenger decides it's not deliverable. This way, data flow can be synchronized without requiring a fixed order of execution. Therefore messages may be sent to cells before they exist.

#### Example

When calculating `2 * 3 + 4 * 5`, the summation has to wait for both factors to complete calculation. The following diagram illustrates the case where the calculation of `2*3` is delayed. 

```text
a = 2*3       ##
b = 4*5  ##
c = a+b  ~~~~~~~###
         ----------->t
```

The summation waits (denoted by `~`) until the calculation of both factors is completed.



### Abstractable

Every cell has a *stem* cell from which it inherits its reaction and all children. Each inherited child and the reaction can be replaced by the *specialized* cell. In order to send a message to an overwritten cell or execute and overwritten reaction, a path may contain names referring to the *stem* of a cell.

```text
Name := ..|<stem>
```

#### Example

Given a cell `A` with a child `C`. If a cell `B` has `A` as stem, it inherits `C` (denoted by lower-case `c`). 
        
```text
    A<--B
    |   ¦
    C   c
```
      
If a message is sent to `B.C`, the reaction of `A.C` is executed in the *context* of `B.C` which means all paths will be resolved relative to `B.C`. 

If `A.C` has a child `D`, it is inherited as well.
    
```text
    A<--B
    |   ¦
    C   c
    |   ¦
    D   d
```



### Distributed

A cell can be distributed over multiple processes and machines. It is connected to a *peer* by sending it a *join* signal with information about how the peer can be reached. If a cell can't deliver a message, it will forward it to each of its peers in turn by sending them a *deliver* signal. If a peer can't deliver the message either, it responds with *failed*, otherwise with *received*. A peer is disconnected from a cell by sending a *leave* signal.

To be able to avoid endlessly forwarding messages in circular peer connections, a *deliver* signal contains a globally unique identifier. Messages are guaranteed to be delivered at most once, but there are no guarantees regarding the order of messages.

#### Example

Given a cell `A` in the process with the ID `111`.

```text
      111
    +-----+
    |     |
    |  A  |
    |     |
    +-----+
```

If a new process (with the ID `222`) is created that contains also cell `A`, the signal `join A 222` is sent to process `111`. This adds a unidirectional connection from the cell in `111` to its peer int `222`.

```text
      111        222
    +-----+    +-----+
    |     |    |     |
    |  A~~~~~~~~~>A  |
    |     |    |     |
    +-----+    +-----+
```


## Discussion

The purpose of this document is to invite discussion by providing a precise but readable description of a proposed unified computing model. If you find possible design flaws or contradictions, or if you have any other feedback, e.g. regarding applicability or plausibility, please don't hesitate to [let me know][contact]. You'll find a reference implementation and proof of concept [on github][qi].

[contact]: http://rtens.org#contact
[qi]: https://github.com/zells/qi