---
title: "Adventures in Roguelike Development, Chapter 3: Bumps in the Road"
date: 04/06/2011
tags: code-dump

Hello all,

Welcome to the (short) third installment of my roguelike development chronicle. You can read the previous posts below:

  - [Chapter 1: The Quest Begins!](/?c=36)
  - [Chapter 2: Gathering Supplies](/?c=37)

So, to start things off, let me first apologize that this post is so short. Unfortunately, due to some family medical issues, I have been unable to work on much of anything this week, and most of what I am about to report on is simply housekeeping and maintainance stuff. Also, I preemptively apologize for any late entries in the future.

So, what did I manage to get done this week? For starters, I started keeping a changelog, which will help keep me on track and organized for when I write these posts. It's available in the snapshot below, see `changelog.txt`.

I then dived into some maintainance issues. First on the list was splitting rlutil into two files, a header and an implementation file, in order to prevent multiple definitions of functions without inlining everything. As I was doing this, I also decided to include a temporary fix for rlutil's `getkey()` for *nix machines; the same empty `while(1){}` that I previously had defined in my roguelike's code. This is just a temporary fix, until I can wrap my head around the internals of *nix systems calls. I also mucked around a bit with the makefile, adding a timestamp to the code snapshots, the `-O3` flag to the compile flags, and restructuring the source tree to organize my code.

In the way of actual code, I just fixed the room/corridor drawing and contains logic to make more sense.

Next up, should I ever find a break, is FoV :)

Thanks for reading! I have no screenshots this week, but here's the source snapshot, as usual.

Code: [snapshot 20110604](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/rlprototype-20110604.tgz)

Keep tweaking~ 
