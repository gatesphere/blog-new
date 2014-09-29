---
title: ! 'CSMM - Lesson 1.5: Flow-control and Recursion in the Lambda Calculus'
date: 2012-07-03
tags: [csmm, lambda calculus, recursion, flow-control, fibonacci]

Remind me again?
----------------
Last time we left off with some high-level topics in the \\(\lambda\\)-calculus,
and this time we'll build upon them with two last concepts, and finally a functioning
program in the \\(\lambda\\)-calculus!  Be sure to refer to the previous lessons
for the definitions of functions, we're going to need them.  Let's get started.

Flow-control
------------
An important thing to be able to do in a computer program is make decisions based
on the state of some information.  In computer science, this is known as *flow-control*,
because it controls the flow of instructions.  The most simplistic (and indeed
elementary) model of flow-control is the *if-then-else* statement.

If-then-else is a simple instruction that checks the truth of a statement, and 
does one thing if it's true, and something else if it's false.  For example,
when deciding whether or not to go out to dinner, you could make the following
decision:

    if (I have enough money to go out) 
      then [go out to eat] 
      else [stay in tonight].
    
Thanks to our handy \\(T\\) and \\(F\\) functions, if-then-else is a piece of cake
in the \\(\lambda\\)-calculus:

$$G := \lambda abc.abc$$

Where \\(a\\) is some statement whose truth you are testing, \\(b\\) is what to
do if \\(a\\) is true, and \\(c\\) is what to do if \\(a\\) is false.  Here's
an example:

$$G(Z2)13$$
$$(\lambda abc.abc)(Z2)13$$
$$(\lambda bc.(Z2)bc)13$$
$$(\lambda c.(Z2)1c)3$$
$$(Z2)13$$
$$F13$$
$$3$$

This works because of the inherent functionality of \\(T\\) and \\(F\\), such
that \\(T\\) will return the first input it is given, and \\(F\\) will return
the second.  Should the \\(a\\) term evaluate to \\(T\\), the first branch is
evaluated, otherwise \\(a\\) is \\(F\\), so the second branch is evaluated.

Simple, right?

Recursion
---------
Moving on from if-then-else, we have another model of flow-control called recursion.
Recursion is defining something in terms of itself, and used correctly it's a very
powerful tool.  The poster-child example for recursion is the factorial (\\(!\\))
function in mathematics, whereby you can find the value of \\(5!\\) as follows:

$$5!$$
$$5(4!)$$
$$5(4(3!)$$
$$5(4(3(2!)))$$
$$5(4(3(2(1!))))$$
$$5(4(3(2(1(0!)))))$$
$$5(4(3(2(1(1)))))$$
$$5(4(3(2(1))))$$
$$5(4(3(2)))$$
$$5(4(6))$$
$$5(24)$$
$$120$$

In other words, \\(n! = n(n-1)!\\).  It is important to note here that every
recursive definition needs a *base case*, or a place for the recursion to 
stop.  With the factorial function, the base case is \\(0! = 1\\).  Without this
base case, the function would have recurred forever (so called *infinite recursion*)
and entered undefined territory (I dare you to find a real number that equals
\\(-1!\\))!  Unterminated recursion is almost always a bad thing, so be sure
to define things with a base case that will *always* be triggered when you
are looking to define something recursively.

What does recursion look like in the \\(\lambda\\) calculus?  Well... it's ugly.
We can't just define something in terms of itself, because we need a base case.
For example, what is the normal form of \\(X := \lambda a.aX\\)?  There is none,
as it will forever rewrite itself!

To get around this, we use what is called the the *Y-combinator*, but what it's
called isn't important.  What you should pay attention to is what it does.  First,
a definition:

$$Y := \lambda a.(\lambda b.a(bb))(\lambda b.a(bb))$$

Let's apply it to some generic function, \\(z\\).  It doesn't matter what \\(z\\)
is, the results are the same.

$$Yz$$
$$(\lambda a.(\lambda b.a(bb))(\lambda b.a(bb)))z$$
$$(\lambda b.z(bb))(\lambda b.z(bb))$$
$$z((\lambda b.z(bb))(\lambda b.z(bb)))$$
$$z(Yz)$$

This might be a bit confusing to understand just looking at the notation, but
basically what \\(Y\\) does is it provides a way for a function to repeat itself.
We provided \\(z\\) to \\(Y\\), and ended up with \\(z\\) applied to \\(Yz\\) again.
With \\(Y\\), and \\(G\\) from the previous section, we are able to provide a safe
way to define functions recursively!

To prove this, let's move on to writing our first program: a fibonacci number
generator.

Fibonacci, recursively
----------------------
The Fibonacci number sequence is a sequence of integers defined with the following
rules:

$$f(0) = 1$$
$$f(1) = 1$$
$$f(n) = f(n-1) + f(n-2)$$

That is, each number in the Fibonacci sequence is the sum of the two numbers that
proceeded it.  This makes the first few numbers in the sequence \\(1,1,2,3,5,8,13,21,...\\).
Simple enough, right?

Well, sense we have a nice recursive definition above, let's try to transform that
into the \\(\lambda\\)-calculus.  This is going to use many of the topics we've
covered up until this point, so take this section slowly and carefully.

Here's our Fibonacci function, written in a slightly unfamiliar way.

$$\chi := \lambda rn.G(\lor(=n0)(=n1))1(+(r (-n1))(r (-n2)))$$

So, here we have a function that takes two inputs, \\(r\\) which is eventually to
be \\(Y\chi\\), and \\(n\\), an index into the Fibonnaci number sequence, such that
if \\(n\\) were \\(5\\), \\(\chi\\) would return \\(8\\).

Why the \\(r\\) in \\(\chi\\)?  Well, we're going to be using \\(Y\\) here, and
\\(Y\\) applied to anything (as seen above) will always return another copy
of that anything.  Our function needs to be able to accept that copy and do 
something useful with it.

So, to calculate the second Fibonacci number, we do this:

$$(Y\chi)2$$
$$\chi(Y\chi)2$$
$$(\lambda rn.G(\lor(=n0)(=n1))1(+(r (-n1))(r (-n2))))(Y\chi)2$$
$$(\lambda n.G(\lor(=n0)(=n1))1(+((Y\chi)(-n1))((Y\chi)(-n2))))2$$
$$G(\lor(=20)(=21))1(+((Y\chi)(-21))((Y\chi)(-22)))$$
$$(\lor FF)1(+((Y\chi)1)((Y\chi)0))$$
$$F1(+((Y\chi)1)((Y\chi)0))$$
$$+((Y\chi)1)((Y\chi)0)$$
$$+(\chi(Y\chi)1)((Y\chi)0)$$
$$+((\lambda rn.G(\lor(=n0)(=n1))1(+(r (-n1)(r (-n2)))))(Y\chi)1)((Y\chi)0)$$
$$+((\lambda n.G(\lor(=n0)(=n1))1(+((Y\chi)(-n1))((Y\chi)(-n2))))1)((Y\chi)0)$$
$$+(G(\lor(=10)(=11))1(+((Y\chi)(-11))((Y\chi)(-12))))((Y\chi)0)$$
$$+((\lor FT)1(+((Y\chi)0)((Y\chi)0)))((Y\chi)0)$$
$$+(T1(+((Y\chi)0)((Y\chi)0)))((Y\chi)0)$$
$$+1((Y\chi)0)$$
$$+1(\chi(Y\chi)0)$$
$$+1((\lambda rn.G(\lor(=n0)(=n1))1(+(r (-n1)(r (-n2)))))(Y\chi)0)$$
$$+1((\lambda n.G(\lor(=n0)(=n1))1(+((Y\chi) (-n1))((Y\chi) (-n2))))0)$$
$$+1(G(\lor(=00)(=01))1(+((Y\chi) (-01))((Y\chi) (-02))))$$
$$+1((\lor TF)1(+((Y\chi)0)((Y\chi)0)))$$
$$+1(T1(+((Y\chi)0)((Y\chi)0)))$$
$$+11$$
$$2$$

Now, that's a lot of work, but as you can see, it does give the correct answer!
It should work for any other value of \\(n\\) you wish to try as well.  I will
assign a few more in your homework, to get you used to working with \\(Y\\).

Fibonacci, iteratively
----------------------
So... all of that work, and it turns out that there's a much easier way to find
Fibonacci numbers in the \\(\lambda\\)-calculus.  Call me a bully, but I wanted
to use that previous example to show you the power of \\(Y\\).  There are some
things that can *only* be accomplished recursively, and \\(Y\\) is your go-to
function when you need things done that way.  But sometimes there are simpler ways
to go about seemingly difficult problems, and Fibonacci numbers show this.

I'm going to present an iterative method for finding Fibonacci numbers, based upon
our work with \\(P\\).  In fact, the approach is going to be nearly identical.

First, we'll need a "ladder" function that will map a pair \\((m, n)\\) to the
pair \\((n, m+n)\\).  This is simple enough.

$$\delta := \lambda x.\Phi(xF)(+(xT)(xF))$$

Let's test it:

$$\delta(\Phi 23)$$
$$(\lambda x.\Phi(xF)(+(xT)(xF)))(\Phi 23)$$
$$\Phi((\Phi 23)F)(+((\Phi 23)T)((\Phi 23)F))$$
$$\Phi 3(+23)$$
$$\Phi 35$$

It works!

Now comes a slight cognitive leap.  To find the \\(n\\)th Fibonacci number, you'll
need to do \\(\delta\\) a total of \\(n\\) times to the pair \\(\Phi 01\\), and then
take the second element of that pair. Hmm.  How about this:

$$\chi_1 := \lambda n.(n\delta(\Phi 01))F$$

Let's find the fifth Fibonnaci number, which should be \\(8\\).

$$\chi_1 5$$
$$(\lambda n.(n\delta(\Phi 01))F)5$$
$$(5\delta(\Phi 01))F$$
$$((\lambda sz.s(s(s(s(sz)))))\delta(\Phi 01))F$$
$$((\lambda z.\delta(\delta(\delta(\delta(\delta z)))))(\Phi 01))F$$
$$(\delta(\delta(\delta(\delta(\delta (\Phi 01))))))F$$
$$(\delta(\delta(\delta(\delta(\Phi 11)))))F$$
$$(\delta(\delta(\delta(\Phi 12))))F$$
$$(\delta(\delta(\Phi 23)))F$$
$$(\delta(\Phi 35))F$$
$$(\Phi 58)F$$
$$8$$

Hooray!

Wrapping up
-----------
And with that, we've covered about everything that I wanted to cover with the 
\\(\lambda\\)-calculus.  We've gone from humble beginnings to writing our first
program (in two ways!) in five short lessons.  I hope this hasn't been too
much of a whirlwind tour for you.

As always, I have some homework for you, dealing with the things we've discussed
in this lesson.  It's available [here](https://github.com/gatesphere/blog-resources/raw/master/downloads/csmm/lesson1-5.pdf).

Next time
---------
Next time, we go abstract.  Away from the realm of doing things and towards the
realm of how to do things.  We'll learn what formal languages and grammars are,
which define the realm of computing in several ways.  See you soon!