---
title: ! 'CSMM - Lesson 1.4: Advanced Logic and Arithmetic in the Lambda Calculus'
date: 2012-06-29
tags: [csmm, lambda calculus, boolean logic, predicates, logic, arithmetic]

Where we were
-------------
Last time, we went over the basics of boolean logic and it's manifestation in the
\\(\lambda\\)-calculus.  This time, we'll move those basics into the realm of numbers
and start testing for things such as equality and difference.  We'll also see the 
first hint of a data structure: the pair.  And we'll provide the missing subtraction
function, along the way (division is still too difficult, but we'll get there in time).

A bit of review
---------------
Before we start this lesson, it's probably a good idea to collect the various
named functions we've encountered up until this point.

First, some basic ones:

$$I := \lambda x.x$$
$$\omega := \lambda x.xx$$
$$\Omega := \omega \omega$$

Next up, the Church numerals:

$$0 := \lambda sz.z$$
$$1 := \lambda sz.sz$$
$$2 := \lambda sz.s(sz)$$
$$3 := \lambda sz.s(s(sz))$$
$$...$$

And some arithmetic functions for working with Church numerals:

$$S := \lambda wyx.y(wyx)$$
$$+ := \lambda ab.aSb$$
$$\times := \lambda ab.a(+b)0$$
$$E := \lambda ab.ba$$

And finally, some boolean logic:

$$T := \lambda xy.x$$
$$F := \lambda xy.y$$
$$\neg := \lambda x.xFT$$
$$\land := \lambda xy.xyF$$
$$\lor := \lambda xy.xTy$$

Keep these handy, we'll be using most of them for the rest of the \\(\lambda\\)-calculus
lessons.

They come in twos
-----------------
Alright, moving on to pairs.  Pairs are useful for many things, and are fairly
simple to use in the \\(\lambda\\)-calculus.

As with everything else in the \\(\lambda\\)-calculus, a pair is just a function.
Say you wanted to make a pair containing \\(3\\) and \\(1\\).  The function representing
this pair would be as follows:

$$\lambda f.f31$$

There is a helper function to create such pairs, called \\(\Phi\\).  It is defined
like this:

$$\Phi := \lambda abf.fab$$

Such that creating the pair above would be as simple as:

$$\Phi 31$$
$$(\lambda abf.fab)31$$
$$(\lambda bf.f3b)1$$
$$\lambda f.f31$$

So we can see that we can write a pair of elements \\(x\\) and \\(y\\) as \\((\Phi xy)\\),
with the parentheses serving to ensure the correct associativity.

So, we know how to create pairs now.  How do we get their parts?  Turns out, we already
have the tools for this in the form of \\(T\\) and \\(F\\).  For example, to get the first
part of \\((\Phi 31)\\), we do the following:

$$(\Phi 31)T$$
$$((\lambda abf.fab)31)T$$
$$((\lambda bf.f3b)1)T$$
$$(\lambda f.f31)T$$
$$T31$$
$$(\lambda xy.x)31$$
$$(\lambda y.3)1$$
$$3$$

And to get the second, we do this:

$$(\Phi 31)F$$
$$((\lambda abf.fab)31)F$$
$$((\lambda bf.f3b)1)F$$
$$(\lambda f.f31)F$$
$$F31$$
$$(\lambda xy.y)31$$
$$(\lambda y.y)1$$
$$1$$

So, \\(T\\) extracts the first element of a pair, and \\(F\\) can pull out the second.
Neat.

So, why the seemingly random diversion?  Well... we're about to create a few functions
that use pairs to perform some tricky work.

What comes before...
--------------------
This section will actually step through two functions, one which takes in a pair
\\((m, n)\\) and returns \\((n, n+1)\\), and one which finds the predecessor of a
given Church numeral.

The first function, \\(\oplus\\), operates on pairs, providing a sort of climbing
upwards.

$$\oplus := \lambda x.\Phi(xF)(S(xF))$$

Let's test this out.  We're going to provide it the pair \\((\Phi 11)\\) and it
should return the pair \\((\Phi 12)\\).  As we've already seen how \\(F\\) works
on pairs and how \\(S\\) works on Church numerals, I will not be writing the complete
long-form of this \\(\beta\\)-reduction, rather I will be substituting results in
where they belong.

$$\oplus (\Phi 11)$$
$$(\lambda x.\Phi(xF)(S(xF)))(\Phi 11)$$
$$\Phi((\Phi 11)F)(S((\Phi 11)F))$$
$$\Phi(1)(S((\Phi 11)F))$$
$$\Phi(1)(S(1))$$
$$\Phi 12$$

And we see it works!  For good measure, let's plug that result in, hoping for 
\\((\Phi 23)\\).

$$\oplus (\Phi 12)$$
$$(\lambda x.\Phi(xF)(S(xF)))(\Phi 12)$$
$$\Phi((\Phi 12)F)(S((\Phi 12)F))$$
$$\Phi(2)(S((\Phi 12)F))$$
$$\Phi(2)(S(2))$$
$$\Phi 23$$

So, now we can increment a pair of numbers.  How does this help us?  Well, now
we have an easy way to find the predecessor of a Church numeral!  There are other
formulations for the predecessor function, but this one is in my opinion the easiest
to understand once you have the fundamentals down.  It's defined like this:

$$P := \lambda x.(x \oplus(\Phi 00))T$$

So... what does this function mean?  How does it work?

It takes in a single Church numeral, \\(x\\), and applies the \\(\oplus\\) function
\\(x\\) times to the pair \\((\Phi 00)\\), and then takes the resulting function and
returns the first element.  Applying the \\(\oplus\\) function to \\((\Phi 00)\\)
one time gives us \\((\Phi 01)\\), applying it another time (for a total of two
applications) to that result gives us \\((\Phi 12)\\), and applying it \\(x\\) times
will give us a result of \\((\Phi yx)\\), where \\(y\\) is the Church numeral 
immediately preceeding \\(x\\).  Taking the first element of this pair will give
us \\(y\\), the predecessor of \\(x\\)!

Here it is in action, finding the predecessor of \\(3\\).  Again, I've omitted
certain details, including the applications of \\(\oplus\\).

$$P3$$
$$(\lambda x.(x \oplus(\Phi 00))T)3$$
$$(3 \oplus(\Phi 00))T$$
$$(\oplus (\oplus (\oplus (\Phi 00))))T$$
$$(\oplus (\oplus (\Phi 01)))T$$
$$(\oplus (\Phi 12))T$$
$$(\Phi 23)T$$
$$2$$

It works!

One thing to note is that Church encoding has no concept of negative numbers.  Our
\\(P\\) function handles this in the following way:

$$P0$$
$$(\lambda x.(x \oplus(\Phi 00))T)0$$
$$(0 \oplus(\Phi 00))T$$
$$(\Phi 00)T$$
$$0$$

That is, the predecessor of \\(0\\) is \\(0\\).  This will come in handy later.

Subtraction, at last
--------------------
With \\(P\\) under our belt at last, subtraction is pretty easy to define now.

$$- := \lambda ab.bPa$$

This works much like \\(+\\) does, in that to perform \\(3-2\\), you're actually
trying to find the second predecessor of three.

$$-32$$
$$(\lambda ab.bPa)32$$
$$(\lambda b.bP3)2$$
$$2P3$$
$$P(P3)$$
$$P2$$
$$1$$

And it's done.  Simple as cake.

A foundational predicate
------------------------
Alright, we're going to define our first predicate, which is a function which performs
some sort of test on its inputs, and returns either a \\(T\\) or a \\(F\\).  The
predicate we are going to define will test whether or not a given Church numeral is
equal to \\(0\\).  It's defined like so:

$$Z := \lambda a.aF\neg F$$

Let's test it out:

$$Z0$$
$$(\lambda a.aF\neg F)0$$
$$0F\neg F$$
$$(\lambda sz.z)F\neg F$$
$$(\lambda z.z)\neg F$$
$$\neg F$$
$$T$$

So, it returns \\(T\\) if you provide it \\(0\\), as it should.  How about other
cases?

$$Z2$$
$$(\lambda a.aF\neg F)2$$
$$2F\neg F$$
$$(\lambda sz.s(sz))F\neg F$$
$$(\lambda z.F(Fz))\neg F$$
$$(F(F\neg))F$$
$$(F((\lambda xy.y)\neg))F$$
$$(F(\lambda y.y))F$$
$$(FI)F$$
$$((\lambda xy.y)I)F$$
$$(\lambda y.y)F$$
$$IF$$
$$F$$

So, testing on \\(2\\), it returns \\(F\\), as it should.  But why?

This again relies upon the inherent properties of the Church numerals.  If you provide
\\(Z\\) a Church numeral \\(N\\), then it applies \\(F\\) a total of \\(N\\) times
to \\(\neg\\).  But \\(F\\) applied to anything provides you \\(I\\), the identity
function.  For any number \\(N\\) which is not \\(0\\), \\(ZN\\) will simplify to
\\(IF\\), which simplifies to \\(F\\).  When \\(N\\) equals \\(0\\), on the other
hand, \\(F\\) is never applied, allowing \\(Z0\\) to simplify to \\(\neg F\\), which
by definition simplifies to \\(T\\).  Pretty beautiful, huh?

Why did we define this predicate?  We'll see soon.  It is vital in defining subtraction
and many other useful predicates we'll need later.

More predicates, in rapid succession!
-------------------------------------
Alright, with \\(Z\\) defined, we're ready to make some more predicates.  These
will all build off of one another in a natural progression, so they shouldn't be
too hard to absorb.

Let's start with something that utilizes \\(P\\)'s property that \\(P0 = 0\\).  
How about \\(\leq\\)?

$$\leq := \lambda ab.Z(-ab)$$

This tests whether \\(a\\) is less than or equal to \\(b\\), by subtracting \\(b\\)
from \\(a\\).  If \\(-ab\\) is \\(0\\), then we know that \\(b\\) must be equal to
or greater than \\(a\\).  Pretty simple.

Here it is showing that \\(3\\) is greater than \\(1\\)
$$\leq 31$$
$$(\lambda ab.Z(-ab))31$$
$$(\lambda b.Z(-3b))1$$
$$Z(-31)$$
$$Z2$$
$$F$$

And here it is showing that \\(1\\) is less than or equal to \\(1\\).

$$\leq 11$$
$$(\lambda ab.Z(-ab))11$$
$$(\lambda b.Z(-1b))1$$
$$Z(-11)$$
$$Z0$$
$$T$$

As you might imagine, \\(\geq\\) is pretty similar:

$$\geq := \lambda ab.Z(-ba)$$

I'm not going to show \\(\geq\\) in action, as it's extremely similar to \\(\leq\\).

With both \\(\leq\\) and \\(\geq\\), we can now test for equality!  Since \\(m = n\\)
if and only if \\(m \leq n\\) and \\(m \geq n\\), we have what we need to define \\(=\\).

$$= := \lambda ab.\land(\leq ab)(\geq ab)$$

Let's test it:

$$=12$$
$$(\lambda ab.\land(\leq ab)(\geq ab))12$$
$$(\lambda b.\land(\leq 1b)(\geq 1b))2$$
$$\land(\leq 12)(\geq 12)$$
$$\land T(\geq 12)$$
$$\land TF$$
$$F$$

And on one that should pass:

$$=44$$
$$(\lambda ab.\land(\leq ab)(\geq ab))44$$
$$(\lambda b.\land(\leq 4b)(\geq 4b))4$$
$$\land(\leq 44)(\geq 44)$$
$$\land T(\geq 44)$$
$$\land TT$$
$$T$$

Cool.  So, now with \\(\leq\\), \\(\geq\\) and \\(=\\), we can define the last
two predicates: \\(<\\) and \\(>\\).  They're no surprise, if you realize that
a \\(m < n\\) if and only if \\(m \leq m\\) and \\(\neg(m = n)\\).  \\(<\\) reflects 
this:

$$< := \lambda ab.\land(\neg(=ab))(\leq ab)$$

Let's give it a shot:

$$<23$$
$$(\lambda ab.\land(\neg(=ab))(\leq ab))23$$
$$(\lambda b.\land(\neg(=2b))(\leq 2b))3$$
$$\land(\neg(=23))(\leq 23)$$
$$\land(\neg F)(\leq 23)$$
$$\land T(\leq 23)$$
$$\land TT$$
$$T$$

How about equality?

$$<33$$
$$(\lambda ab.\land(\neg(=ab))(\leq ab))33$$
$$(\lambda b.\land(\neg(=3b))(\leq 3b))3$$
$$\land(\neg(=33))(\leq 33)$$
$$\land(\neg T)(\leq 33)$$
$$\land F(\leq33)$$
$$\land FT$$
$$F$$

Again, as you probably have guessed, \\(>\\) is much the same:

$$> := \lambda ab.\land(\neg(=ab))(\geq ab)$$

And with that, we have everything we need to keep moving closer to an actual program
in the \\(\lambda\\)-calculus!

Wrapping up
-----------
We sure blew through a lot of material with this lesson, and I hope it wasn't too
much.  But if you've been following along with the previous lessons, nothing here
should be too tricky to figure out with a bit of study.

I've posted your homework [here](https://github.com/gatesphere/blog-resources/raw/master/downloads/csmm/lesson1-4.pdf).

See you soon for lesson 1.5!

Next lesson: [here](/2012/07/03/csmm---lesson-15-flow-control-and-recursion-in-the-lambda-calculus/)