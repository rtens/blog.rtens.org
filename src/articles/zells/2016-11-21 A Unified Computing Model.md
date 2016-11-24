status: draft

In 1963, while working at the Advanced Research Project Agency, J.C.R. Licklider wrote in his [Memorandum to the *Members and Affiliates of the Intergalatic Computer Network*][memo]:

> At this extreme, the problem is essentially the one discussed by science fiction writers: "how do you get communications started among totally uncorrelated "sapient" beings?"

[Alan Kay referred to this][kay1] as the *communicating with aliens problem*. Licklider continues:

> But, I should not like to make an extreme assumption about the uncorrelatedness. (I am willing to make an extreme assumption about the sapience.)

Licklider's "Intergalatic Computer Network" became the "ARPANET" which in turn became the "Internet", which quite well fulfills his vision of connecting every single person on the planet.

In the context of the Internet, the "aliens" are two independently developed computer programs and the problem is how to get them talking to each other. Since Licklider allows us to soften the *uncorrelatedness* requirement, we can assume that there exists a common language language that both services know how to speak, albeit it won't be the native language of either. How should this language look like?

[memo]: http://worrydream.com/refs/Licklider-IntergalacticNetwork.pdf
[kay1]: https://vimeo.com/22463791


## Current State

The "language of the Internet" is the Internet Protocol stack (TCP/IP), which allows one program on the internet to talk to any other program. But it only specifies *how* they can talk to each other, not *what* they can talk about or how to discover what the other one talks about.

It's analogous to the air, lungs and ears. Given enough air, I can certainly *speak* to any other human on the planet that is close by. And they can probably *hear* me, but that doesn't mean they *understand* me or that I can *talk* with them. This is the state that the IP stack leaves us with.

The most wide-spread *meaningful* language of the internet is the WorldWideWeb. It specifies how things can be addressed (with URIs/URLs) and how these things can present themselves (with HTML). It provides meaning by specifying what you can do with these resources (such as "post" and "get"). And most importantly it defines how communication is done (with HTTP).

The result is a *computing model* that turned out to be quite useful for accessing static documents but really not a good fit for doing anything more interesting. And over the last decades many million of man-hours have been poured into mitigating its design flaws.

I very much agree with Alan Kay's notion that "HTML has gone back to the dark ages and is one of the worst ideas since MS-DOS", as he said in [one of his most iconic talks in 1997][kay2]. A case of "reinventing the flat tire". I also remember him saying once that the web-browser "does too much and not enough". I think what he means is that there are way too many primitives in HTML which all have to be interpreted (doing too much) but it's not at all extensible (not enough). The second critique point also goes for HTTP which has a fixed number of *verbs* which just don't fit in many situations. But the worst design flaw is in HTTP, which assumes that all communication is initiated by the client and no state is preserved in the server.

How could we do this better?

[kay2]: https://youtu.be/oKg1hTOQXoY?t=1421


## Proposal

I propose to design a protocol based on a computing model that is the ultimate abstraction of all existing and conceivable models and is thus compatible with all of them. I would like to call this model [Qi] which means "breath" and "air" but also "energy flow".

This model could be used as a meta-language to create a meaningful but extensible vocabulary. Two uncorrelated services could use this model to discover each others capabilities and use the vocabulary to transfer meaning. The model would also be used to transfer not only data between services but also dynamic behaviour without the need to manually translate either.

This model could make communicating with aliens possible.

[Qi]: https://en.wikipedia.org/wiki/Qi


## Properties

The model consists of *composable*, *dynamic*, *concurrent*, *abstractable* and *distributed* objects, called *cells*. The semantics of the model are defined by these properties.


### Composable

A cell can contain any number of other cells as children. Each *child* has name that is unique amongst its siblings. 

```text
Child := <symbol>+
```

This form a tree where each cell is a node and can therefore be addressed by a *path* containing the *names* of each cell between the source and destination.
   
```text
Path := Name+
Name := Child
```

A name can also refer to the current node *itself* and to move up in the tree, a can refer to the *parent* or the *root* of the tree.

```text
Name := ..|<self>|<parent>|<root>
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

A cell may have a *reaction* which is executed every time the cell receives a *message* in the form of a cell path.

```text
Message := Path
```

A reaction consists of any number of *message sends* which define the path of the *receiver* cell and the message.

```text
Reaction := MessageSend*
MessageSend := Receiver Message
Receiver := Path
```

Paths in a reaction can also refer to the received *message* and the the execution *frame*. Frames are cells which are implicitly created for every execution to provide an execution-specific space.

```text
Name := ..|<message>|<frame>
```

#### Example

Given the following cell structure.

```text
       °
     / | \  
    A  B  C
       |
       D
```

The reaction of `A` is to send `B` to `C` (written as `<receiver> <message>`).

```text
°.C °.B
```

In its reaction, `C` creates a new cell `E` in the frame (denoted by `#`) and sends it to the child `D` of the received message (denoted by `@`), which is `B`, so to `°.B.D`.

```text
(create #.E)
@.D #.E
```

The resulting structure is the following. Note that the frame cell has an automatically generated unique name.

```text
       °
     / | \  
    A  B  C
       |  |
       D  a1fd5a
          |
          E
```

Hence the message that `D` received is `^.^.C.a1fd5a.E`



### Concurrent

All messages of a reaction are sent *concurrently*. Each message is sent by a *messenger* which will keep trying to deliver the message repeatedly. This way, data flow can be synchronized without requiring a fixed order of execution. Hence that messages may be sent to cells possibly before they exist.

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

Every cell has a *stem* cell from which it inherits both its reaction and children. Each inherited child and the reaction can be replaced by the *specialized* cell. In order to send a message to an overwritten cell or execute and overwritten reaction, a path may contain names referring to the *stem* of a cell.

```text
Name := ..|<stem>
```

If an inherited cell is modified, it will be *adopted* by its parent by creating a new child with the formerly inherited cell as its stem.

#### Example

Given a cell `A` with a child `C`. If a cell `B` has `A` as stem, it inherits `C` (denoted by lower-case `c`). 
        
```text
    A<--B
    ¦   |
    C   c
```
      
If a message is sent to `B.C`, the reaction of `A.C` is executed in the *context* of `B.C` which means all relative paths will be resolved starting at `B.C`. 

If `A.C` has a child `D`, it is inherited as well.
    
```text
    A<--B
    ¦   |
    C   c
    ¦   |
    D   d
```

If `B.C.D` is modified, for example by creating `B.C.D.E`, then both `B.C` and `B.C.D` are adopted, with `°.A.C` and `°.A.C.D` as stem cells respectively.
    
```text
    A<--B
    |   |
    C<--C
    |   |
    D<--D
        |
        E
```



### Distributed

A cell can be distributed over multiple processes and machines. A cell is connected to its *peer* by sending it a *join* signal with the connection parameters. If a cell can't deliver a message, it will forward it to its peers by sending each a *deliver* signal until one responds with *received*. If a peer can't deliver the message either, it responds with *failed*. A peer can disconnect from a cell by sending a *leave* signal 

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

If a new process (with the ID `222`) is created that contains also cell `A`, the signal `join A 222` is sent to process `111`. This adds a unidirectional connection from the cell in `111` to its peer at `222`.

```text
      111        222
    +-----+    +-----+
    |     |    |     |
    |  A~~~~~~~~~>A  |
    |     |    |     |
    +-----+    +-----+
```
