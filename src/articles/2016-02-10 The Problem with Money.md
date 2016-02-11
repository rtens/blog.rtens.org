For a long time I've been having the faint feeling, that something is fundamentally wrong with money. With the way it's created, the way it's used, the way it drives our actions. I could never quite put my finger on it but the feeling was always there when I thought about economy, capitalism and welfare. Only recently I could put the puzzle together and found a way to fix money.

When I learned about [social entrepreneurship], I immediately felt that it might be a solution for many problems caused by capitalism and although I'm convinced that it will replace conventional businesses in the long run, it doesn't go deep enough. Then along came [Bitcoin] just as the global economy was collapsing. And while using cryptography and the [block chain] to free trading from bank-controlled money is ingenious, it still didn't feel right to me and I only recently discovered why. The last piece of the puzzle was my [move to Bhutan][bhtuan] in the beginning of the year. Learning about some of the problems of the local monetary system got me thinking and talking again about money. And when a friend told me about [complementary currencies], it finally clicked.

[social entrepreneurship]: https://en.wikipedia.org/wiki/Social_entrepreneurship
[Bitcoin]: https://bitcoin.org/
[block chain]: https://en.wikipedia.org/wiki/Block_chain_(database)
[complementary currencies]: https://en.wikipedia.org/wiki/Complementary_currency
[bhutan]: http://blog.rtens.org/category/bhutan.html

## Bank Money

In his book ["The Ecology of Money"][eom], Richard Douthwaite defines three types of money: Bank money, government money and people money. It surprised me to find out that most of the money we use is *bank money*, created by private banks when giving loans for profit. There are several problems with this kind of money, nicely described in the [open money manifesto][manifesto]. All these problems are design flaws that can be avoided by improving the design of a currency.

One fact that most people accept as a law of nature is that acquiring money always costs in the form of **interest**. Interest benefits the rich and impairs the poor. Not a surprised in a system designed by the rich. Compound interests make it easy to get money if you have money and hard (if not impossible) if you don't. It also puts a **profit-pressure** on the every business that ever took a loan. This condemns the economy to eternally grow just to make even, if necessary on the expense of the community and environment. The result is an economy centred around profit-maximization instead of sustainability.

A phenomenon that makes interest seem unavoidable is **inflation**. Since money becomes worth less every day, you *have* to earn interest just not to loose wealth. But inflation is a side-effect of how a currency is created and managed. A better design could incorporate the incentives that inflation provides without its disadvantages.

Another key problem is the **scarcity** of money. It's kept scarce artificially by a **bank monopoly** to control it's value. This is necessary since the value of bank money is completely artificial. It's only worth something because it's hard to get and everybody seems to want it. But again, it's only hard to get for those who don't have much. And most times there is not enough when it's needed the most. When building schools or community centres for example. Because money always chases the highest return-on-investment, it tends to concentrate in a few profit centres. Therefore many regions experience a **capital drainage** - most of the available money is spent outside the community and never returns - increasing it's scarcity in these regions.

And because it is controlled by private banks, money is actually **hard to move**, thus inhibiting trade. Transferring it to someone requires either to hand over physical tokens or relying on a third party such as banks and credit institutes. Either way implies a transaction cost which limits the size of feasible transactions, apart from the fact that most people are not even able to open an account with any bank or credit institute.

[eom]: http://www.feasta.org/documents/moneyecology/contents.htm
[manifesto]: http://www.openmoney.org/top/omanifesto.html

## Cryptography

This becomes visible in a country like Bhutan where there are no credit cards and online-banking is in its infancy. While attending the [start-up weekend in Thimphu][swthimphu], I noticed that payment was a big challenge for many business ideas since the only way to pay for a service is by sending cash, sending a cheque or going to the bank to make a transference in person. At the workshop I also met a entrepreneur who told me he once tried to set-up a payment service but was not granted the required licence by the central bank.

I started thinking if a cryptographic currency like [Bitcoin] could be used to solve the payment problem. But that would require a Bitcoin-Ngultrum exchange service which would probably need a banking licence as well. And although I'm a big fan of the block chain, Bitcoin shares a design flaw with conventional currency: the artificial value through scarcity.

