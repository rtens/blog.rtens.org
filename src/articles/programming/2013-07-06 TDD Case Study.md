Tags: TDD

I'm a big fan of [Test-Driven Development][tdd] and have been using it in almost all [projects] for a while now with astonishing results. If you are not convinced by TDD, drop me a [line] and I will do my best to change that. Although at first seemingly counter-intuitive, TDD quickly became as natural as me as camel-casing. But while showing it to fellow developers, I noticed how many only understand what test-driven means after having seen it in action. In this article I show how I implemented the solution for two exemplary problems with TDD step-by-step.

[tdd]: http://c2.com/cgi/wiki?TestDrivenDevelopment
[projects]: https://github.com/rtens
[line]: https://twitter.com/rtens_

## Programming Exercises ##

I Recently was asked for some programming exercises that could be used to improve one's software development skills. I came up with the following list of exercises with rapidly increasing difficulty.

1. Calculate the number at a given position of the Fibonacci series
2. Sort a list using Bubble sort
3. Test if a string matches a Regular Expression with a defined set of constructs (e.g. `^` `$` `.` `*` and literal matching)
4. Solver for the goat-wolf-cabbage puzzle
5. An "optimal move" suggester for any state of a tic-tac-toe game

Of course the exercises should be implemented test-driven. A key concept of TDD is to develop a solution iteratively in small steps. The smaller the better. The hard part is often times to be able to identify these small steps. For the Fibonacci series the steps are the positions themselves, for Bubble sort you can use lists with increasing complexity (starting with two elements in order, out of order, then three etc.) and the complexity of Regular Expressions can be fine-tuned easily as well by limiting the number of constructs. But with exercise number four I got stuck and did not instantly find a test-driven approach which is why I dedicated most of this article to it. But let's look at the easy example first.


## Test-Driven Fibonacci ##

As said, the tests for the Fibonacci series can be easily deduced from its first couple of values.

	f(0) = 0
	f(1) = 1
	f(2) = 1
	f(3) = 2
	f(4) = 3
	f(5) = 5
	
The implementation of these tests could look like the following snippet. I use [Python] in version 2.7 without a test framework in this article. Feel free to use the language and test framework of your choice, for example [JUnit][JUnitIntro].

	:::python
	assert fibonacci(0) == 0
	assert fibonacci(1) == 1
	assert fibonacci(2) == 1
	assert fibonacci(3) == 2
	assert fibonacci(4) == 3
	assert fibonacci(5) == 5
	
Now when I run this, all tests will fail. There is no function called `fibonacci` yet. But it's good to know that my test runner works as expected. So let's implement the first test.

	:::python
	def fibonacci(n):
		return 0
	
