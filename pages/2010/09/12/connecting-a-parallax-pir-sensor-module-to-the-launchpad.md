---
title: Connecting a Parallax PIR Sensor module to the LaunchPad
date: 2010-09-12
tags: [code-dump]

Hello all.
A few days ago, I went to RadioShack to purchase a few parts. Among the components in the "sensors" drawer, I stumbled upon a PIR sensor from Parallax, datasheet available [here](http://www.parallax.com/sites/default/files/downloads/910-28027-PIR-Sensor-REV-A-Documentation-v1.4.pdf).

I thought, "hey, what the heck? I've wanted to toy around with one of these for a while, and it's only $10. Why not?". So I bought it.

I also thought, "I should be able to use this with both the LaunchPad and the Arduino due to the input voltage range." I was only partially correct on that last point.

So, I purchased the sensor, took it home, and started playing with it. At first, I didn't use it with anything but an LED. It was fun, lit the LED, and did it's job in detecting motion. Nice, simple, compact, and neat. Then I wrote a simple Arduino sketch to interface with the data output to light the LED on pin D13. It worked like a charm.

Then, I tried to do the same with the LaunchPad. It didn't work.

Well, it did, but not in a way that the datasheet made clear at all. The datasheet has absolutely no electrical characteristics listed at all. It simply states that the output is one-bit HIGH or LOW.

This is kind of hit or miss. The sensor outputs about 2/3 of the input voltage and calls it "HIGH". LOW, however, is tied to ground perfectly. I didn't discover this until I compared output to the full voltage reading on my oscilloscope (which is in reality a re-purposed Arduino), and it turns out that this is the missing link in the chain.

The LaunchPad operates at 3.3V, whereas the Arduino (or, at least, the Arduino Duemilanove) operates at 5V. When operating from a 5V source, the output pin pulses at ~3V. But when operating from a 3.3V source, such as the LaunchPad, the pulse is a mere ~1.7V. The MSP430 line, as juani_c from the [43oh! Forums](http://43oh.com/forum/) points out, requires 0.7*Vcc, or ~2.31V at Vcc=3.3V, to register as HIGH. (It seems the ATMEL uC's are much more sensitive) So clearly, powering from the LaunchPad's standard 3.3V is not going to be a valid option.

So, what I did, was tap in the the tie points on the LaunchPad, labeled TP1 and TP3. They are located near the USB port, and left unpopulated on the boards as shipped. According to the schematics found in the LaunchPad User's Guide, TP1 is connected to VBUS (USB's Voltage, which happens to be 5V), and TP3 is connected to the USB's GND.

So, I soldered a few one pin headers into these tie points (not an easy task, for one with unsteady hands... helping hands are a must) and used those to power the PIR. And guess what, it works!

So, after I made sure the sensor was working, I wrote up a simple little code example to share with you all.

Code available:

[click here](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/launchpadpirsensor.c).

This is just a small example. The code sets up P1.5 as the input of the PIR sensor, and takes an interrupt on that pin to toggle LED1 when motion is detected by the PIR. LED2 is always on to indicate power. After everything is set up, the uC goes into LPM4 to conserve power, waking up on an interrupt on P1.5. It's rather simple, actually, but I think it could come in handy for some people to get a jump start on a motion detecting application of some sort.

Anyways, I hope you have enjoyed this, and that you find this helpful. As always, feel free to ask questions and leave comments. I will answer them as soon as I get them.

Thanks for reading!

Keep tweaking

EDIT: Now, photos!

1: Close up on TP1 and TP3 near the USB port. I also added headers to the other TP pins, just because I might need them in the future should I want to toy around with the emulator.
![1](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadpir/LaunchPadPIR_01.png)

2: Solder points for TP1 and TP3. Ignore the bad soldering.
![2](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadpir/LaunchPadPIR_02.png)

3: The full setup.
![3](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadpir/LaunchPadPIR_03.png)

4: Close up on the 5V and GND connections. Alligator clips are sloppy, but it's all I had on hand.
![4](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadpir/LaunchPadPIR_04.png)

5: In action, no movement (no red LED1 lit).
![5](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadpir/LaunchPadPIR_05.png)

6: In action, movement detected (red LED1 is lit).
![6](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/launchpadpir/LaunchPadPIR_06.png)

EDIT 2: Featured on [43oh](http://www.43oh.com/) for the third time. Link [here](http://www.43oh.com/2010/09/interface-the-launchpad-to-a-parallax-pir-sensor/). Thanks bluehash! 