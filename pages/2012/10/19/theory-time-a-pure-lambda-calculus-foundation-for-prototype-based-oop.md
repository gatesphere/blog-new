---
title: ! 'Theory Time: A pure lambda-calculus foundation for prototype-based OOP'
date: 19/10/2012
tags: theory, lambda calculus, lambda, prototype, oop, map, list, hash

Hello all,

I'm excited to write this post today, because it's something that just kind of 
flowed to me as I was thinking about programming language paradigms.  I was wondering
about just how deeply related functional programming is to other methodologies,
and figured that if the \\(\lambda\\)-calculus is Turing complete, there must be
a way to model object-orientation on some level with it.  What follows is my attempt
at forming a mathemtatical bridge between functional and object oriented programming
paradigms, by showing that OOP is really just a subset of the functionalities provided
by the \\(\lambda\\)-calculus.

A bit of background
-------------------
Alright, I should probably start by defining a few things, such as what object model
I will be using, along with some notational conventions.

First, the object model.  I was looking for the absolute minimal model of what
an "object" is that I could use as a foundation for building in the \\(\lambda\\)-calculus.
It seems that a stripped down version of Io's object model fit the bill here.  In
Io, an object is just a collection of slots, each of which is a named reference to another
object.  There is no differentiation between classes and instances--everything is
a usable object.  And every new object extends and modifies a previously existing
object ("cloning" a "proto" in Io speak).  To interact with an object, you reference 
its slots by sending it a message, which acts as a key to an internal lookup table,
returning the value of the slot which is named the same as the message you sent.
So we have this graph-based relationship between objects tied together by names which
act as messages.  

This sounds to me like an easy thing to model abstractly.  We'll need some sort
of map to tie names to values, to act as an object's collection of slots.  We'll
also need a construct to bind that map to an ancestor object.  This construct will
be our object model.  To interact with it, we'll need some sort of a lookup method
to access the values from the map, and some sort of forwarding mechanism to look up
slots that were not found in the object in question's map, but may be in its
ancestor's slots.  And that, really, is all we need to model this.

But before I dive into details, let me explain my notation for the following
\\(\lambda\\)-terms a bit, as it does not follow the previous examples I've used
in this blog, simply for the sake of using more descriptive bound symbols.

Some conventions:
  
  - Lowercase letters are variables, and are exactly one letter each.
  - Words in UPPERCASE are bound symbols, which are simply aliases for longer \\(\lambda\\)-terms.
  - Words in camelCase are the "interface" that I want to expose as the end result
    of this work.  They are otherwise functionally identical to UPPERCASE aliases.
  - Symbols will be separated with a space for readability.
  
Also, for sake of easy editing, all terms will be typeset in a `fixed-width` font.

Alright, enough babbling, time to begin.

\\(\lambda\\) foundations: a list
---------------------------------
This article assumes you know how to use church numerals, and the definitions for
a few common functions, such as SUCC, TRUE, FALSE, etc.  I will provide definitions
when I remember to, but if I'm missing something, I apologize.

Anyways, a quick and dirty explanation of a list in the \\(\lambda\\)-calculus
follows closely the implementation of a list in LISP, in that a list is either 
the empty list (NIL), or a pair consisting of an element and a smaller list.

We can use the following definitions for creating and manipulating lists:

    TRUE  := λa b.a
    FALSE := λa b.b
    CONS  := λa b f.f a b
    NIL   := λf.TRUE
    NIL?  := λl.l (\a b.FALSE)
    HEAD  := λl.l TRUE
    TAIL  := λl.l FALSE
    
These functions are the building blocks for lists in the \\(\lambda\\)-calculus.

So, an example list could be:

    L := CONS a (CONS b (CONS c NIL))
    
Some operations on this list could be:

    HEAD L                                   -> a
    TAIL L                                   -> CONS b (CONS c NIL)
    HEAD (TAIL L)                            -> b
    NIL? (TAIL (TAIL (TAIL L)))              -> TRUE
    NIL? L                                   -> FALSE
    CONS (HEAD L) (CONS (HEAD (TAIL L)) NIL) -> CONS a (CONS b NIL)
    
Simple enough, right?

Moving on to maps
-----------------
Defining a mapping construct in the \\(\lambda\\)-calculus is simple once you have
a definition for lists down.  A map is simply a list of pairs, each pair being
a pairing between a key and a value.