Run the tests again. Success! The first test passes. And although all the other ones are still failing I am content with myself for having found the tiniest step imaginable. Let's continue with the second test.

	:::python
	def fibonacci(n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
	
Yay! Two tests pass. Does this look like cheating to you? It's not. I am just following the specification. If it would only consist of the first two lines I would be done. But unfortunately I am not. So let's do another one.

	:::python
	def fibonacci(n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		elif n == 2:
			return 1
	
Running the tests confirms that I am 60% done. Time for a coffee break so I can tackle the hard part with new energy. Of course I could implement all five tests with if-else statements. But besides writing the test and making it pass, there is a third step in the TDD circle: refactoring. So the whole cycle goes

	1. Write the test.
	2. Make it pass.
	3. Refactor.
	
So apparently I have ignored the last step until now. Let's fix that and remove duplication from the production code.

	:::python
	def fibonacci(n):
		if n <= 1:
			return n
		else:
			return fibonacci(n-1) + fibonacci(n-2)
	
Ok. This was a little more than obvious refactoring. But TDD doesn't save you from actually using your brain. And we need to get to the more interesting example.

[JUnitIntro]: http://www.vogella.com/articles/JUnit/article.html
[Python]: http://www.python.org/


## Save the goat ##

As metnioned before, when I came to exercise four, I got stuck. I could not see any "small" steps that would lead me to something like this.

	:::python
	print solvePuzzle() # => g_wgc_g which means "move goat", "move back empty", "move wolf", "move back goat" ...
	
It seems like either it solves the puzzle or it doesn't. There is nothing in between. So I went ahead and implemented the solver in one giant leap instead of many small steps.

	:::python
	assert solvePuzzle() == 'g_wgc_g'
	
This was very unpleasant. I didn't see a single passing test until the end and even worse, I never had an excuse for a coffee break. But as usually, sometimes you need to disengage from a problem in order to solve so I went to bed, took a shower, had breakfast and came up with this.

	:::python
	puzzle = Puzzle()
	puzzle.addObject('g')
	puzzle.addObject('w')
	puzzle.addObject('c')
	puzzle.addConstraint('g', 'w')
	puzzle.addConstraint('g', 'c')
	
	assert solve(puzzle) == 'g_wgc_g'
	
The design is dramatically different from the previous implementation. The new solver does not any more just use a puzzle with a goat, a wolf and a cabbage but any puzzle. I can configure the puzzle by adding animals and other objects and putting constraints on which objects should not be left alone. This means I can make up harder puzzles, puzzles without solution but most importantly, also easier ones. Suddenly, there is a small step.

	:::python
	puzzle = Puzzle()
	puzzle.addObject('a')
	assert solve(puzzle) == 'a'
	
<div style="background-color: #cc3300">&nbsp;</div>
	
This time I will specify the tests iteratively after I made the last one pass. TDD works either way. You can either specify the entire behaviour up-front with increasing complexities or discover the steps along the way. Usually it's a mix of both. I also put a red or green bar below every code snippet to indicate the state of the test suite. So let's make the first test pass. We need a class and two functions.

	:::python
	class Puzzle:
		def addObject(self, id):
			pass
	
	def solve(puzzle):
		return move('a')
	
	def move(object):
		return object

<div style="background-color: green">&nbsp;</div>
	
That's what I call a tiny step. I didn't really implement anything and the test is already passing. Let's refactor that duplication in `solve`.

	:::python
	class Puzzle:
		def __init__(self):
			self.objects = []
		
		def addObject(self, id):
			self.objects.append(id)

	def solve(puzzle):
		return move(puzzle.objects[0])

<div style="background-color: green">&nbsp;</div>
	
This already solves all puzzles with just one object. How about two objects?

	:::python
	puzzle = Puzzle()
	puzzle.addObject('x')
	puzzle.addObject('y')
	assert solve(puzzle) == 'x_y'

<div style="background-color: #cc3300">&nbsp;</div>
	
Fail! But that was expected. Actually, when doing TDD, I always make sure to have seen every test failing at least once. It's the best way to confirm the tests are actually doing something. The reason for the failing test is that `solve` still only moves the first object. So let's try to fix this.

	:::python
	def solve(puzzle):
		moves = ''
		for object in puzzle.objects:
			moves += move(object)
		return moves

<div style="background-color: #cc3300">&nbsp;</div>
	
Seems like I am getting closer. Now I get 'xy' as the solution. And if the goat, the wolf and the cabbage were standing on catapults this would actually work but for our puzzle the farmer can only move an object if they are on the same side. This means we need to know on which side everyone (the objects and the farmer) is. Let's put this information into the dictionary `positions` which is indexed by the object (including the farmer) and has a boolean value indicating if the object is on the left side of the river (`True`) or on the right side (`False`). 

	:::python	
	farmer = '!'
	
	def solve(puzzle):
		positions = getStartPositions(puzzle)
		
		moves = ''
		for object in puzzle.objects:
			moves += move(object, positions)
		return moves

	def getStartPositions(puzzle):
		start = {farmer: True}
		for object in puzzle.objects:
			start[object] = True
		return start

<div style="background-color: #cc3300">&nbsp;</div>
		
I guess a coder in the true python spirit would write the second function as

	:::python
	def getStartPositions(puzzle):
		return dict([(object, True) for object in [farmer] + puzzle.objects])

<div style="background-color: #cc3300">&nbsp;</div>
		
Also, an object can only be moved when it's on the same side as the farmer.

	:::python
	def move(object, positions):
		if positions[object] == positions[farmer]:
			positions[object] = not positions[object]
			positions[farmer] = not positions[farmer]
			return object
		else:
			return ''

<div style="background-color: #cc3300">&nbsp;</div>
	
Let's run it... Seems like the farmer gets stuck on the right side. Let's give him the chance to go back without cargo.

	:::python
	def move(object, positions):
		if object == '_':
			positions[farmer] = not positions[farmer]
			return '_'
		[...]

<div style="background-color: #cc3300">&nbsp;</div>
		
This means that we have to add `'_'` (nothing) to the list of objects that can be moved.

	::python	
	def solve(puzzle):
		positions = getStartPositions(puzzle)
		
		moves = ''
		for object in getMovables(puzzle):
			moves += move(object, positions)
		return moves
		
	def getMovables(puzzle):
		return puzzle.objects + ['_']

<div style="background-color: #cc3300">&nbsp;</div>
			
Let's run it. Bummer. Now the first test fails. Seems like it doesn't know when to stop. And while we're at it, let's have the farmer make trips repeatedly until everybody is on the other side.

	:::python
	def solve(puzzle):
		positions = getStartPositions(puzzle)
		
		moves = ''
		while (True):
			for object in getMovables(puzzle):
				moves += move(object, positions)
				
				if positions == getTargetPositions(puzzle):
					return moves

	def getTargetPositions(puzzle):
		return dict([(object, False) for object in [farmer] + puzzle.objects])

<div style="background-color: green">&nbsp;</div>
		
Bingo! Both tests are passing. Next step: three objects.

	:::python
	puzzle = Puzzle()
	puzzle.addObject('c')
	puzzle.addObject('w')
	puzzle.addObject('g')
	assert solve(puzzle) == 'c_w_g'

<div style="background-color: green">&nbsp;</div>
	
Something that works with two usually works with three as well (which is why software engineers count "zero, one, many") so I can already modify this test to make sure that the goat and the wolf are not left alone.

	::python
	puzzle.addConstraint('g', 'w')
	assert solve(puzzle) == 'w_c_g'

<div style="background-color: #cc3300">&nbsp;</div>
	
We can do this by checking for each move if the new constellation is "valid", meaning that no two objects that are unhealthy for each other are left alone on one side. So I change the inner loop of the `solve` function to

	:::python
	for object in getMovables(puzzle):
		nextMove = move(object, positions)
		if (isValid(puzzle, positions)):
			moves += nextMove
		
		if positions == getTargetPositions(puzzle):
			return moves

<div style="background-color: #cc3300">&nbsp;</div>
			
If I run this now python reminds me that I need to define the `isValid` function. So I do her this favour.

	:::python
	def isValid(puzzle, positions):
		for threat in puzzle.constraints:
			victim = puzzle.constraints[threat]
			if positions[threat] == positions[victim] and not positions[farmer] == positions[threat]:
				return False
		return True

<div style="background-color: #cc3300">&nbsp;</div>
	
Looks good enough. So I run it. And bam! Some weird thing went wrong. Debugging time. So I check the positions after the first move and see that the goat is still moved. Simply not registering the move is apparently not enough, I also need to undo it. Luckily in this puzzle, undoing means just doing the same move again.^^

	:::python
	if (isValid(puzzle, positions)):
		moves += nextMove
	else:
		move(object, positions)

<div style="background-color: #cc3300">&nbsp;</div>
		
This should fix it. But the test still fails because the found solution is `w_cwg_w`. This is not what I expected but given the constraints, it's actually a valid solution albeit unnecessarily complicated. But finding the shortest solution is not a requirement so I just adapt the test to the reality.

	:::python
	assert solve(puzzle) == 'w_cwg_w'

<div style="background-color: green">&nbsp;</div>
	
And finally all tests pass again. I'm not entirely happy with having to adapt the assertion so this might be something I would work on when I want to improve the algorithm. It turns out by changing the order of the objects to `['w', 'c', 'g']`, the solution would be indeed `w_c_g`. So I could look for the shortest solution systematically by trying every possible order. But yeah.. later.

Because we are still missing our final and original test.

	:::python
	puzzle = Puzzle()
	puzzle.addObject('c')
	puzzle.addObject('w')
	puzzle.addObject('g')
	puzzle.addConstraint('w', 'g')
	puzzle.addConstraint('g', 'c')
	assert solve(puzzle) == 'g_cgw_g'

<div style="background-color: green">&nbsp;</div>
	
Since this is just a variation of what I have already implemented, the test passes right away and I realize that I'm done. Completely done. Done-done. And I have a nice little test suite to prove it which you can find [here][riverpuzzle].

But of course I'm only done until I think of more features. I already mentioned the finding-the-shortest-solution idea but another one would be to detect if a puzzle does not have a solution or maybe it has one but only with a certain order of objects. So feel free to practice your TDD skills by teaching the solver some more tricks. A rather complete version in PHP can be found [here][phppuzzle].

[riverpuzzle]: static/res/river_puzzle.py
[phppuzzle]: https://github.com/rtens/riverpuzzle


## Conclusion ##

Test-Driven Development has many advantages both during development and in the long run. The long-term benefits probably outweigh the short-terms ones by several magnitudes. But TDD can be tricky to apply and since we are humans and future benefits are a terrible motivation, I focused in this article on how TDD can be used even in non-obvious cases to improve the design of the solution and facilitate development.

Most of the questions that remain unanswered by TDD are addressed very effectively by a development method called [Behaviour-Driven-Development][bdd], aka [Specification by Example][sbe]. It is actually my preferred method at the moment and also a superset of TDD which is why I started with it and kept BDD as its own topic for another day.

[bdd]: http://dannorth.net/introducing-bdd/
[sbe]: http://specificationbyexample.com/