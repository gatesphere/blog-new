---
date: 09/12/2013
tags: python, garbage collector, gc, algorithms, code-dump
title: Mark and Sweep in Python

Today I read a fantastic article on [mark and sweep garbage collectors](http://journal.stuffwithstuff.com/2013/12/08/babys-first-garbage-collector/), and thought I'd give replicating it in python a go.

I highly recommed reading the linked article -- it's a fascinatingly brief and simple look into one of the most misunderstood concepts in computer science.  And it's drop dead simple.

My [python version](https://gist.github.com/gatesphere/7878676) is all but useless, *unless* one plans on implementing a language in python!  Which I do, in the form of silica2.    Hmm.