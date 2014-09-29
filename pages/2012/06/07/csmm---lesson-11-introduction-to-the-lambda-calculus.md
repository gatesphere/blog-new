---
title: ! 'CSMM - Lesson 1.1: Introduction to the Lambda Calculus'
date: 07/06/2012
tags: lambda calculus, csmm

Hello everyone.

Today marks the first lesson in the "Computer Science for Mere Mortals" lecture series.  In this lesson, we'll go over the basics of the \\(\lambda\\)-calculus, preparing you for some more advanced work in the next lesson.

So, where to begin?

What is the \\(\lambda\\)-calculus?
-----------------------------------
Well, simply put, the \\(\lambda\\)-calculus is a formal mathematical system which consists solely of applying functions to each other.  Everything in the pure \\(\lambda\\)-calculus is a function, including numbers and truth values.  But more on that later.  First, some basics.

Functions and Variables
-----------------------
A good starting place to learning the \\(\lambda\\)-calculus is discussing the definitions of the terms function and variable.

In general terms, a variable is a placeholder for something else.  In the \\(\lambda\\)-calculus, that's as much as you need to know about variables, for the most part.  We'll get into bound vs. free variables later, but for know, just think about variables as holding a spot for something.

A function is a rule for taking one or more things and converting them to another thing.  In the \\(\lambda\\)-calculus, functions operate on functions to create new functions.  Think "I N C E P T I O N".

Simple enough, right?

A look at a simple function
---------------------------
Alright, let's look at a simple function in normal mathematical notation, the identity function.  This is a function which simply returns whatever you give it.  In normal mathematical notation, it looks like this:

$$f(x) = x$$

Where \\(f\\) is the function name, and \\(x\\) is some variable that it works upon.  In the \\(\lambda\\)-calculus, the same function would be written as follows:

$$\lambda x.x$$

