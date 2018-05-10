Status: draft

I used last Christmas break to watch "The Expanse" which quickly became my favorite SciFi series with its incredibly realistic and inspirational vision of a humanity that has colonized the solar system. And it was one sentence in this show that struck a unexpected chord with me. It was a comment about how - even decades after populating Mars and the asteroid belt - they still used earth-based units to measure time such as days, months and years. As probably almost every software developer, I struggled more than once with the convoluted dominant time system of this planet, and this comment got me once again thinking about how an alternative might look like.

The result is *[Reference Time]*, a time system designed for regularity, usability, and relativity. I uses decimal groups of seconds to count seconds elapsed since an arbitrary zero point, relative to a specific frame of reference.


## Design Goals

> "We have a choice: do we actually think, that the sun, the stars and the moon are important to our lives, or do we think that our lives should be controlled by intervals?" - [Kristen Lippincott][bbc]

What time system would make sense for a civilization that is not bound to a single planet anymore? What if the sun, the stars and the moon become indeed very unimportant? What if we start living in completely artificial environments were it makes much more sense to let intervals control our lives? What could time for a space faring civilization look like?

### Relativity

Time is relative. And not only in the sense that a second in a supermarket queue appears longer than on the beach, but also in a very physical sense. One of the most important predictions of Einstein's theory of General Relativity was that time behaves differently in different frames of reference, which is most impressively demonstrated by the fact that time on GPS satellites shifts about [38 microseconds][gps] per day compared to clocks on earth. While this time dilation can be calculated very precisely for satellites in a known orbit, it would be very difficult for a large number of vessels zipping through the solar system on unpredictable trajectories. So a space-age time system must incorporate the fact that every interval is always relative to a specific frame of reference, e.g. the surface of a planet, an orbit or a vessel.

Time is personal. While the thought of abolishing all timezones is tempting it is not compatible with reality where time is all but universal. Space exploration will only increase the number of timezones with different cycle lengths, time dilations and even people living on the same station but in different time zones to provide uninterrupted operations. A universal time system must therefore embrace the fact that everybody is following their own clocks, explicitly state the frame of reference plus offset, and make conversion between them as simple as possible.

### Regularity

To ease calculations, the time system needs to be as regular as possible. The notation of our current calendars and clocks use decimal place-value numbers but different bases for minutes, hours, days and weeks and even irregular lengths for months and years. And although base 24 and 60 make division easier, it comes at the cost of addition and subtraction which I think are the much more frequent operations on time. A regular time system uses the same base for all of its units and numbers.

Irregular units make calculations harder, but as long as the exceptions are predictable (e.g. leap years), they're still possible. A time system bound to natural phenomena will also include unpredictable discontinuations (e.g. leap seconds), which in the best case makes calculation impossible and in the worst case leads to contradictory results. A continuous time system avoids cyclic and sporadic exceptions.

### Usability

Relativity and regularity make a time system easier to use for machines, but it also has to be usable for humans. We need to be able to easily speak about time frames that are important to us. For people living in artificial environments, this may be different intervals than the natural cycles we use nowadays. A usable time system enables precise and efficient communication while avoiding ambiguity.


## Reference Time

I would like to propose a *time system for the space age*, which is not bound to the natural cycles of a single planet, but designed for **regularity**, **usability**, and embraces the **relative** nature of time which can only ever be measure relative to a frame of reference. *Reference Time* counts **[SI seconds][second]**, grouped into **decimal units**, relative to a **frame of reference**, that have lapsed since an arbitrary **zero point**. 

Instead of insisting on a single, universal time, in *Reference Time* a point of time is given as "I was born at 46 Rotations and 45 Cycles, Earth-time since 1970-01-01" or "We'll arrive at 42 Cycles and 21 Turns, Ship-time since mission start" or "The meeting starts at 97 Turns and 5 Moments, Station-time since start of shift".

### Units

To facilitate machine-to-human and human-to-human communication, seconds are grouped into decimal units. It happens to work out that groups of 100s (and one group of 10) lead to intervals that are likely to be meaningful to most humans.

- 100 Seconds are 1 *Moment* - a little less than 2 minutes and a good unit for business precision, e.g. for bus schedules or appointments.
- 10 Moments are 1 *Turn* - a little more than a quarter hour and a good unit for "social precision", e.g. meeting friends or starting dinner. It's also a nice unit for splitting up a working day, e.g. "this is gonna take 5 Turns".
- 100 Turns is 1 *Cycle* - little longer than a day (27.7 hours) and might be suitable for sleep cycles in artificial environments, if the human body is flexible enough.
- 100 Cycle is 1 *Rotation* - about a third of a year which seems like a good unit of time to track personal and professional progress or to plan projects. 
- 100 Rotations is 1 *Generation* - with 31.7 years very close to the [average time between human generations][generation] and the largest unit of time in the system, e.g. "the Roman empire fell 47 generations ago".

### Zero Points

Zero points are freely chosen and multiple clocks can be synchronized by broadcasting a reference description along with the number of seconds counted. Alternatively, a zero point can be defined in terms of external events or other time systems. For example "1st of January 1970", "next midnight UTC plus 2 hours", "last high sun in London", or even "when I got up today".

For an coordinated [Earth Reference Time][Reference Time] (ERT), we need a widely accepted, precise and continuous time signal. I picked the one emitted by the satellites of the [Global Positioning System][GPS], which uses the [Geoid] as its frame of reference. Regarding the zero point, I would follow the suggestion of [Kurzgesagt] and define ERT as GPS + 400000000000 seconds, which puts 0 ERT roughly at the [start of civilization].


## Other Time Systems

There are of course many many time systems already out there and you might (rightfully) have the strong desire to point me to [xkcd#927] by now. And maybe I simply had too much time on my hand over the holidays but none of the systems I could find meet the stated design goals. Let's have a quick look at some.

**Coordinated Universal Time** ([UTC]) is all but regular or predictable and also does not support different frames of references since time zones are defined by a fixed offset and depend more on arbitrary political decisions than location. A more regular version of UTC is **[Unix time]** which only counts seconds (skipping leap seconds) which makes it much less usable for humans.

Various **[decimal time]** systems tried to improve regularity, usually by dividing a day repeatedly by ten. These systems inherit all problems of whatever calendar they are bound to, and sacrifice ease of division for only a small facilitation of addition and subtraction. They also usually redefine the length of a "second".

The **International Atomic Time** ([TAI]) is continuous (by ignoring leap seconds) but apart from that as irregular as UTC. Unless you use a notation like [TAI64] which is extremely regular by counting only seconds but it still does not support different frames of reference and is unusable to anyone who needs units greater than seconds or who is not fluent in hexadecimal notation. The time of **[GPS] satellites** can be derived from TAI, but counts weeks and seconds instead of using the Gregorian calendar. Although this is an improvement over just counting seconds, it still doesn't make it human friendly.


## Reality Check

So what's this *Reference Time* actually good for? Probably not much. Living in a natural environment, there is little reason to adopt it. Also, mechanic watches and Gregorian calendars won't disappear anytime soon. But to me it's an idea worth thinking about. As an experiment, I started living on my personal reference time which starts at zero every morning when I wake up. Computers make time zones much more manageable and I rarely have to manually transform one time system into the other, since the current time and the time until my next calendar event are always displayed on my watch. And several weeks into the experiment, I feel like even on Earth, having a time system that is just a little more personal and human-centered does make my day easier.


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