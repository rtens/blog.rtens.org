(This article was featured on the [blog of the International PHP Conference][blog])

The premise of my talk "[Rapid Prototyping with Domain-Driven Design][slides]" is that the two greatest foes of every software developer are a) uncertainty and b) complexity. Over the years, we have invented many tools and methods to fight them. But eventually we realized that uncertainty cannot be defeated and instead we learned to embrace it with ever shorter feedback cycles, "agile" methods, continuous integration, devops and Test-Driven Development.

But what about complexity? Can it be defeated? We sure are trying. Every other week there is a new programming language claiming to reduce it, every other day a new framework to make storage, networking, rendering or communication easier than ever before.

One could think that if this trend continues, writing software might one day be as easy as 123. But these are all solutions to technical problems and while they receive a lot of attention, I consider them unessential. There are many ways to solve a certain problem with software. Many different languages and frameworks to use. Each with their own benefits but also own drawbacks, like added complexity.

Outside the technology lies the conceptual space of the problem you are trying to solve with your piece of software - the domain. If you are creating a jump-n-run game, your domain includes physics, didactics and game design. If you write a restaurant management system, your domain consists of tables, orders and bills. Whatever kind of software you write, you will have to deal with the domain and its complexity. It cannot be avoided.

This is why in the talk I claim that "complexity is essentially in the domain".

The good news is that we might actually one day defeat unessential complexity. Many people, myself included, are working on it. But the bad news is that even then we will still be stuck with the complexity of the domain, which we cannot reduce without reducing the problem, since it’s part of it.

But it’s really not that bad because without unessential complexity, the difficulty of the solution depends solely on the problem. Easy problems, like organizing your grocery shopping would be trivial to solve. Harder problems, like analyzing your supermarket receipts and calculating your consumption rate of butter, would be only proportionally more difficult, with a smooth learning curve between them.

My personal hope is that it is possible to build a software development tool that avoids all unessential complexities. With such a tool, everybody could solve most of their own problems themselves. It could lead to a general software literacy, enabling people of every trade to take advantage of the full potential of computers, without depending on a tiny fraction of the “elite” to solve their problems for them.

Without technical complexity to conquer, software creators could completely focus on the domain. Instead of battling with encoding and databases, programmers could spend their time on understanding the world and forging their insights into dynamic models.

But we are not quite there yet. The tools we use are still complex enough that they require weeks of training before you can write software that solves even the simplest of your problems, let alone the harder ones. So you don’t need to worry that your knowledge of the newest Javascript framework becomes obsolete soon. Our jobs are safe yet.

We still need professionals for creating and maintaining every tiny bit of software but because engineers have an inclination towards technical problems, we tend to neglect the domain.

If we accept that technical complexity is essentially in the domain, we can start to avoid technical complexity and focus on the essential problem, the domain. This is the premise of Domain-Driven Design.

[blog]: https://phpconference.com/blog/essential-complexity/
[slides]: http://blog.rtens.org/static/res/rapid_prototyping_with_ddd_v2.pdf