One issue with maps is that unless your keys are guaranteed to be unique, you'll
have some collisions, resulting in either maps with more values than keys, or missing
elements.  For simplicity, we'll limit our maps to single-valued maps, wherein each
key maps to exactly one value.

An example map could be:

    M := CONS (CONS 1 x) (CONS (CONS 5 y) NIL)
    
So, here we have a map with 2 keys, here being Church numerals (you will see why
in a second), mapping to different values.

In order to make use of this map, we need a function to lookup the value related
to a given key.  This is why I chose Church numerals for the keys above--there
is an easily defined equality predicate for testing if two Church numerals are
the same.  Though, any class of \\(\lambda\\)-terms that you can define an equality
predicate for will work as the keys of a map.

The lookup function isn't to difficult to define:

    LOOKUP := λr m k.
      IF (= (HEAD (HEAD m)) k)
        (TAIL (HEAD m))
        (IF (NIL? (TAIL m))
          NIL
          (r (TAIL m) k))

That's a bit dense, but in pseudo-code, it reads a bit like this:

    lookup(map, key):
      if (the head of the first element of map == key)
        then [return the tail of the first element of map]
        else [
          if (the tail of map is the empty list)
            then [return the empty list]
            else [return lookup(tail(map), key)]
        ]
        
Actually using this involves the Y-combinator, a method of recursion in the \\(\lambda\\)-calculus:

    Y := λa.(λb.a (b b)) (λb.a (b b))
    
To perform a lookup of key k on map m, do this:

    (Y LOOKUP) m k
    
Easy as pie.

The object model
----------------
Our object construction is almost complete!  Now we just need to tie the map of
slots to an ancestor object in some construct, and define a getSlot function to
retrieve the value of a slot in an object or its ancestors.

Guess what it's going to be.

That's right, another pair.  We pair an ancestor to a map, and we have an object.
Pretty easy.

Here's an example object:

    O := CONS a (CONS (CONS 1 x) (CONS (CONS 5 y) NIL)

For the getSlot function, we need to be able to find the value of some slot s
in either the object's slot map, or failing that (a value of NIL returned), in 
the slots of its ancestor object, recursing further if it isn't found there either.

A definition for this is pretty simple as well:

    GETSLOT := λr s o.
      IF (NIL? ((Y LOOKUP) (TAIL o) s))
        (IF (NIL? (HEAD o))
          NIL
          (r (HEAD o) s))
        ((Y LOOKUP) (TAIL o) s)
        
Again, pseudo-code for those who would like it:

    getslot(slot, object):
      if (the returned value for lookup(tail(object), slot) is nil)
        then [
          if (the head of object is nil)
            then [return nil]
            else [return getslot(head(object), slot)]
        ]
        else [return lookup(tail(object),slot)]

Again, this makes use of the Y combinator, but because getSlot will be a part of
our clean interface to this model, I want to hide that detail for aesthetic
purposes.

    getSlot := Y GETSLOT
    
And our model is complete!

What this model does
--------------------
This model allows us to perform simple method chaining to adopt a very linear 
programming style.  Take the following line, for instance:

    a (getSlot 3) (getSlot 4) (getSlot 2)

This would retrieve the slot 3 from object a, then retrieve that returned object's
4 slot, then finally retrieve that returned object's 2 slot.  This closely mirrors
the idea of message passing in prototype-based object-oriented languages.  Because
everything in the pure \\(\lambda\\)-calculus is a function, there is no such
thing as an exception in the above statement.  However, the end result might be
absolutely meaningless if one of those slots didn't exist along the way.

What this model doesn't do
--------------------------
Multiple inheritence, for a reason.  Which order would the ancestors be visited?
Besides, you can emulate multiple inheritance by creating multiple objects that
chain together dependencies.

Self referencing, as there's no introspection in the \\(\lambda\\)-calculus.  Though
it can be achieved in much the same fashion as with the Y combinator:

    a (getSlot 3) a
    
That would pass a as a value to a's 3 slot.  Kind of python-like, but performed
manually.

Mutation, because I wanted to model this as a purely functional system, and further
wanted to stay strictly pure with my \\(\lambda\\)-terms.  Mutation is simply not
a concept that exists within the scope of this article.

Final thoughts
--------------
This was an interesting process of exploring and writing.  I'm not typically a theoretical
mathemetician, but something about the \\(\lambda\\)-calculus just gets me (as I'm
sure you've noticed).

Thanks for reading, and any suggestions/comments/criticisms are welcome in the comments
area below.