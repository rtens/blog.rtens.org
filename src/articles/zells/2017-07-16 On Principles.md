In high school, I was oftentimes mocked for caring too much about principles. Saying things like "This is against my principles" or "I'm doing this out of principle" earns you quite bit of ridicule from fellow teenagers. And even today, I still get scoffed at when I'm one of the few cyclists in this city that stops at a red light. Out of principle.

So I wasn't too surprised when [Bret Victor]'s talk [*Inventing on Principle*][video] resonated deeply with me. I'm all about principles. But yet, I never looked for one in my work. Not of the kind that Victor talks about at least. But I got the feeling that there might be one.

[Bret Victor]: http://worrydream.com/
[video]: https://vimeo.com/36579366


## Choices

How do you live your life? How do you want to live you life? Why did you make the decisions you made? What do you want to stand for as a person? These are not the usual questions that you hear in a talk at a technical conference. But in this talk (transcript [here][transcript]), Victor speaks about nothing less than the question of all questions: What do I want to do with my life?

This is already the [second time][climate change] that Victor has deeply inspired me with his words. But I can't remember another presentation that moved as much as this one. He ends it with a truth that is as important and universal as it is simple. It's a liberating realization that yet many people refuse to accept.

> There are many ways to live your life. What's maybe the most important thing you can realize in your life, is that every aspect of your life is a choice. But there are default choices. You can choose to sleepwalk through your life and accept the path that's been laid out for you. You can choose to accept the world as it is. But you don't have to.

That sounds a lot like the usual "quit your job", "follow your dreams" and "listen to your heart" kind of talks. But Victor goes down another path. Instead of letting your economic interests or your heart guide your decisions, he suggests to discover a *principle*. In his words:

> If there is something in the world you feel is a wrong and you have a vision for what a better world could be, you can find your guiding principle. And you can fight for a cause. So after this talk, I'd like you to take a little time and think about what matters to you. What you believe in. And what you might fight for.

[transcript]: http://blog.ezyang.com/2012/02/transcript-of-inventing-on-principleb/
[climate change]: http://worrydream.com/ClimateChange/


## The Pain

I followed his advice and looked for things in the world that I consider "a wrong" and where I see a moral obligation to change them. I started to take better notice of all the little things that hurt me to watch. Just like it hurts Victor when he sees an idea die or like it hurts Larry Tesler when he sees someone stuck in a mode.

One thing that came into my mind immediately was the sting I feel when I see a screenshot of text on Twitter. That hurts. Or pictures of graphs on websites. That hurts as well. Also the fact that I have to copy a picture in order to share it with a friend or rely on a third party service to share my files or do simple surveys. I even need a third party just to get a reminder about emails I haven't gotten a reply to yet. 

I feel pain when I think about how an international consortium decides what pictograms I can text to my mom. Or about how much work goes into making a website work on all browsers and platforms. Every time I see someone struggle with file formats - be it video, graphics or formatted text - it hurts. And it hurts when I'm forced to export something as PDF. Or when I have to download a CSV from one service just to upload it again to another. Although you could argue that it's quite amazing *if* that's possible at all. 

Because what hurts even more is when my own content is locked away from me. And the worst pain I feel when I read stories about people loosing all their content because Facebook suspended their accounts without giving a proper reason or hearing. It hurts when a million passwords get stolen, and that a lot of them can be used for the email addresses that can reset them, and that that's usually enough to steal an entire identity. I also hate spam.

It hurts that I have to download an app on my phone just to do one simple thing. And that I have to uninstall another app first because I'm running out of space. And that I have to give it irrevocable blanket permissions to access my files or camera. It hurts that I have 8 different messaging apps installed in order to talk to people. And lastly, I cringe every time I have to manually restart my WiFi when the connection fails for no obvious reason.


## The Vision

I couldn't really infer a principle from these pain points. And I don't enjoy focusing too much on negatives anyway. So I also looked at my own work and at things that have inspired me for some more clues.

Bret Victor is certainly high up on my personal list of inspirations. Especially his interactive essays and demos of highly interactive authoring tools. The most interactive authoring tools I have at my own disposal is certainly Squeak Smalltalk. Everything about it is highly inspirational, along with pretty much [everything Alan Kay utters][kay]. Another thing that comes to mind is Paul Chiusano's take on [The Future of Software] and Ted Nelson's ideas about data structures. I'm also very much inspired by the [One Laptop Per Child][olpc] project and how the XO-1 and C.H.I.P. computers let you look under the hood. Or how Richard Pawson's [Naked Objects] allow the user to directly interact with the domain model.

My own work has lately evolved around Domain-Driven Design, Command/Query Responsibility Segregation, Event Sourcing, Specification by Example (aka Behaviour-Driven Development), Ubiquitous Language and collaborative domain modeling. I built a user [interface generator][domin] that is quite similar to Pawson's approach but is based on commands and queries instead of entities. I used it for a couple of prototypes and it was very helpful with debugging the domain model since it allowed me to give users direct access to the model early on.

And most importantly, last September I defrosted [zells] and since then dedicated as much time as I can afford to it. Zells is a software platform with a minimal programming model. Basically it's a mix of Kay's, Victor's, Nelson's and other ideas. My goal with this project is to enable software literacy by avoiding incidental complications of other programming platforms and thus making creating, understanding, manipulating and sharing software more accessible.

[kay]: https://www.youtube.com/playlist?list=PLwia5ezffHz6zhMc7is7aPGwKsLElPFWU
[olpc]: http://one.laptop.org/
[The Future of Software]: http://pchiusano.github.io/2013-05-22/future-of-software.html
[Naked Objects]: https://en.wikipedia.org/wiki/Naked_objects
[domin]: https://github.com/rtens/domin
[zells]: http://zells.org


## My Principle

Looking at my paint points and inspirations, my principle seems to have something to do with how people interact with computers. More specifically, what models they interact with and what lies between them and the model. But how to phrase it? Searching for inspirations, I looked at other people's principles.

> Creators need an immediate connection to what they're creating. - *Bret Victor*

> No modes. - *Larry Tesler*

> Women should vote. - *Elizabeth Cady Stanton*

> Software must be free, as in freedom. - *Richard Stallman*

> Enable mankind to solve the world's urgent problems. - *Doug Engelbart*

> Amplify human reach and bring new ways of thinking to a faltering civilization that desperately needs it. - *Alan Kay*

In his presentation, Victor uses Larry Tesler's principle "No modes." as an example to describe what properties a principle should have.

> If you choose to follow a principle, a principle can't just be any old thing you believe in. Larry Tesler['s principle] is a powerful principle because it gave him a new way of seeing the world. It divided the world in right and wrong in a fairly objective way. So, he could look at somebody selecting text and ask: Is this person in a mode? Yes or no? If yes, he had to do something about that.

So why not do it like Tesler? It seems I have a problem with computer users being unnecessarily separated from the dynamic models they are working with. So my principle could simply be expressed as

> No UI. - *Nikolas Martens*



## Your Principle

Since I cannot add anything valuable to to them, I end this bit with Victor's words.

> So, you can choose this life. Or maybe it will end up choosing you. It might not happen right away. It can take time to find a principle because finding a principle is essentially a form of self-discovery, that you're trying to figure out what your life is supposed to be about. What you want to stand for as a person. Took me like a decade. [...] I'm not saying you have to live this way. I'm not saying that you should live this way. What I'm saying is that you can.
