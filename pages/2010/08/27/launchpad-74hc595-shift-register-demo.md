---
title: LaunchPad 74HC595 Shift Register Demo
date: 2010-08-27
tags: [code-dump]

Hey all. I wrote up a quick bit of code today to use a '595 shift register. It's a binary counter that counts from 0 to 255 and then restarts.
Code:

[click here](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/launchpad595.c).

Basically, you set up the circuit as follows: (all pin numbers are in regards to the '595 chip, information available at [http://www.msarnoff.org/chipdb/74595](http://www.msarnoff.org/chipdb/74595))

Q0-Q7 (pins 1-7, 15): LED to ground, with suitable resistor in series.

GND (pin 8): ground, obviously.

Vcc (pin 16): Vcc, obviously :P

MR (pin 10): Vcc.

OE (pin 13): ground.

DS (pin 14): P1.0 on the LaunchPad

RCK (pin 12): P1.1 on the LaunchPad

SCK (pin 11): P1.2 on the LaunchPad

What the code does is count from 0 to 255, with each count setting the latch pin (RCK, P1.1) low to prevent flashing of the LEDs while shifting bits, and then calls shiftOut(), which breaks the value down into bits, writing them out to DS one at a time, while pulsing SCK low-high in the process to allow the bits to be shifted out. After that, the RCK is brought high again, allowing the LEDs to light in unison. Then there is a delay of 25000 clock cycles to allow the count to be followed by the human eye.

This was written in an attempt to prototype the shiftOut() function of the MSPhere framework, which is coming along swimmingly, and was recently featured on [43oh](http://43oh.com/)! Check the feature [here](http://www.43oh.com/2010/08/msp430-msphere-framework/trackback/).

Thanks for reading, and keep tweaking. 
