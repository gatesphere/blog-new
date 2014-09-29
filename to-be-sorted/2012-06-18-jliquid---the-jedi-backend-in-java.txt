---
title: jliquid - the jedi backend, in Java
date: 18/06/2012
tags: jedi, java, jliquid, github, finite state machines

Hello all,

Thought I'd take a second to mention that I've begun porting my [jedi 
programming language](http://jedi.suspended-chord.info/) backend to Java.  I'm
not entirely sure why, but it's been fun, and it's shown me how flawed my object-
oriented thinking is sometimes, if I dive into projects without a defined spec
ahead of time.  While the current version of jliquid works, it is lacking several
important features, for which I *must* redesign to accomodate.  Chief among them
is the inability to output *anything* to the output ports from within the machine
(JLiquidTask).  Ah well.  We shall see where it goes from here.

If you're interested, you can check out the [jliquid Github repo](https://github.com/gatesphere/jliquid).
