---
title: LaunchPad-based Glitchamin, Take 2
date: 2010-09-24
tags: [code-dump]

Hello all.

So, I made a major mistake in the code for my [last post](/?c=16). It turns out that ignoring warnings about integers being truncated due to conversions is a bad idea. Basically, my code was reading the sensor pin correctly (INCH_0 = 0), but the CUTTER and CYCLE potentiometer pins (INCH_1 and INCH_2) were outside the range of a signed integer, and therefore the ADC was returning garbage data for those two pins. I swear, sometimes it's the smallest stuff that gets you.

Aside from fixing that major problem, I also sped up the sampling process a tad by telling the ADC to use MCLK, and by only holding for 4 cycles.

These fixes brought the LP-glitchamin right up to par with it's Arduino cousin.

Updated code available:

[click here](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/launchpadglitchamin2.c).

Photos available:

1: The full setup, a bit messy.
![1](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadglitchamin/LaunchPadGlitchamin_01.png)

2: Closeup on the breadboard side.
![2](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadglitchamin/LaunchPadGlitchamin_02.png)

3: The CdS cell voltage divider in all its glory. :P I love CdS cells, they're awesome.
![3](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadglitchamin/LaunchPadGlitchamin_03.png)

Soundclip available:

[(de)Modulator2](https://github.com/gatesphere/blog-resources/raw/master/downloads/sounds/deModulator2.mp3) - .mp3, 3:03, a bit painful but it gives you an idea of the range of sounds the instrument is capable of making.

That's about it! Thanks for reading.

Keep tweaking~

EDIT: Featured on [43oh!](http://43oh.com/), again! Check it out [here](http://www.43oh.com/2010/09/make-noise-with-the-launchpad-do-a-led-zep/). 