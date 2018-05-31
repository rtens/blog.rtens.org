I used last Christmas break to watch "The Expanse" which quickly became my favorite SciFi series with its incredibly realistic and inspirational vision of a humanity that has colonized the solar system. And it was one sentence in this show that struck an unexpected chord with me. It was a comment about how - even centuries after populating Mars and the asteroid belt - people still used earth-based units to measure time such as days, months and years. As probably almost [every software developer][zach], I struggled more than once with the convoluted dominant time system of this planet, and this comment got me once again thinking about what an alternative might look like.

The result of this holiday pondering is *[Reference Time]*, a time system designed for the Space Age. A time system for a fundamentally relative universe, and a time system for humans, using simple and regular units. Reference Time is always defined relative to a frame of reference and simply counts seconds passing in this frame since an arbitrary zero point, grouped in decimal units that are meaningful to people.


## Design Goals

> "We have a choice: do we actually think, that the sun, the stars and the moon are important to our lives, or do we think that our lives should be controlled by intervals?" - [Kristen Lippincott][bbc]

As long as we live only on this one planet, the movement of the sun, the stars and the moon are probably still important to our lives. But what time system would make sense for a civilization that is not bound to a single planet anymore? What if the sun, earth and the moon are too far away to guide us? What if we start living in completely artificial environments were it makes much more sense to let intervals control our lives? Intervals that we choose. What could time for a space faring civilization look like?

### Relativity

Time is relative. And not only in the sense that a second in the supermarket queue appears longer than on the beach, but also in a very physical sense. One of the most important predictions of Einstein's theory of [Special Relativity][relativity] was that time behaves differently in different frames of reference moving at different speeds, which is most impressively demonstrated by the fact that clocks on GPS satellites shift about [38 microseconds][gps] per day compared to clocks on earth. While this time dilation can be calculated precisely for satellites in a known and carefully tracked orbit, it would be very difficult for a large number of vessels zipping through the solar system on unpredictable trajectories. So a space-age time system should incorporate the fact that every interval is always relative to a specific frame of reference, e.g. the surface of a planet, an orbit or a vessel.

Time is personal. While the thought of abolishing all timezones is tempting, it is not compatible with reality where time is all but universal. Space exploration will only increase the number of timezones with different cycle lengths, time dilations and even people living on the same station but in different time zones to provide uninterrupted operations. A universal time system should therefore embrace the fact that everybody is following their own clocks, explicitly state the offset and a frame of reference, and make conversion between them as simple as possible.

### Regularity

To ease calculations, the time system needs to be as regular as possible. The notation of our current calendars and clocks use decimal place-value numbers but different bases for minutes, hours, days and weeks and even irregular lengths for months and years. And although bases like 12 and 60 make division easier, it comes at the cost of addition and subtraction which in my experience are the much more frequent operations on time. A regular time system should use the same base for all of its units and numbers.

Irregular units make calculations harder, but as long as the exceptions are predictable (e.g. leap years), they're still possible. A time system bound to natural phenomena will also include unpredictable discontinuations (e.g. leap seconds), which in the best case make calculation impossible and in the worst case leads to contradictory results. A continuous time system should avoid cyclic and sporadic exceptions.

### Usability

Relativity and regularity make a time system easier to use for machines, but it also should be usable for humans. We need to be able to easily speak about time frames that are important to us. For people living in artificial environments, this may be different intervals than the natural cycles we use nowadays. A usable time system should enable precise and efficient communication while avoiding ambiguity.


## Reference Time

I would like to propose a *time system for the space age*, which is not bound to the natural cycles of a single planet, but designed for **regularity**, **usability**, and most importantly **relativity**. The relative nature of time means it can only ever be measure relative to a frame of reference. *Reference Time* counts **[SI seconds][second]**, grouped into **decimal units**, relative to a **frame of reference**, that have lapsed since an arbitrary **zero point**.

Instead of insisting on a single, universal time, in *Reference Time* a point of time is always given in reference to something. Examples are "We'll arrive at 42 Cycles and 21 Turns, Ship-time since mission start" or "The meeting starts at 97 Turns and 5 Moments, Station-time since start of shift" or "I was born at 400 Generations, 46 Rotations and 45 Cycles, Earth-time since start of humanity".

### Units

Counting seconds makes for a very regular time system, but gets quickly unwieldy. To facilitate machine-to-human and human-to-human communication, seconds are grouped into decimal units. It happens to work out that groups of 100 (and one group of 10) lead to very useful intervals.

Here they are:

- 1 Second is 1 *Second* - the time between two heart beats of a well-trained person, or the time it takes to say "1 elephant".
- 100 Seconds are 1 *Moment* - a little less than 2 minutes and a good unit for business events, e.g. for bus schedules or appointments.
- 10 Moments are 1 *Turn* - a little more than a quarter hour and a good unit for social events, e.g. meeting friends or starting dinner. It's also a nice unit for splitting up a working day, e.g. "this is gonna take 5 Turns".
- 100 Turns is 1 *Cycle* - a little longer than an Earth day so not really useful on Earth but it might be suitable for sleep cycles in artificial environments.
- 100 Cycle is 1 *Rotation* - about a third of a year which seems like a good unit of time to track personal and professional progress or to plan projects, e.g. "Next Rotation I wanna learn piano." 
- 100 Rotations is 1 *Generation* - with 31.7 years very close to the [average time between human generations][generation] and the largest unit of time in the system, e.g. "the Roman empire fell 47 generations ago".

### Zero Points

Zero points are freely chosen and multiple clocks can be synchronized by broadcasting a reference description along with the number of seconds counted. Alternatively, a zero point can be defined in terms of external events or other time systems. For example "1st of January 1970", "next midnight UTC plus 2 hours", "last high sun in Greenwich", or even "when I got up today".

For an coordinated [Earth Reference Time][Reference Time] (ERT), we need a widely accepted, precise and continuous time signal. I picked the one emitted by the satellites of the [Global Positioning System][GPS], which uses the [Geoid] as its frame of reference. Regarding the zero point, I would follow the suggestion of [Kurzgesagt] and define ERT as GPS + 400 Generations, which puts 0 ERT roughly at the [start of civilization].


## Other Time Systems

There are of course many many time systems already out there and you might (rightfully) have the strong desire to point me to [xkcd#927] by now. And maybe I simply had too much time on my hand over the holidays but none of the systems I could find meet the stated design goals. Let's have a quick look at some.

**Coordinated Universal Time** ([UTC]) is all but regular or predictable and also does not support different frames of references since time zones are defined by a fixed offset and depend more on arbitrary political decisions than location. A more regular version of UTC is **[Unix time]** which only counts seconds (skipping leap seconds) which makes it much less usable for humans.

Various **[decimal time]** systems tried to improve regularity, usually by dividing an average Earth day repeatedly by ten. These systems inherit all problems of whatever calendar they are bound to, and sacrifice ease of division for only a small facilitation of addition and subtraction. They also usually redefine the length of a "second".

The **International Atomic Time** ([TAI]) is continuous (by ignoring leap seconds) but apart from that as irregular as UTC. Unless you use a notation like [TAI64] which is extremely regular by counting only seconds but it still does not support different frames of reference and is unusable to anyone who needs to handle large amounts of seconds or who is not fluent in hexadecimal notation. The time of **[GPS] satellites** can be derived from TAI, but counts weeks and seconds instead of using the Gregorian calendar. Although this is an improvement over just counting seconds, it still doesn't make it human friendly.


## Reality Check

So what's this *Reference Time* actually good for? Probably not much. Living in a natural environment, there is little reason to adopt it. Also, mechanic watches and Gregorian calendars won't disappear anytime soon. But to me it's an idea worth thinking about. As an experiment, I implemented the [watch face][Reference Time] for Wear OS and started living on my personal reference time which resets to zero every morning when I wake up. Computers make different time zones much more manageable and I rarely have to manually transform one time system into the other, since the current time and the time until my next calendar event are always displayed on my watch. Several weeks into the experiment, I feel like even on Earth, having a time system that is just a little more personal and human-centered does make my day a bit easier and more enjoyable. And it's a nice ice-breaker.

[zach]: https://zachholman.com/talk/utc-is-enough-for-everyone-right
[bbc]: http://www.bbc.co.uk/programmes/b01dvw6t
[gps]: https://en.wikipedia.org/wiki/Error_analysis_for_the_Global_Positioning_System#Special_and_general_relativity
[xkcd#927]: https://xkcd.com/927/
[UTC]: https://en.wikipedia.org/wiki/Coordinated_Universal_Time
[Unix time]: https://en.wikipedia.org/wiki/Unix_time
[decimal time]: https://en.wikipedia.org/wiki/Decimal_time
[TAI]: https://en.wikipedia.org/wiki/International_Atomic_Time
[TAI64]: https://www.tai64.com/
[GPS]: https://en.wikipedia.org/wiki/Global_Positioning_System#Timekeeping
[second]: https://en.wikipedia.org/wiki/Second
[generation]: https://www.ncbi.nlm.nih.gov/pubmed/10677323
[Reference Time]: http://time.rtens.org/
[Kurzgesagt]: https://www.youtube.com/watch?v=czgOWmtGVGs
[Geoid]: https://en.wikipedia.org/wiki/Geoid
[start of civilization]: https://en.wikipedia.org/wiki/History_of_the_world#Rise_of_civilization
[relativity]: https://www.youtube.com/playlist?list=PLoaVOjvkzQtyjhV55wZcdicAz5KexgKvm