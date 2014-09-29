---
title: LaunchPad-based Glitchamin
date: 2010-09-23
tags: [code-dump]

Hey all,

I did a quick port of my [Arduino-based glitchamin](http://suspended-chord.info/portfolio/micros/glitchamin-arduino-2010/) to the LaunchPad. I did this mostly as a way to test out a way to write ADC10 code, which I will need for the MSPhere library in the near future.

Anyways, it works, it sounds a bit funky, and it's nowhere near as high fidelity as its Arduino cousin. But it is a start for both ADC code and audio genesis with the LP.

The circuit is pretty simple. It consists of the following:

P1.0 -> voltage divider formed by a CDS cell and a 10k resistor
P1.1 -> a 1k linear pot
P1.2 -> a 10k linear pot
P1.5 -> 8ohm speaker
The values on the three analog parts don't really matter, and if you wanted to, you could replace them with any analog components. And the speaker can be replaced by a piezo buzzer or a mono jack output. The circuit is rather flexible.

The code is available:

[here](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/launchpadglitchamin.c).

Keep tweaking~ 