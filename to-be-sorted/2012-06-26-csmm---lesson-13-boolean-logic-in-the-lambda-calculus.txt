---
title: ! 'CSMM - Lesson 1.3: Boolean Logic in the Lambda Calculus'
date: 26/06/2012
tags: csmm, lambda calculus, boolean logic, predicates, logic

Welcome back
------------
Last time we left off with basic arithmetic in the \\(\lambda\\)-calculus.  In this
lesson, we'll show the fundamental building blocks for boolean logic, which will 
be vitally important as we approach our first program!  Let's get started.

Truth values
------------
Before we get into the nitty gritty, I'm going to briefly explain the basics of
boolean logic.  If you have a good handle on mathematical logic, feel free to skip
this section completely.

So, what is boolean logic?  To be concise, it's the field of mathematical logich
where every statement has a value of either true, or false, with no in between.
Boolean logic, so named after George Boole, allows us to evalute the truth of statements
by combining these truth values with very simple operators which have well-defined
return values--in other words, functions.

So, we have two values (\\(T\\) for true, and \\(F\\) for false), and a number of
operators.  Which operators?  We'll start with negation (\\(\neg\\)).

The \\(\neg\\) operator simply negates whatever it is applied to.  \\(\neg T = F\\)
and \\(\neg F = T\\).  Simple, right?

The and (\\(\land\\)) operator takes two operands, and returns \\(T\\) only if
both operands are \\(T\\), otherwise it returns \\(F\\).  Here's  all possible
combinations:

$$T \land T = T$$
$$T \land F = F$$
$$F \land T = F$$
$$F \land F = F$$

The or (\\(\lor\\)) operator also takes two operands, and returns \\(T\\) if either
of the operands are \\(T\\), or both are \\(T\\), and returns \\(F\\) only if both
operands are \\(F\\).  Here's the full defintion:

$$T \lor T = T$$
$$T \lor F = T$$
$$F \lor T = T$$
$$F \lor F = F$$

Using these three operators, we can figure out rather complex statements.  For example:

$$\neg (T \land \neg ((T \lor F \lor T) \land F))$$
$$\neg (T \land \neg ((T \lor T) \land F))$$
$$\neg (T \land \neg (T \land F))$$
$$\neg (T \land \neg F)$$
$$\neg (T \land T)$$
$$\neg T$$
$$F$$

Some abstraction
----------------
So, now we're ready to start with boolean logic in the \\(\lambda\\)-calculus.  A
good place to start--indeed, the only place to start--is how to define the truth
values.  As with everything else in the \\(\lambda\\)-calculus, \\(T\\) and \\(F\\)
are simply functions.  And, as a bonus, you already know \\(F\\)!

$$F := \lambda xy.y$$
$$T := \lambda xy.x$$

As you might recall, \\(0\\) is defined as \\(\lambda sz.z\\), which is \\(F\\).
\\(T\\) is pretty simple as well--Instead of returning it's second input, it returns
the first, ignoring the second.

Now, let's define some operators.

That's not me!
--------------
As above, we'll start with negation.

$$\neg := \lambda x.xFT$$

We can see that this holds with the definition of negation.  First, \\(\neg T\\):

$$\neg T$$
$$(\lambda x.xFT)T$$
$$TFT$$
$$(\lambda xy.x)FT$$
$$(\lambda y.F)T$$
$$F$$

And now \\(\neg F\\):

$$\neg F$$
$$(\lambda x.xFT)F$$
$$FFT$$
$$(\lambda xy.y)FT$$
$$(\lambda y.y)T$$
$$T$$

This definition is pretty clever.  It uses the fact that both \\(T\\) and \\(F\\)
return one of the two inputs they recieve.  \\(T\\) returns the first input it recieves,
so \\(\neg\\) makes sure that the first input will be \\(F\\).  \\(F\\) on the other
hand returns the second input it recieves, so \\(\neg\\) makes sure it will recieve
\\(T\\) second.  Simple, sweet, but functional and powerful.

Don't forget me!
----------------
How about and?  And is defined as follows:

$$\land := \lambda xy.xyF$$

Let's test this out:

$$\land TT$$
$$(\lambda xy.xyF)TT$$
$$(\lambda y.TyF)T$$
$$TTF$$
$$(\lambda xy.x)TF$$
$$(\lambda y.T)F$$
$$T$$

How about another?

$$\land FT$$
$$(\lambda xy.xyF)FT$$
$$(\lambda y.FyF)T$$
$$FTF$$
$$(\lambda xy.y)TF$$
$$(\lambda y.y)F$$
$$F$$

I won't bore you with the other two cases, in fact, I'll let you work those out 
in the homework.

This function works in much the same way as \\(\neg\\) does, by relying upon the
work that \\(T\\) and \\(F\\) do.  If the first operand to \\(\land\\) is \\(T\\),
then it will return whatever the second operand is.  If the first operand to \\(\land\\)
is \\(F\\), then it will always return \\(F\\).  This ensures that the only time \\(\land\\)
will return \\(T\\) is if both operands equal \\(T\\).

Anyone at all?
--------------
The third operator we need is or.  Or is defined as follows:

$$\lor := \lambda xy.xTy$$

And, some examples:

$$\lor TT$$
$$(\lambda xy.xTy)TT$$
$$(\lambda y.TTy)T$$
$$TTT$$
$$(\lambda xy.x)TT$$
$$(\lambda y.T)T$$
$$T$$

And another:
$$\lor FT$$
$$(\lambda xy.xTy)FT$$
$$(\lambda y.FTy)T$$
$$FTT$$
$$(\lambda xy.y)TT$$
$$(\lambda y.y)T$$
$$T$$

Again, the other two cases will be in your homework.

This function is analogous to \\(\land\\), in that it relies upon the first input
to determine the return value.  If the first input is \\(T\\), it returns \\(T\\)
no matter what, and if the first input is \\(F\\), it returns the value of the
second input.  In this way, \\(\lor\\) will only return \\(F\\) if both inputs
are \\(F\\).

Wrapping up
-----------
This lesson was rather short, but only because the next lesson will involve mixing
boolean logic with arithmetic to create a few advanced functions, which will lead
us to be able to define a subtraction function.  But, enough about that.  Your 
homework is available as a PDF [here](https://github.com/gatesphere/blog-resources/raw/master/downloads/csmm/lesson1-3.pdf).  As always,
questions on page 1 and answers on page 2.

See you soon for lesson 1.4!

Next lesson: [here](/2012/06/29/csmm---lesson-14-advanced-logic-and-arithmetic-in-the-lambda-calculus/)