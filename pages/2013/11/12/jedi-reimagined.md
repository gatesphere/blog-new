---
date: 12/11/2013
tags: programming language design, theory, jedi
title: Jedi Reimagined

The past few weeks I've been thinking more about the dataflow paradigm, and how I would approach it after the lessons learned from jedi.  In my mind, I'd like to have the following features in any dataflow language I'd design or use:

  - Object orientation, on some level
  - Lambdas, for syntactic sugar
  - Hackable internal framework (i.e. metaprogrammability)

To elaborate a bit more, let's focus on each of these one at a time.

# Object orientation

An object at it's absolute core is simply a map, or a dictionary, or an associative array, whatever your language of choice calls them.  They are containers that accept names and return other objects based on the names passed to them.  Io calls the names 'slots', and I find that to be very fitting.

I'd most likely go with a prototype paradigm, akin to Io, rather than a class-based design, simply because I love the flexibility offered by prototypes.  As a result, the whole language would extend from a single Metaobject, and would use duck typing.  Perhaps a performance penalty, but I'm more interested in expressability and flexibility than type-safety.

Additionally, I'd like some sort of data-munging/mixin capability akin to [http://perl11.org/potion/](Potion)'s concept of the trait.  This would reduce the load on the duck-typing system.  As syntactic sugar, there would be a 'origtype' keyword that would de-munge a type after the last trait mixin, if needed.  This would rarely be used, though, I think.

There would be special named slots for each object.  These would be 'magic slots', akin to Python's 'magic methods'.  I'm sure more would pop up in implementation, but the only one I can think of now is:

   - current_node (the 'node' type object that is currently processing this object)

There would, aside from the Metaobject, be at least three other fundamental object types (all descending from Metaobject, of course):

  - lambda (a wrapper object that provides syntactic sugar around simple methods)
  - arc (an object with 'many ends', [de]muxer, splitting and copying objects to send from it's in_nodes to it's out_nodes)
  - node (an object with 'many holes', it connects lambdas with arcs, and lambdas act on objects.  It has in_arcs and out_arcs)

# Lambdas

Covered by the 'lambda' object above.

Imagine you had an accumulator object that could increment some internal count.  Now, imagine you wanted a node to perform this twice.  The body of the node would be contained in a lambda.  The following pseudo-code (inspired by Potion) would do the trick:

<pre>
# Create the Accumulator object
Accumulator = Metaobject ():
  .value = 0
  accumulate:: lambda (self) (self .value += 1)

# Create an instance of the accumulator
a = Accumulator ()

# create a node that operates on its input 
# by calling accumulate slot twice
n = Node (lambda (x) (2 times (x accumulate ())))

# some other code here to set up and run the node
</pre>

# Metaprogramming

Being a prototype language, all bits and bob about the node, arc, lambda, and Metaobject definitions are hackable just by extending them!

Just some thoughts... I doubt it will ever happen, but this is where I'd like to see a workable Jedi system go.