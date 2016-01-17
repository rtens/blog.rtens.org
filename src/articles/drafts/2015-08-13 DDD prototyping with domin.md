Status: draft

In this article I'm describe the problems I see with how applications are commonly developed nowadays and propose DDD as a solution together with a UI generator I've built that allows rapid prototyping by allowing direct interaction with the domain model.

## UI-driven design considered harmful ##

Most software projects I see use what I like to call a "UI-driven design" approach, meaning the application is specified using more or less detailed illustrations of the user interface. The main reasons seem to be

1. The project members are end users themselves and thus used to think about software purely through the UI perspective
2. The business stakeholders feel the need to be able to "show something" in order to gain supporters. The "sexier" this something is, the better.
3. Designers are easier/cheaper to bring on board than developers

As a developer (I'm sure a designer would have a different perspective), I see a couple of problems with this approach.

#### Putting effort into volatile design ####

It wastes resource by creating (sometimes very detailed) user interfaces which usually don't survive contact with implementation

#### Domain model delution ####

The "core" (aka domain model) of the system gets deluted because UI concerns come first

#### Less seperation of concerns ####

Often times this leads to mixing UI concerns and domain concerns

#### Looser feedback loop ####

The feedback loop lossens since the whole system, including "core" and UI needs to be implemented before it can be tested by the business stakeholders. Often times, implementing the UI takes the same time

#### Form follows function ####

As industrial designers can attest, defining the functionality first and then creating a form to access it yields much better results than doing it the other way around.


## DDD to the Rescue ##

I love Domain-Driven Design because it deals with precicely these issues by turning the above described development process inside-out. Instead of concentrating on the solution - the application with it's user interface - DDD focuses on the problem space - the domain - and tries to create a model which can implemented in software. If you haven't already, I highly recommend to read "Domain Driven Design" by Vaugh Vernon.

[or the "Why Domain Driven Design is so great" article]

In order to get feedback of your domain modelling efforts, you need to be able to interact with the implementation of the model. So it seems like you need a user interface after all. But there are at least three ways to tighten the feedback loop.

1. Don't create a user interface and use "Specification by Example" (aka Behaviour-Driven Development) to verify that the model works for the chosen use cases.
2. Implement a minimalistic version of the user interface.
3. Generate a use interface from the domain model.

As you probably guessed, in the rest of the article, I show how to follow the third method using a tools I've recently developed.

## Generating user interfaces ##

I named the tool *domin* which is an akronym for *domain model interface*, because it's main purpose is to serve as a direct interface to your domain model. It relies on the *request-response* paradigm, meaning that each interaction with the system consists of sending a request which triggers some kind of response.

In *domin* the requests and the responses they produce are defined by **Actions**. *domain* takes care of getting the input data (aka request parameters) from the user and rendering the response.

[it's not CRUD - compare to other admin generators]

But enough with the theory, let me show you how it works.

[link to sample application]
[what examples should I show?]
[let's only use MethodActions and link to readme for other ways of creating actions]

- basic one with just two params and outputting them (foo:Hello bar:World)
- filling parameters
- other standard-lib types like integer, boolean, DateTime, arrays and objects
- nullable and multi
- enumeration and identifiers
- domin-defined types like HTML, File and Image
- rendering of objects, lists, tables and maybe even charts
- redirecting responses
- links
- the menu