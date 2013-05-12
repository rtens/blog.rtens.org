Tags: testability

[Dependency Injection][di] is a must-have for testable code - and please write me if you are no convinced of testability. I even wrote my [own][factory] simple Dependency Injection Container recently out of pure joy on experimenting. But there is one tiny thing that I can't make up my mind about when using Dependency Injection. Should dependencies be pulled or pushed?

[di]: http://www.martinfowler.com/articles/injection.html
[factory]: http://github.com/watoki/factory


## Push ##

The first option would be that the DIC *pushes* objects into the constructor.

	:::java
	class MyClass {

		private SomeDependency one;
		private SomeMore two;

		public MyClass(SomeDependency one, SomeMore two) {
			this.one = one;
			this.two = two;
		}
	}

The dependent classes require their own dependencies the same way which results in a dependency tree with the root somewhere in the Main class.

	:::java
	DependencyInjectionContainer dic = new DependencyInjectionContainer();
	MyApplication app = dic->getInstance(MyApplication.Class);

**Pros**

- The classes are completely DI-ignorant
- Dependencies are defined in a natural way

**Cons**

- Overhead for analyzing the constructor (can be compensated by generating static factories)
- It seems a bit verbose, especially with many dependencies

## Pull ##

The second option would be for the the requiring class to *pull* the dependencies from the DIC.

	:::java
	public MyClass(DependencyInjectionContainer dic) {
		this.one = dic.getInstance(SomeDependency.Class);
		this.two = dic.getInstance(SomeMore.Class);
	}

Here, only the DIC itself is passed to the class. If this is done consistently, you don't need to `getInstance()` anymore.

	:::java
	public MyClass(DependencyInjectionContainer dic) {
		this.one = new SomeDependency(dic);
		this.two = new SomeMore(dic);
	}

**Pros**

- Cleaner constructor signature

**Cons**

- Every class depends explicitly on the DIC


## Conclusion ##

While the software architect in me strongly leans towards pushing, the lazy programmer in me often times uses pulling. It's just less writing. But it's probably not a good idea to couple everything with your DIC. This is confirmed by the [clean code cheat sheet][clean] with the anti-pattern "Artificial Coupling". But still, the easier to read and to maintain code could be worth it.

I would like to know what you think about this. Which approach do you usually use?

[clean]: http://www.planetgeek.ch/wp-content/uploads/2011/02/Clean-Code-Cheat-Sheet-V1.3.pdf
