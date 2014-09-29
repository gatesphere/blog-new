---
title: White Noise Generator for the MSP430
date: 2010-08-23
tags: [code-dump]

For my first project with the TI LaunchPad MSP-EXP430G2 device, I ported a simple 
white noise generator from an Arduino sketch. 

This specific code is for the G2231 
that comes preinstalled on the LP, but the code is light enough that it should 
work with any MSP430G2xxx uC. Just change the header file.

The circuit is simple. A piezo buzzer or mono output from P1.0 to GND. If you 
want to, you can remove the P1.0 jumper from J5, though it's not necessary.

The original Arduino sketch is available [here](https://code.google.com/p/greennoisehttps://github.com/gatesphere/blog-resources/raw/master/downloads/detail?name=prbsGen.pde).

And on to my code:

[click here](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/launchpadwhitenoise.c).

This code could be easily modified into a pseudo random bit generator, or into 
using PWM for producing tones on an output pin.

This code got me thinking about working on a set of Arduino-like libraries for 
the MSP430G2xxx line uC's (should also work with the F2xxx line). I have made 
some progress in this endeavor, with pinMode(), digitalRead(), and digitalWrite() 
working. I will post with more info as it progresses.

