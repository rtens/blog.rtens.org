When I was searching yesterday for "what makes programming hard", none of the results really resonated with me. All pieces were about why it is hard to become a *professional* software developer. Most people seem to view programming as an all-in activity. Either you're in for the big win (a job), or you don't even start trying. They talk about how problem analysis, modelling, software design, project management and so on make programming hard since they are all major challenges on their own. And for anybody who wants to become a professional developer, there are a multitude of resources and courses available. But what about the casual programmer? The every-day computer user who just has this small specific problem which could be easily solved by some machine magic? They have very limited options.

## Definitions

When I say "programming", you probably think of nerdy people hacking on their keyboards, encoding instructions in some language like C, Java, PHP or Python. But the kind of programming I want to address is the *casual* programming. The cases where most people wouldn't even call it "programming". For example, if you create a **spreadsheet** that calculates your holiday expenses, you're programming. And even if you create **slides** of your holidays with penguins flying around on the click of a button, you're still programming.

> Programming is the activity of creating a *program*. A program is a set of instructions that, when interpreted, specifies how to *react* to *events*.

This is my definition. It's probably not perfect, but let's work with it. The key terms here are **event**, **react** and **instructions**. In the case of slides, the event is *mouse clicked*, the reaction might be *text appears* and the instructions are created using a *specialized user interface*. In a spreadsheet, the event would be *this number changes* which causes *another number to change* as a reaction, following the instructions of *some formula*.

While I consider both of these to be "programming", other activities like *writing a Word document*, *making a video* and even *creating a web-site* don't fit the definition. Actually web-sites are edge cases because even without JavaScript, a hyper-link is the explicit instruction *browse to URL* to react to the event of *clicking on it*. That's not the slope I want to go down here though.

## Limitations

More obvious examples of casual programming are macros in Word and Excel, beginner-friendly environments like [Scratch] and specialized tools like Excel, PowerPoint and Matlab. And while these are great tools for their use cases they are all limited in their capabilities - by design. I probably should not complain about the limitations of Excel since more than a few of my freelancing projects were basically replacing a spreadsheet with a web application.

And it always got me wondering: Why is it that somebody with a vast and precise domain knowledge, who can formulate complex dynamic model on a spreadsheet is incapable of creating even a simple web application? Of course there are many tools out there to create web-sites but they are usually even more limited than Excel. What is it about general purpose programming that makes it so much harder? And is that intrinsic complexity that can't be avoided? Or is it incidental and we just haven't tried hard enough to make it easier?

Every time I teach programming to children, friends or other developers, I get the feeling that there should be an easier way. That most complications are absolutely unnecessary. So I use special environments like [Scratch] and [Etoys] to get the general ideas of across because they are wonderfully easiy to get started with. But even with Etoys, which is conceptually not limited in it's capabilities, I cannot create anything more complex than introductory examples myself. Pretty cool introductory examples with self-driving cars, but still somehow limited.

## Obstacles

When I teach programming, I usually see my students struggle with the same obstacles. And I have the suspicion that they are the same fundamental reasons that make it annoying for experienced programmers. Every time I have to tell to myself "that's just the way it is" I wonder if that's really the case. And I wonder why the people in my search result don't see these as problems. Is it because they get so used to them that they accept them as unavoidable complications? The way most people learned to accept spam?

The following list is what I consider to be the fundamental reasons of why programming is hard to learn and unpleasant to practice.

### Set-up

The first struggle appears even before you can start. Many programming languages are comically difficult to get started with. Maybe I'm asking for too much but spending half and hour to an hour for just setting-up the environment is often times frustrating, especially when time is limited. All language providers try to make this process as painless as possible but often they only achieve this for a single platform. 

The by far easiest language to start with is JavaScript since everybody has a browser installed.

### Syntax

So you finally have installed the programming environment of your choice and are ready to create your first program but you find something blocking your way: the syntax. So the very first thing is either to open the documentation or a tutorial. There is absolutely no way for anyone to guess how to do anything beyond basic arithmetic. Because it's just text, the language is not discoverable. This is a property it shares with the command line interface. Before you get anything done, you need to memorize obscure combinations of characters. In other words: In order to command the demon, you need to learn the spells. And the demon is very unforgiving towards even the tiniest mistake.

The best way is to avoid syntax all together with tile-based programming environments like [Scratch] and [Etoys].

### Interactivity

