Tags: BDD, PHP

So Richard McIntyre (aka [mackstar]) created a BDD tool named [ShouldIT] ([video]) which led to a discussion between him and Konstantin Kudryashov (aka [everzet]), mostly comparing ShouldIT to Cucumber/Behat. For example in [this gist][gist].

Guess I'm jumping kinda late on the bandwagon here but I wanted to add my two cents.

To me it seems like the discussion is mostly about formularization and structure. While everzet's approach leads to a more detailed description of examples by explicitly describing the context for each scenario, mackstar prefers to combine the contexts (I guess mostly to avoid repetition?) and just formulate expectations explicitly.

Both approaches have something fundamental in common: using examples to specify the behaviour of a system. The difference is only *how* these example are formulated. But to me that's an "implementation detail".

The more important difference between Behat/Cucumber and ShouldIT is the direction of connecting the description and the implementation of the examples. While Cucumber executes the description (the .feature file) and matches its steps to the code, ShouldIT does it exactly the other way around - executing the code and then amatches the results to the descriptions.

So the discussion is not about the differences of the tools as much as about different description styles. It seems though as if the tools and the styles are all tangled up.

But what I don't understand is *why* a tool would ever dictate a certain style. Shouldn't the style and struct ure be up to the user? I sort of understand it in Cucumber's case because it needs to parse the description. But I don't see why ShouldIT couldn't work with just any style. After all it's just matching test results to text.

My approach is just not to use any tool for writing and executing the specification (besides a test runner, in my case PHPUnit). By only relying on the code, I have complete freedom over style and structure. This approach also avoids the duplication created by the separation of description and implementation.

But since (PHP) code is super ugly I *do* use a tool for browsing and presentation of the specification named [dox], which I wrote about in [my last article][last].

[mackstar]: https://twitter.com/mackstar
[everzet]: https://twitter.com/everzet
[ShouldIT]: https://github.com/bbc-sport/ShouldIT/
[gist]: https://gist.github.com/icambridge/7694d6d7b0a987f6c33b
[dox]: http://dox.rtens.org
[last]: http://blog.rtens.org/specification-by-example.html
[video]: https://skillsmatter.com/skillscasts/5675-should-it-a-new-approach-to-bdd-pain-not-included