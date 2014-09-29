---
date: 28/10/2013
tags: python, programming languages, stupid tricks, code-dump
title: Passing a comparison operator in Python

So, earlier today I was refactoring some code to be more general purpose, and said code
involved a comparison operator.  I was already using the same code in two places, but copy-pasted
with different comparison operators switched in.  Eww.

I didn't quite know how to pull this off, given that I'm not that well versed on Python's introspection
faculties... but I gave it a whack.  My first thought was the nïave approach, of passing in a string
to specify mode...

<script src="https://gist.github.com/gatesphere/7201086.js?file=approach_1.py"></script>

Yuck.

Then I realized that functions are pretty much first class in python.  Additionally, lambdas are short
and sweet.  A few minutes later, I was rolling with this instead:

<script src="https://gist.github.com/gatesphere/7201086.js?file=approach_2.py"></script>

So much nicer.  Instead of passing a mode string, now you just pass one of those comparators, ala:

    myfun(4,7,comparator=cmp_lt)

**Update**: A friend pointed out a few other ways of accomplishing this -- one way more pythonic, and one incredibly unsafe.

The pythonic solution relies on the 'operator' module:

<script src="https://gist.github.com/gatesphere/7201086.js?file=approach_3.py"></script>

That's much like approach 3, but the call is now:

    myfun(4,7,comparator=operator.lt)

The unsafe way is to evaluate it as a string!  Here we go:

<script src="https://gist.github.com/gatesphere/7201086.js?file=approach_4.py"></script>

Man, I love Python.  We're not starved for options!


    
Hope this helps someone else!