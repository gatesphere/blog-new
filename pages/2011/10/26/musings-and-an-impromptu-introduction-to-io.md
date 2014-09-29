---
title: Musings, and an impromptu introduction to Io
date: 2011-10-26

Hello all.

Sorry it's been a while. I've been involved in a lot of projects lately, all school related. I was able to finish my honors thesis on algorithmic composition recently, and it is available online for anyone who would like to read it [here](http://cs.oswego.edu/~jpeck2/). It is actually going to end up being an assignment for a class here at SUNY Oswego next year titled Cognitive Musicology, which I am acting as TA for, so I'm kind of pumped.

I've also been working on a sort of paid internship position with a professor here, working with some bleeding edge technology from IBM (sorry, can't disclose any more information about that). That's been exciting and frustrating at the same time, but I'm very happy that I'm able to work with the tech.

Recently, in my concurrency course (taught by the legendary [Doug Lea](http://en.wikipedia.org/wiki/Doug_lea)), I had an opportunity to benchmark one of the new concurrent data structures proposed for inclusion in Java 8 - ConcurrentHashMapV8. If you're interested in seeing how this stacks up to the current Java 7 implementation of ConcurrentHashMap, feel free to view the results [here](http://cs.oswego.edu/~jpeck2/375/). Note the server names... SUNY Oswego's CS department has an interesting collection of personalities, and I think they're all awesome.

As far as programming and development go, I've been working with Prolog a lot lately as a part of my Computational Modelling of Cognitive Processes course, and I find it both beautiful and clunky. But it works, and that's more than you can say about certain other languages. For things like brute-force pattern matching, Prolog can't be beat.

In my spare time, I've endeavored to learn the language Io. It's beautiful. You can read more about it in several other places, but allow me to mention the salient points here: it's purely object-oriented, meaning that everything is an object, including numbers, booleans, and even methods; it's prototype-based, meaning that there is no true distinction between instance and class (e.g. you can have two objects of type "Cat", and have one who has an additional method or slot without creating a subclass); it's a message passing language, allowing the entire core of the syntax to be summed up in 5 basic pieces (statement form, blocking with parens, assignment operators, separating disparate statements in a block with a semicolon, and comments in 3 forms); and it has a Lisp-like representation of data and instruction, meaning that data is stored in the Iovm's working memory identically to the way it is delivered in code, allowing real-time manipulation of any object.

To that end, I have built several simple data structures and even a basic non-reentrant lock in Io (source available below... didn't think I'd mention a new language without providing some code, did you?). Along the way, I've discovered some fascinating things that I never thought of before, such as the way Io handles multiple inheritance. Instead of being statically defined, ancestors are simply references to objects stored in a list, meaning that you can add and remove ancestor ojects dynamically at runtime. That floored me. I can't imagine what that could be used for, but it is incredibly powerful and speaks a lot about the way object-oriented programming is presented. Subtle things like this, mixed with the fact that it is the most elegant object-oriented model I've ever encountered, make me think that Io would be the perfect introductory language for an undergrad computer science major, or even a non-major taking an exploratory course.

That thought, combined with the high I have from finishing my thesis, gave me an idea. My professional goal is to become a college professor, as I find where I am in life to be absolutely fascinating and the best place for me. To help with that goal, I imagine that if I manage to write an introductory programming book focusing on the object-oriented paradigm, it couldn't hurt me any. So, I've started down the road towards writing a book... a lofty goal for an undergrad senior, perhaps, but one I'm excited to tackle. I've run my tentative table of contents by a few professors, and they're all for it, so here's hoping! Io would be a perfect language to use in introducing many situations in object-oriented programming, with very few exceptions which can easily be explained with a small bit of imagination. You can monitor my progress on this blog. I'll update whenever I have a decent chunk written, and post the whole thing online.

That's all I've been doing, really. I say 'all' as if that isn't a lot, but eh. I always feel like I have to be doing more than I am, but that's just who I am, I suppose.

Oh, I promised you some Io code! This code is very verbose, and probably not the 'Io' way of doing things, but it works, it's readable, and it makes sense.

Here's some simple data structures in Io:

  - [LinkedList.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/LinkedList.io) - a simple singly-linked list (from scratch, ignoring the inbult List object)
  - [Queue.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/Queue.io) - a simple FIFO queue (a wrapper around the inbuilt List)
  - [Stack.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/Stack.io) - a simple LIFO stack (again, a wrapper around List)
  - [Deque.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/Deque.io) - a simple double-ended queue (again, wrapper around List)
  - [BinarySearchTree.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/BinarySearchTree.io) - a binary search tree with several methods, including remove

Here's an implementation of an L-System in Io:

  - [LSystem.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/LSystem.io) - an L-System for operating on strings

Here's a potentially dangerous implementation of a non-reentrant style lock in io:

  - [Lock.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/Lock.io) - proven to deadlock when appropriate, but untested otherwise

Here's a small sequence of classes designed to figure out functional-style programming in Io:

  - [SequenceGenerator.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/SequenceGenerator.io) - A class to generate numbers, non-functionally
  - [SequenceGenerator2.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/SequenceGenerator2.io) - A class to generate numbers, approaching functional programming
  - [SequenceGenerator3.io](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/io/SequenceGenerator3.io) - A class to generate numbers, finally functionally (genSeq takes a parameter named next, which is a block(..))

That's it for me, I have a test or 3 to finish. Thanks for reading!

Keep tweaking~ 