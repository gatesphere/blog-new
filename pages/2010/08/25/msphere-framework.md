---
title: MSPhere Framework
date: 2010-08-25

I have been developing a framework of helper functions for the TI MSP430 microcontrollers, with the aim of making the Arduino function collection available for the LaunchPad environment. So far, I have accomplished quite a bit of progress, but also hit a few walls.

First up, for the progress:

  - Created a core header file which defines main() and init(), and the HIGH, LOW, INPUT, and OUTPUT constants, and declares setup() and loop().
  - Mapped the GPIO pins to single numbers, like Arduino (P1.0-P1.7 are pins 0-7, P2.0-P2.7 are 8-15... meaning the 14 pin devices only have pins 0-7,14, and 15, but still...)
  - Created a header file defining the Arduino digital I/O functions (pinMode, digitalRead, digitalWrite) and tested.
  - Created a header file defining some of the Arduino math functions (min, max, abs, constrain, and map).

Now for the walls. It appears that including all of these functions in the code leads to severe overhead. My basic test program (blinks leds at intervals, and samples the math functions into variables) clocks in at

    Code Size - Text: 1166 bytes  Data: 2 bytes
    
so I am making the code modular, so that if one doesn't need a particular set of functions, they won't be adding bloat to the codebase. I will, however, also be looking into ways to condense these functions to take up less code space.

Oh, about the name. I had originally called it MSPduino, but [NJC](http://msp430launchpad.com/) suggested that I call it msphere, as a subtle way to include my web name. I recapitalized it as MSPhere, and realized that when capitalized this way, it emphasizes MSP and "here", signifying ease of use and control, while still giving me a subtle ego boost.

Where do I see this going? Potentially a free IDE ala Arduino, but that would be a long way down the road. Due to the current code bloat, I don't see myself using it for many of my own projects--once I get bit masking down, it'll become rather useless to me--but I do want to help the user community as much as possible, and all of this is a good exercise to introduce myself more fully to the MSP430 architecture and the LaunchPad platform.

Anyways, once I get a bit more done on it, I will release it to the community under the GNU GPLv3 license, and continue to update it as time allows. I will also encourage anyone who wishes to build upon it, so long as I am informed in some manner. I want to see it grow and prosper :)

Thanks for reading, and until next time, keep hacking. 