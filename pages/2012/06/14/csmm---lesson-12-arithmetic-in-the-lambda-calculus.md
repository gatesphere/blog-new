---
title: ! 'CSMM - Lesson 1.2: Arithmetic in the Lambda Calculus'
date: 14/06/2012
tags: csmm, lambda calculus, arithmetic

Where we left off
-----------------
Welcome back.  This is lesson two in the \\(\lambda\\)-calculus unit.  Last time
we left off discussing the basics of working with the \\(\lambda\\)-calculus, including
some interesting functions.  This time, we'll move forward into the universe of 
representing numbers and arithmetic in \\(\lambda\\) terms. Fun stuff.  So, let's 
get started!

Church notation for numerals
----------------------------
Alonzo Church, the progenitor of the \\(\lambda\\)-calculus, devised a wonderful
way of encoding the natural numbers as \\(\lambda\\) terms.  Here are the first
few numbers in what is known as "Church encoding":

$$0 := \lambda sz.z$$
$$1 := \lambda sz.sz$$
$$2 := \lambda sz.s(sz)$$
$$3 := \lambda sz.s(s(sz))$$

As you can probably see, the pattern is pretty simple: a number of occurrences of
\\(s\\) which is equal to the number being represented, followed by a single \\(z\\),
all of which is right-associative.  Using this, we can easily define any of the natural
numbers.  Here's \\(6\\) for example:

$$6 := \lambda sz.s(s(s(s(s(sz)))))$$

It's long and tedious, but we could define any natural number in this fashion.  \\(100\\)
would be 100 \\(s\\)'s followed by a single \\(z\\).

Explanation of the encoding scheme
----------------------------------
Why did Church choose this way of encoding numerals?  Well, it's actually quite
ingenious.  Providing a function as the first term to a number \\(n\\) encoded in Church 
encoding applies that function \\(n\\) times to the second term.  Let's see an example\
(remembering the definition of \\(I\\) from the previous lesson):


$$3Ic$$
$$(\lambda sz.s(s(sz)))Ic$$
$$(\lambda z.I(I(Iz)))c$$
$$I(I(Ic))$$
$$I(Ic)$$
$$Ic$$
$$c$$

This example is pretty mundane, but it gets the point across.  The identity function
was applied to \\(c\\) three times, finally reducing to \\(c\\).  We will use this
property in defining addition and multiplication.

The successor function
----------------------
This next function is fundamental to Church encoding, as it will allow us to derive
*any* Church numeral so long as we start with a definition of \\(0\\).  This function
is called the successor function, and it's defined as follows:

$$S := \lambda wyx.y(wyx)$$

