Ever once in a while everything seems to fall into place and suddenly the connection between previously unconnected dots becomes obvious. During the last couple of days, I've had such a moment. In this article I describe the reasoning behind my conclusion that [The Lean Start-Up][lean], [Agile Development][agile], [Specification by Example][sbe], [Test-Driven Development][tdd] and [Elon Musk's Secret Sauce][secret sauce] are all based on the same underlying principle: the scientific method.

[lean]: http://theleanstartup.com
[agile]: http://agilemanifesto.com
[sbe]: http://specificationbyexample.com
[tdd]: http://en.wikipedia.org/wiki/Test-driven_development
[secret sauce]: http://waitbutwhy.com/2015/11/the-cook-and-the-chef-musks-secret-sauce.html


## Models ##

> The scientific method is the process by which scientists [...] construct an accurate [...] representation of the world [wolfs]

The *representation of the world* is also known as *model* or *theory*, depending on its level of acceptance and applicability. A model may describe a phenomenon accurately only within certain limitations. We use many different models in our everyday lives in order to predict the outcome of our actions and we start forming then as early as when we learn that crying will yield food and attention. When it comes to achieving your goals, the known accuracy of your model is crucial.

For example, in order to save Lois Lane, Superman can pick between at least two models

	A) Catching something saves it from harm.
	B) Force equals mass times acceleration.
	
Using the first model, he will catch her while flying horizontally and rip her apart. If he uses the second model, he will realise that since he cannot changes Lois' mass, he has to also fly downwards and minimize her de-acceleration.

Both models are "correct" - meaning they hold under certain circumstances - as dropping an egg from the kitchen counter can easily demonstrate. Proving model A wrong is a little harder and might include dropping eggs from tall buildings. Falsifying model B is even harder and would probably require accelerating an egg to a larger fraction of the speed of light. A key principle of scientific models is that you can only show where it is incorrect, never that it's correct. There is no Truth, just , less wrong".

Improving the accuracy of our models might be the most important thing in our lives. And the only way to do so is by letting them collide with reality and discard the assumptions that didn't survive the collision. With each iteration you'll have a slightly less-wrong model. This is called the scientific method.

![Scientific Method](static/img/scientific_method.png)

[wolfs]: http://teacher.nsrl.rochester.edu/phy_labs/appendixe/appendixe.html


## Loops ##

The ["Secret Sauce"][secret sauce] of Elon Musk an other highly successful people is that they're really good at going through these assumption/validation loops. And the common principle of the before mentioned software development practices is that all of them optimize going through loops on different scales.

I identified three loops, whereas the outer precedes the inner.

![Software Development Loops](static/img/development_loops.png)

### <span style="color:red">Value</span> ###

**Assumption** What we're building is valuable to somebody.

**Scale** Weeks to months

**Validator** Market

**Optimization** Deliver working software continuously (agile) and collect real data from users and quickly as possible (lean)

### <span style="color:green">Behvaiour</span> ###

**Assumption** This is how the system is supposed to behave.

**Scale** Hours to days

**Validator** Customer

**Optimization** Have costumer close-by (agile) and specify system in common language (BDD, Specification by Example)

### <span style="color:blue">Code</span> ###

**Assumption** The behaviour is implemented correctly.

**Scale** Seconds to minutes

**Validator** Tests

**Optimization** Automate tests and keep them fast (TDD)


## Experiment is Supreme ##

Using the scientific method to solve engineering problems has the pleasant side-effect that it replaces inefficient discussions consisting mostly of guessing with the design and execution of experiments. Instead of guessing if your product actually solves a problem, build a simple prototype and find out. Instead of guessing the missing specification, turn around and ask the customer. Instead of discussing which software design works better, re-factor and run the tests.

Endless discussions can be an indicator that an assumption is based on a "magical" theory which cannot be tested and require faith to be accepted. Such a theory does not qualify as a scientific theory and should not be used in a decision-making process.

What I've experienced as a main hurdle when applying these methods is to avoid the error of mistaking an hypothesis for the explanation of a phenomenon, without performing experimental tests. Sometimes "common sense" and "logic" tempt us into believing that no test is needed. [wolfs] These believes can go very deep and questioning them might feel like an attack on our core values.

But being able to apply the scientific method openly and rationally to your projects and your life will greatly enhance your chances of success.