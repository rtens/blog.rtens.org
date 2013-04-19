Tags: git, lean
Status: draft

Controlled experiments, aka split tests, aka a/b tests are a great way to prove your daily hustle actually makes a difference. But each experiment causes a significant code overhead, making sure that a certain user only sees variant. In this article I propose a way to facilitate experiments by making the code completely ignorant of them.

## The joy of experimenting ##

Testing your product is a good idea. Test it as much as you can. Test it against you specification, but test it also against the market. Because even the best specification is pointless if nobody uses your stuff. 
And when the numbers go up after a few dozen updates are released, everybody pats his own shoulder. Even worse, if the numbers go down, it's everybody's else fault. The gold standard of proving that your doing actually has an effect are controlled experiments.

There are plenty of libraries that support the painless integration of controlled experiments in your project. But all of them require a code overhead that needs to be cleaned up after the experiment is over. This means all code belonging to the losing variant needs to be removed. This might be quite a lot and hard to find. Especially if you don't only test a green button against a blue one.

## Call the specialist ##

So how about using a system that is specialized in keeping track of differences and implementing variants as branches of your version control system? The advantages are clear: the code is completely ignorant of the experiment and thus cleaning up becomes as simple as deleting a branch.

But the approach also brings new challenges: how do you deploy several branches? How do you keep them in sync? How are users assigned to variants? I haven't implemented anything yet but I'd like to suggest possible solutions.

## Branching strategy ##



## Deployment ##


## Conducting the experiment ##

