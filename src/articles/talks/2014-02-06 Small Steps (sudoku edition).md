Tags: TDD, PHP

After [trying out live coding][small_steps] at the October meeting of the [Berlin PHP user group][bephpug] last year, I tasted blood. So I decided to repeat it with a more complex problem.

At that point I remembered some articles discussing the [pros] and [cons] of TDD in the context of a [sudoku] solver. Seems like there is still [more to find][google] on this discussion. And I decided to join it.

So I broke down the sudoku solver problem into "small steps" - the smallest I could find - and presented to whole process, from an empty file to a working (yet somewhat slow) solver at this week's user group meeting. [You can find the result here][code]. Since a soduko solver is all but trivial, I wasn't sure if I could do it live without creating a horrible mess. But with the help of a very attentive user group it worked out just fine and it was great fun for me. And I'm glad to [hear][comment] that I wasn't the only one enjoying it.

[small_steps]: small-steps-at-bephpug.html
[bephpug]: http://bephpug.de
[sudoku]: http://en.wikipedia.org/wiki/Sudoku
[google]: https://www.google.de/search?q=sudoku+tdd
[pros]: http://johannesbrodwall.com/2010/04/06/why-tdd-makes-a-lot-of-sense-for-sudoko/
[cons]: http://devgrind.com/2007/04/25/how-to-not-solve-a-sudoku/
[code]: /res/sudoku_solver.zip
[comment]: https://twitter.com/IchHabRecht/status/430808466295648256