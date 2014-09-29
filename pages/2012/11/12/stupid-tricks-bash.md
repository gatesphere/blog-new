--- 
tags: bash, stupid tricks, hacks, code-dump
date: 12/11/2012
title: "Stupid Tricks: bash"

This article showcases a few stupid bash tricks that I've gathered in my 
recent employment as a unix sysadmin.  Some of these aren't all that 
useful, but they are neat.

First up, a fun toy:

<script src="https://gist.github.com/4061547.js?file=slash-r.sh"></script>

Running this, you'll see a counter that rises from 1 to 100, overwriting 
itself as it goes.  You could use this with some trickery to give a 
visual indicator of how far done a process is, for example.

Next up, returning a value from a function:

<script src="https://gist.github.com/4061547.js?file=return-value.sh"></script>

You can scale this to return as many values as you want from a function.  
I use this one all the time.


Concatenate strings:

<script src="https://gist.github.com/4061547.js?file=concat.sh"></script>

It really is as simple as mushing them together like that.


That's all for now.  Thanks, for reading!