Apart from that, Bitcoin also seems to be facing technical and governance problems. Mike Hearn even goes as far as to claim that [Bitcoin has failed][hearn]. I believe a reason might be that purely monetary incentives are just not enough to keep a community viable. In such a system, the concentration of wealth and formation of monopolies is motivated which is harming the community. The result is that the vast majority of [hashing power] now lies in the hand of a few people.

Another core assumption of Bitcoin that I disagree with concerns trust. A declared feature of Bitcoin is that users can transfer the ownership of a coin without having to trust each other or any third party. The only thing they have to trust is the block chain which is controlled by whoever has the most computing power in the world. But what is trade without trust?

[swthimphu]: http://www.up.co/communities/bhutan/thimphu-bhutan/startup-weekend/7382
[hearn]: https://medium.com/@octskyward/the-resolution-of-the-bitcoin-experiment-dabb30201f7
[hashing power]: https://bitcoin.org/en/vocabulary#hash-rate

## Community

So instead of using a currency that denies trust, let's use one that fosters it. Instead of basing the value on artificial scarcity, let's design a currency that is abundant and based on real value. And instead of accepting the yoke of perpetual growth, let's create a interest-free monetary system that is under the control of the community that uses it.

As I said this to my brother in-law, he responded "This sounds like what the Chiemgauer is doing." which is how I learned about [complementary currencies]. The [Chiemgauer] is a local currency used in the region around Chiemsee, created in 2003 as a school project. It implements an idea by Silvio Gesell of *money that rusts*. Gesell argued that money, like natural products should slowly lose its value over time and thus create a spending incentive. *Chiemgauer* is the proof that this idea actually works with a turnover of over 7 million units in 2014.

I discovered that there are [hundreds of complementary currencies][list], some fairly large like the [WIR Bank] in Switzerland but most are small by design to support a local community. A very comprehensive description of many currencies along with good arguments supporting them can be found in [People Money]. But they all have in common that they require a central accounting system or a central issuer of physical tokens.

[Chiemgauer]: http://www.chiemgauer.info/
[list]: https://en.wikipedia.org/wiki/Local_currency#List_of_local_currencies
[WIR Bank]: http://www.wir.ch
[People Money]: http://www.lietaer.com/writings/books/people-money/

## GroupCash

Since I still wanted to solve the online-payment problem, physical cash was not an option and setting up a central bank for community money would require a licence which was apparently hard to get. What I needed was a system that combines the de-centralized features of a cryptographic currency with the community-building properties of a local currency. In such a system, transactions could be done directly without relying on a third party by trusting eachother, every user would be in control of its own account, and could even print its own cash if needed.

So I started to design a system with these properties which I named [groupcash]. The result is a software system based on digital signatures. Money is created by value-creating companies issuing delivery promises. The promises are signed by a regulatory entity that guarantees the compatibility and plausibility of these promises. Each promise is worth one unit which can be transferred by signing it over to a new owner. To avoid double-spending, transferences can be validated by the company backing the promise, but this does not have to be done immediately - depending on how much the giver is trusted.

So although there is a single entity regulating the issuing, it cannot issue units on its own and has no role in the trading. And although validation is done by the backing companies, the owner of a promise can independently prove their rightful entitlement to the delivery of the promise.

A more detailed description of the system including algorithms to issue, transfer and validate units can be found [here][whitepaper]. I also implemented these algorithms in a [PHP library] and intend to create a web application that can be used to easily set-up a local currency community. Peer-to-peer and mobile applications will follow once the system is proven to be useful.

[groupcash]: https://github.com/groupcash/
[whitepaper]: https://github.com/groupcash/core/blob/master/README.md
[PHP library]: https://github.com/groupcash/php/

## Resources

More information and resources on complementary currencies can be found here

- [Complementary Currency Resource Center](http://complementarycurrency.org)
- [Complementary Currency Literature](http://cc-literature.de)
- [CommunityForge](http://CommunityForge.net/en) - Open-source tools
- [Open Money Project](http://openmoney.org)
- [RegioGeld e.V.](http://regiogeld.de)
- [IRTA](http://irta.com) - International Reciprocal Trade Association
- [STRO](http://socialtrade.org) - Social Trade Organization
- [QOIN](http://qoin.org) - Consultancy and Tools