Judging from the name, it's a safe bet to assume that this function gives us the
Church numeral that immediately follows the one it is given.  Let's try this out 
(careful, this is the most tricky derivation we've done yet... follow closely):

$$S0$$
$$(\lambda wyx.y(wyx))0$$
$$\lambda yx.y(0yx)$$
$$\lambda yx.y((\lambda sz.z)yx)$$
$$\lambda yx.y((\lambda z.z)x)$$
$$\lambda yx.y(x) = \lambda yx.yx = \lambda sz.sz = 1$$

That last line has a few tricky points.  First, the parentheses are removed as per
convention, then \\(\alpha\\)-equivalence states that \\(y\\) and \\(x\\) can be 
rewritten as \\(s\\) and \\(z\\), and finally we see that this is equivalent to \\(1\\).
We gave \\(S\\) the Church numeral \\(0\\) and it provided us with the Church numeral
\\(1\\), the successor to \\(0\\).  This property of \\(S\\) holds true for any Church
numeral you provide to \\(S\\), allowing us to derive *every* natural number from
only \\(S\\) and \\(0\\)!

Adding things together
----------------------
At this point, we have everything we need to define addition.  How?  Well, it's 
actually pretty simple if you stretch your mind a bit and think of addition only
in the realm of natural numbers.  How do you add two numbers?  For example, two 
and three... you're finding the **second number** *after* **three**, or the *second
successor of three*.

We already have \\(S\\), so we're in luck!  Adding two and three together is as
simple as the following:

$$2S3$$
$$(\lambda sz.s(sz))S3$$
$$(\lambda z.S(Sz))3$$
$$S(S3)$$
$$S(4)$$
$$5$$

Here, I'm assuming that \\(S\\) works, and not bothering to write out the long-form
of the reduction.  Verifying that this is true is left as an exercise to the reader,
if you wish to gain more practice in long-form reduction.  I'm also using the property
of Church numerals such that the numeral \\(n\\) applies it's first term \\(n\\) times
to the second term.

So, There's addition.  Just because we can, we should define a function for addition.
Let's call it \\(+\\):

$$+ := \lambda ab.aSb$$

This function takes two variables, and adds them together using the same technique
we used above.  Now, we can add two and three like so:

$$+23$$

And it will work as expected.  Try it!

Multiplication
--------------
Now we're moving along nicely.  How about multiplication?  Again, we have everything
we need already at our disposal.  Think about multiplying two natural numbers.  Let's
use two and three again, for example's sake.  When multiplying two by three, we're actually
seeing what the value would be of *adding* **two** *to zero* **three times** and summing 
it all together, or vice-versa. A bit convoluted, I know, but hear me out.  Here's 
what I'm trying to explain in traditional mathematical notation:

$$2 \times 3 = (2+0) \times 3 = (2+0) + (2+0) + (2+0) = 2 + 2 + 2 = 6$$

How about this:

$$3(+2)0$$
$$(\lambda sz.s(s(sz)))(+2)0$$
$$(\lambda z.(+2)((+2)((+2)z)))0$$
$$(+2)((+2)((+2)0))$$
$$(+2)((+2)2)$$
$$(+2)4$$
$$6$$

Note the parentheses, and their effect upon associativity.

For completeness, let's define a multiplication function too, called \\(\times\\):

$$\\times := \lambda ab.a(+b)0$$

Exponentiation
--------------
Turns out, exponentiation is much simpler than multiplication, in theory.  Since 
the Church numerals have the application property that I've mentioned a few times, where
they apply their first term multiple times, exponentiation is pretty straightforward.

Let's attempt this with one and two, for simplicity.  We'll do both one squared and 
two to the first, to show that the different results are adequately represented.

To take the \\(b\\)th power of \\(a\\), the application is simple:

$$ba$$

That is, just reverse the typical written order of the numbers.  one squared is:

$$21$$
$$(\lambda sz.s(sz))1$$
$$(\lambda z.1(1z))$$
$$(\lambda z.1((\lambda ab.ab)z))$$
$$(\lambda z.1(\lambda b.zb))$$
$$(\lambda z.(\lambda cd.cd)(\lambda b.zb))$$
$$(\lambda z.(\lambda d.(\lambda b.zb)d))$$
$$(\lambda z.(\lambda d.zd))$$
$$\lambda zd.zd = 1$$

And here's two to the first:

$$12$$
$$(\lambda sz.sz)2$$
$$\lambda z.2z$$
$$(\lambda z.(\lambda ab.a(ab))z)$$
$$(\lambda z.(\lambda b.z(zb)))$$
$$\lambda zb.z(zb) = 2$$

For completeness, here's the \\(E\\) function:

$$E := \lambda ab.ba$$

The first example would be written \\(E12\\) and the second \\(E21\\).

*(edit: the \\(E\\) function above was originally called \\(P\\), but was renamed
to avoid a conflict with lesson 1.4)*

Wrapping it up
--------------
We've covered basic arithmetic in the \\(\lambda\\)-calculus today, and we have
begun to see the power that this simple system holds within it.  In the next lesson,
we'll cover the basics of boolean logic.  Stay tuned!

Alright, that's more than enough for today.  Your homework is available
[here](https://github.com/gatesphere/blog-resources/raw/master/downloads/csmm/lesson1-2.pdf) (PDF).  8 questions, answers on the second
page, as last time.

It's been great, hope you agree. :)

Next lesson: [here](/2012/06/26/csmm---lesson-13-boolean-logic-in-the-lambda-calculus/)