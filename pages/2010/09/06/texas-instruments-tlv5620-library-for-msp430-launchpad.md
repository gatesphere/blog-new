---
title: Texas Instruments TLV5620 library for MSP430 LaunchPad
date: 2010-09-06
tags: [code-dump]

Hey all.
I've written a library for the TLV5620 8-bit quad-channel DAC from TI. This is a wonderful little chip which works on the SPI interface and supports simultaneous update of all four channels of the DAC. Datasheet available from TI [here](http://www.ti.com/litv/pdf/slas110b).

The library is available for download from this very blog. The link is at the end of this post.

I have also coded up an example application showing all the features of the chip. Code available:

[click here](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/launchpad5620waveform.c).

This example application is a simple quad-waveform generator operating on all four DACs the 5620 has, and updating them all simultaneously. The circuit is as follows (pin numbers refer to pins on the TLV5620):

pin 1 - GND (gnd)

pin 2 - VCC (vref for DACA)

pin 3 - VCC (vref for DACB)

pin 4 - VCC (vref for DACC)

pin 5 - VCC (vref for DACD)

pin 6 - P1.0 (data)

pin 7 - P1.2 (clock)

pin 8 - P1.3 (load, like data latch)

pin 9 - DACD output

pin 10 - DACC output

pin 11 - DACB output

pin 12 - DACA output

pin 13 - P1.1 (ldac, controls simultaneous update)

pin 14 - VCC (VDD)

The use of the library is relatively self-explanatory, by looking at the example code. One thing to note is that the function tlv5620_simultaneousUpdate() only should be called if you are using the simultaneous update feature of the TLV5620. Otherwise, I would suggest calling tlv5620_updateMode(ASYNCHRONOUS, LDACPIN, LDACPORT) at the beginning of your program to initialize the LDAC pin to LOW.

To compile this example, make sure the source file and the two source files in the library are in the same directory, and within whichever environment you use (untested outside of CCS4), that the symbol pertaining to whichever MSP430 you are using is defined. For example, make sure that __MSP430G2231__ is defined if you're using the G2231.

If anyone has any questions, just let me know either here or at the [43oh forums](http://www.43oh.com/forum/viewtopic.php?f=10&t=66).

Download MSP430_TLV5620lib:

[version 20100906](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/MSP430_TLV5620lib_20100906.zip)

Keep tweaking

EDIT: featured on 43oh, again! Link [here](http://www.43oh.com/2010/09/msp430-interface-to-a-ti-tlv5620-dac/)! 