status: draft

I propose a computing model names *Qi* that is compatible with every existing or conceivable model

## Usages

Translator between any two software platforms
=> meta language for "communicating with aliens"

## Properties

The model consist of a *composable*, *dynamic*, *concurrent*, *abstractable* and *distributed* objects, called *cell*. The semantics of the model are defined by these properties.


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

peers, protocol (deliver,received,failed,join,leave,ok)