Since the days of punch cards, the feedback cycles of programming have increased immensely. What used to be several hours of waiting for the operators to feed your cards has become milliseconds after pressing a button. But still most languages don't let you interact directly with its elements. Debuggers try to bridge this gap but don't seem to be part of the standard tool set of most languages. It's almost impossible to find an introduction or tutorial that discusses how and when to use it. And even if your language comes with a good debugger, it usually only lets you inspect, but not change what you see.

The only language that I know of which allows true interactivity is Smalltalk and it's derivatives like [Squeak] and [Pharo].

### Sharing

Because of all these obstacles it'll probably take a while before you create your first program that you're actually proud of. But the day will come on which you want to show your creation to your mother. But how? Now you regret having saved on the set-up costs by choosing a interpreted language. And even if you can compile it to something she can run with a double-click, if she only has a phone, you're out of luck - unless that's what you were going for from the start. But even then she might have the wrong type of phone. And what if you change something and want her to get the new version?

This is where web applications really shine since all you need to send is a URL but they force your user to be on-line and you to learn not one but three to five languages.

### Dependencies

One reason why it's hard to share your program is because it will probably be using some other programs, so-called libraries. These dependencies need either to be bundled up with your program or your mother needs to download them before she can run it. And your dependencies probably have dependencies as well which might depend on the same programs as others but in different versions. And that's where it really gets complicated.

Here web applications have it easier as well but even those need to be installed somewhere. The only way that I know of to avoid the dependency struggle is to use web-services instead of downloading.

### Security

Now that you use web services for everything, you realize that all of them require you to authenticate, to proof that you are you. So you still end up with dependencies on libraries that handle the authentication. But even if you get the services to trust your program, to convince the user to trust it is a whole different ball game. Having chosen to create a web application now bites you in the back because there is no way you can access the user's file system or talk to any program running on his computer. But at least you can ask for permission to access the camera and location. If you get your user to download and run your program locally, then you basically get to do everything you want on their machine. Copy personal information, delete their holiday pictures. You name it.

Web application still have probably the best permission system since they don't require any up-front permission but still can access some things. Many platforms are adapting a more fine-grained permission system but they still have a long way to go.

### Serialization

Another problem with using web services is that now you are using a library which does not live in the same space as your application. Every piece of information you exchange with it needs to go through a thin wire. That not only slows everything down, it also means to have to squeeze your data really thin before you send it and inflate the strings you receive. This is called serialization and it's a major pain. You also need to do it if you want to keep any information after your program was shut down because the hard drive is really just a very long but equally thin wire.

[Smalltalk][Squeak] is once again the only environment that I know of which uses an *image* that just keeps everything that happens around. You still need to serialize data before sending it to anything outside the image though.

### Society

There also seems to be the conviction amongst programmers that programming needs to be hard and if it's not hard then "it's not real programming". I'm not sure if that's some sort of elitism or if they just want everybody to suffer as much as they did. So there is a huge technological but also social gap between people creating software and people consuming software. And unwillingly or not, the programmer community does its best to keep it that way. Neither do they provide the tools to make it easy for everyone to create programs, nor a particularly open attitude. Instead they create walled gardens, golden cages and cryptic jargon.

Many developer communities try hard to be as inclusive to new-comers as possible but there is still a lot of segregation between technologies (because other languages are always worse than mine).

### Practices

Lastly, programming is hard because a lot of times it deals with complex problems that are simply complex. And it's just too easy to get it wrong or to make a mess. Since programming is a very creative activity, there is no simple process you can follow to get it right. So even if all the above obstacles were eliminated. If you can easily and securely create and use programs but most of them are broken or too messy to work with, it's all in vain.

There are many practices like *open source*, *shared ownership* and *automated testing* that help to implement a good solution correctly in a clean and sustainable way. But this might actually be an inherent complexity that you can't easy get rid of.


## Solutions

So it seems that the way to avoid most of the described struggles would be to create web applications with Smalltalk (nd having arrived at that conclusion, that's definitely something I will try soon). But it always struck me as weird that although I'm convinced of Smalltalks advantages and have been for a while, I have yet to use it for something more than basic exploration.

My dream solution would be a mix between [Pharo], [Etoys] and the WorldWideWeb. The result would be an interactive programming environment where all objects are persistent and can be accessed from any device, secured by asymmetric encryptions. Building such a system, that removes all incidental complexity and enables every computer user easily and securely create and share dynamic models is what I'm planning to do with [zells].

[Scratch]: https://scratch.mit.edu/
[zells]: http://zells.org
[Etoys]: http://www.squeakland.org/
[Squeak]: http://squeak.org/
[Pharo]: http://pharo.org/
