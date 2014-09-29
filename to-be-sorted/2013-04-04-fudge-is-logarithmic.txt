---
date: 04/04/2013
tags: fudge, rpg, fate, dice, math, simulations, code-dump
title: Fudge is logarithmic

Hello all,

I thought I'd take a second and explain something that I once read about
the tabletop RPG ruleset [Fudge](http://fudgerpg.com/).  A while back, I 
was looking for some space opera inspiration for a Fudge game I was going 
to run (though, it ended up taking a very different direction!), when I 
came across a set of draft rules called, appropriately, [Fudge Space Opera](http://www.sonic.net/~rknop/php/Omar/fudge/spop/spop_0.3.0.pdf).
Right in the introduction, it states:

>Fudge ... is intrinsically a logarithmic system (although you don’t need 
>to know that to play it!), and that together with the Scale mechanic lets 
>you elegantly renormalize yourself to any range of sizes.

Now, I knew what the author was getting at here - the attribute scale
in Fudge is not linear as it seems.  In the Fudge rules, chapter 2, section
2.31, Strength and Scale are discussed.  Regarding relative strengths,
the rules state:

>Each level of Strength (from Terrible to Superb) is defined to be 1.5 times 
>stronger than the previous level. A character with Good Strength is thus 1.5 
>times as strong as a character with Fair Strength.

And then further, about scale:

>Strength Scale increases in the same way: a Scale 1, Fair Strength individual 
>is 1.5 times stronger than a Scale 0, Fair Strength individual. This holds for 
>each increase in Scale: a Scale 10 Superb Strength creature is 1.5 times stronger 
>than a Scale 9 Superb Strength creature, for example.

So here, the rules give us two dimensions that act in a similar manner to increase
a variable by a relative degree.  If we were to give that variable a numerical 
value, starting at 1 for Terrible, Scale 0, and draw curves representing the
values at Scales 0 through 10, we'd get the following graph:

![Fudge power scales](https://rawgithub.com/gatesphere/blog-resources/master/images/fudge-power-scales.svg)

Each different colored line is a different scale, and each of the points on the 
x-axis is a trait rating, on the standard Fudge Terrible ... Superb ladder.

So, what does this graph tell us?

We see that the curves tend to diverge more wildly from each other at the far 
right of the graph, whereas they're more similar on the far left.  This fits the
profile for an exponential relationship.  Systems which are rated on a linear
scale overlaying an exponential true-value are logarithmic in nature.

Fudge is logarithmic.

It's simple things like this that make me truly appreciate the power of multiplication
when describing phenomena.

If you're curious, the graph was generated with [PLOTlet](http://www.plotlet.com/),
with data provided by a small Leo script, available on [gist](https://gist.github.com/gatesphere/fd9939474a5c5bb17da2).

Thanks for reading!