---
title: Texas Instruments TLV5618A library for MSP430 LaunchPad
date: 05/10/2010
tags: code-dump

Hello all,

I have written up another library for the MSP430G2xxx value line chips, this time targeting the TLV5618A 12-bit dual-channel DAC from TI. (Datasheet available [here](http://www.ti.com/litv/pdf/slas230h).)

It has been written in much the same way as [my previous library for the TLV5620](/?c=9). I also plan to port it to the MSPhere framework as I did the [other one](/?c=15).

Anyways, there are a few important things to point out about the TLV5618A. Firstly, the '5618A has a "feature" of applying a 2X gain to the reference voltage, meaning that the input to the REF pin (pin 6 on the DIP) has to be half of the maximum range of whatever you are interfacing the DAC with. To get around this "feature", I used a simple voltage divider formed by two resistors of equal value.

[Aside: For those of you unfamiliar with a voltage divider, I'd suggest reading the [Wikipedia article](http://en.wikipedia.org/wiki/Voltage_divider) on them. But to sum up, by using two resistors between ground and your voltage source, tapping between the two resistors supplies a voltage based upon the values of the two resistors, and consistent with the following equation: Vo = (R2 / (R1 + R2)) * Vi, where Vo is the output voltage, Vi is the input voltage, and R1 and R2 are the values of the resistors. It can be shown that when R1 and R2 are the same (lets call it Rx), then the equation simplifies further, to Vo = (Rx / (Rx + Rx)) * Vi = (Rx / (2 * Rx)) * Vi = 0.5 * Vi.

Another thing to mention about the TLV5618A is that it has a power-down feature, in order to help preserve power and reduce consumption. However, one (undocumented, it seems) side effect of this is that putting it into power-down mode resets the value of BUFFER and DACB to CODE_4095 (full-on), causing undesirable effects if you are using both DAC channels the chip offers.

Also, to update the two channels simultaneously, you simply write the value for DACB to BUFFER (DACBUFFER in my library), and then write to DACA. Updating DACA also updates DACB with the value in BUFFER. To use the two separately, simply write to DACB rather than DACA. Writing to DACB also writes to DACBUFFER, so that when DACA is written, DACB is effectively unchanged.

And, last, but in my case also least, the '5618A has two speeds it can operate in, appropriately called SLOW and FAST. This refers to the setting time of each individual channel. But with the speeds that the MSP430G2xxx chips operate at, this is a non-factor. So, use FAST or SLOW to write. I wrote both into the code simply because I like to expose every aspect of a chip via a library, even if it is useless to the application I have in mind. This also makes porting to other architectures easier.

I have written an example application using the library.

Code available:

[click here](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/launchpad5618awaveform.c).

This is a modified version of my quad waveform generator for the TLV5620. This one simply produces two waves, updated simultaneously. DACA is a rising sawtooth, and DACB is a falling sawtooth. The circuit is simple, and outlined in the schematic available at the bottom of the post.

So, without further stalling and rambling, here are associated files.

Images:

O'scope capture of output
![o'scope capture](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpad5618a/o-scope.png)

schematic

![schematic](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpad5618a/schematic.png)

Download MSP430_TLV5618Alib:

[version 20101005](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/MSP430_TLV5618Alib_20101005.zip)

Thanks for reading!

Keep tweaking~ 