And would be read something like "\\(x\\) maps to \\(x\\)".  There are a few things to notice here, first and foremost is that the function has no name (i.e., it's not called \\(f\\) anymore).  Secondly, there are a few interesting things going on with this notation.  Turns out, in the \\(\lambda\\)-calculus, only four symbols have any defined meaning, and they are as follows:

  * \\(\lambda\\) - "this is a function"
  * \\(.\\) - "maps to"
  * \\((\\) and \\()\\) - for grouping and overriding associativity

For simplicity when manipulating these functions, people working with the \\(\lambda\\)-calculus often give these functions equivalent placeholder symbols.  For the purposes of my lessons, I will write such definitions as follows:

$$I := \lambda x.x$$

This states that the symbol \\(I\\) is just a placeholder for the \\(\lambda\\)-expression \\(\lambda x.x\\).  Wherever we can write that expression, we can now write the simpler and shorter \\(I\\), and vice-versa.

It's also worth noting now a property of functions in the \\(\lambda\\)-calculus.  Variable names are inconsequential so long as ordering remains the same within a given \\(\lambda\\)-expression, such that \\(\lambda x.x = \lambda a.a\\).  This is called \\(\alpha\\)-equivalence.

A first function application
----------------------------
So, in the \\(\lambda\\)-calculus, to apply a function to another function, you simply concatenate them (place them next to each other).  For example, in the following example, I will be applying the generic variable \\(a\\) to the identity function, \\(I\\).  This is written like this:

$$Ia$$

To figure out what the value of this expression is, we should replace \\(I\\) with it's long-form companion:

$$(\lambda x.x)a$$

Now, we have a function which takes a single variable, and a value which to give it.  We use \\(a\\) for the value \\(x\\), and we get the following result:

$$a$$

As you can see, \\(Ia = a\\), so it acts as the identity function should.  What we just did is called a \\(\beta\\)-reduction, one of the few operations that the \\(\lambda\\)-calculus uses to provide all of it's various facilities.  \\(\beta\\)-reduction is simply the process of simplifying the \\(\lambda\\)-expressions we are working with.  When an expression can no longer be simplified, it is said to be in "normal form".

Another example, for kicks
--------------------------
To play around with this a bit more, and for practice, let's apply \\(I\\) to itself.  The result is as follows:

$$II$$
$$(\lambda x.x)I$$
$$I$$

So, here we see that the identity function applied to itself gives us the identity function.  This is no surprise, since it simply gives us back what we put in.

Getting tricky: functions of multiple variables
-----------------------------------------------
So, functions of more than one variable in the \\(lambda\\)-calculus work just as you would expect them to work.  For example, here's a function which takes two arguments and returns them in the opposite order:

$$\lambda xy.yx$$

Applying this to two variables \\(a\\) and \\(b\\), we get:

$$(\lambda xy.yx)ab$$
$$(\lambda y.ya)b$$
$$ba$$

No surprises, right?

Well, this actually demonstrates an important concept in the \\(\lambda\\)-calculus, called Currying.

Making things simpler: Currying
-------------------------------
Currying, named after Haskell Curry, the mathematician who first wrote about the concept, is a rather simple idea.  Basically, Curry proved that when dealing with functions of multiple variables, it is *always* possible to decompose said function into multiple functions, each of a single variable.  For example, take the following function in mathematical notation:

$$f(x,y) = x + y$$

Given \\(3\\) and \\(4\\), we get:

$$f(3,4) = 3 + 4 = 7$$

This function can be rewritten as the composition of two functions:

$$g(x) = x + h(y), h(y) = y$$

Given the same \\(3\\) and \\(4\\), we can see that the functions are equivalent:

$$g(3) = 3 + h(y)$$
$$3 + h(4) = 3 + 4 = 7$$

In the \\(\lambda\\)-calculus, it turns out that Currying is dreadfully simple.  Taking the function above, it can be shown that the following are equivalent:

$$\lambda xy.yx = \lambda x.\lambda y.yx$$

To prove it, here is the full application of the same \\(a\\) and \\(b\\) to the second (Curried) form:

$$(\lambda x.\lambda y.yx)ab$$
$$(\lambda y.ya)b$$
$$ba$$

Because the normal form of this version is the same the normal form of the original version (as demonstrated in the previous section), the are equivalent.  In other words, it could simply be stated that \\(\lambda abc.cab\\) is *shorthand* for writing \\(\lambda a.\lambda b.\lambda c.cab\\).

A note about associativity
--------------------------
The previous section ended with a note on shorthand.  There is one other convention in the \\(\lambda\\)-calculus that is shorthand, and that is the assumption of left-associativity.  The following expressions are equivalent:

$$abcdefg = ((((ab)c)d)e)f$$

The parentheses are often left off when writing things down so as to save time and space.  However, when they are used, pay special attention to them, because they often override the assumed left-associativity.  One example is the following function:

$$\lambda wyx.y(wyx) = \lambda wyx.y((wy)x)$$

Here we see that \\(w\\) and \\(y\\) are associated with each other, then \\(x\\) is associated with that quantity, and finally \\(y\\) is associated with the whole quantity.  However, the same function sans parentheses tells a different story:

$$\lambda wyx.ywyx = \lambda wyx.((yw)y)x$$

Depending upon what is provided for \\(w\\), \\(y\\), and \\(x\\), these two forms may very well have extremely different normal forms, and therefore not be equivalent forms.

A few diversions: \\(\omega\\) and \\(\Omega\\)
-----------------------------------------------
Now I'd like to introduce a few functions: first \\(\omega\\) (the lowercase Greek letter omega), and then \\(\Omega\\) (the uppercase Greek letter omega).  Why use the same symbol in different cases to represent the two functions?  Because one is defined in terms of the other!  But enough about that for now.  First, \\(\omega\\).

$$\omega := \lambda x.xx$$

So, \\(\omega\\) takes a single variable, and produces two of that variable, or in other words, that variable *applied to itself*.  This is incredibly cool.  As an example, here's \\(I\\) applied to \\(\omega\\):

$$\omega I$$
$$(\lambda x.xx)I$$
$$II$$
$$(\lambda x.x)I$$
$$I$$

It produced \\(I\\) applied to \\(I\\), which further reduced to simply \\(I\\) (remember, \\(I\\) simply repeats what it is given).

So, what about \\(\Omega\\)?  Here's the definition:

$$\Omega := \omega \omega$$

So, \\(\Omega\\) is \\(\omega\\) applied to itself.  What is the normal form of \\(\Omega\\)?

$$\omega \omega$$
$$(\lambda x.xx)\omega$$
$$\omega \omega$$
$$(\lambda x.xx)\omega$$
$$\omega \omega$$
$$...$$

It reduces forever, without ever coming to a stop!  Such a function is said to have no normal form.  Another interesting property of \\(\Omega\\) is that it will *never* respond to another function being applied to it, due to the left-association rule.  This means that an expression like \\(\Omega I\\) also will not have a normal form.  To prove it to yourself, give it a shot.

Getting ahead of ourselves
--------------------------
Okay, so what I've given you thus far is the basics of the \\(\lambda\\)-calculus.  Before we get too far ahead, I'd like to take this opportunity to provide some homework for you.  It's not much, just 8 simple questions, but you should be prepared to work them out by paper and pencil until you're satisfied with your results.  Don't fret too much though, answers are also provided.

The homework is available as a PDF file, and it you can view it [here](https://github.com/gatesphere/blog-resources/raw/master/downloads/csmm/lesson1-1.pdf).  Answers are on the last page.

Closing
-------
Hope you've enjoyed this!  In the next session, we'll learn a bit about arithmetic and how to represent numbers in the form of a function.

Next lesson: [here](/2012/06/14/csmm---lesson-12-arithmetic-in-the-lambda-calculus/)