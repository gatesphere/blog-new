---
title: MSPhere update
date: 2010-09-08

Hello all,
I've been busy at work at MSPhere, seeing as I have a relatively short class week due to Labor Day and Rosh Hashanah. So in between my light homework load, I've been coding a bit. Here's what I have so far, and what I have left to do before I feel it's fit for an initial release.

"Completed": (I use the term lightly, it's subject to change at a moment's notice)

  - MSPhere core lib
  - Digital I/O module
  - shiftOut() function for dealing with SPI, in the Advanced I/O module.
  - Math module
  - resistorMode() function for controlling internal pullup/down resistors

To be implemented before initial release:

  - functions for setting various LPMs
  - interrupt helper functions
  - timer/clock functions
  - delay() function, ala Arduino
  - pulseIn()... possibly

What will NOT be included in the initial release: ADC functions, for sure. Nor will flash memory functions. Those will come at a later date.

I will also offer an MSPhere-ized version of my TLV5620lib mentioned in the previous post as an additional library in a separate download. I feel that this chip-specific library doesn't belong in the main library, but that it could be useful to some people working with the MSPhere framework, so I will have a collection of add-on libraries to go along with the main framework, with my TLV5620lib being the first.

That's the current status. So, yeah. It's coming soon-ish, but not too soon.

Thanks for reading!

Keep tweaking 