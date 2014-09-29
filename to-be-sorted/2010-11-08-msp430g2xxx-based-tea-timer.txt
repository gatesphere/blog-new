---
title: MSP430G2xxx based Tea Timer
date: 08/11/2010

Hello all,

I am an avid tea drinker. As such, I make many cups of various kinds of tea, each with their own optimal steep times. Usually, I just keep track of the time, but I have found that I can make the best cup of tea by setting a timer to go off after a certain amount of time, depending on the style of tea that I am brewing. I find the best results come from going by the following table (based on personal preference and experimentation):

<table><p>
  <tr><p>
    <td><b>Tea Variety</b></td><p>
    <td><b>Recommended Steep Time</b></td><p>
  </tr><p>
  <tr><p>
    <td>White tea</td><p>
    <td>2 minutes</td><p>
  </tr><p>
  <tr><p>
    <td>Green tea</td><p>
    <td>3 minutes</td><p>
  </tr><p>
  <tr><p>
    <td>Black/Oolong tea</td><p>
    <td>4 minutes</td><p>
  </tr><p>
  <tr><p>
    <td>Herbal tea/infusions (most varieties)</td><p>
    <td>5 minutes</td><p>
  </tr><p>
  <tr><p>
    <td>Rooibos tea (African redbush)</td><p>
    <td>6 minutes</td><p>
  </tr><p>
  <tr><p>
    <td>Chai tea (regardless of base)</td><p>
    <td>8 minutes</td><p>
  </tr><p>
  <tr><p>
    <td>Kukicha twig tea and other varieties</td><p>
    <td>in intervals of 1 minute</td><p>
  </tr><p>
</table>

With this in mind, I decided that I should make a tea timer. This seems simple enough, and it has been on my to-do list for a while anyway, and [43oh!](http://43oh.com/) is having an [MSP430 Project of the Month Contest](http://www.43oh.com/forum/viewtopic.php?f=13&t=166), so I decided to hack it together. Turned out rather simple.

The full part count is as follows:

  - 3 toggle switches (or a 3-switch DIP, as I used)
  - 4 10k resistors
  - 1 5mm green LED
  - 1 piezo buzzer with integrated driver circuit
  - 1 tact switch/push button
  - wire
  - Any MSP430 uC with at least 1k flash and a TimerA module (though I could have hacked the WDT to work)
  
So, I assembled the circuit on my breadboard, following the schematic at the end of my post, and programmed the MSP430.

For the code, I borrowed [beretta's](http://mspsci.blogspot.com/) TimerA code example, and tweaked it to fit the needs of my timer. The timer is to read the input value of the three switches as a binary value to determine tea type, set a "goal" amount of half-second ticks based upon the user's request, and when the user presses the "start" button, go into a waiting period. While the uC is waiting, the LED will be flashed slowly at first, but increasingly faster as the timer ticks closer to the goal. Once the goal amount of ticks has been reached, the LED will be turned on, and the buzzer will sound (mine sounds reminiscent of an old-fashioned tea kettle, so it's suitable). The buzzing can be stopped by pressing the "start" button again to reset the device, and allow another time to be set. Simple enough, right?

The code is available:

[click here](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/g2xxx-teatimer.c).

Basically, as I stated above, the user selects a mode (tea type) by way of the three switches, and then presses a button to start the timer. When the tea is done steeping, the buzzer goes off, and the user can press the button again to reset it. The switch positions corresponding to the tea types are as follows:

<table><p>
  <tr><p>
    <td><b>P1.6</b></td><p>
    <td><b>P1.5</b></td><p>
    <td><b>P1.4</b></td><p>
    <td><b>Tea type (time)</b></td><p>
  </td><p>
  <tr><p>
    <td>0</td><p>
    <td>0</td><p>
    <td>0</td><p>
    <td>White Tea (2 minutes)</td><p>
  </tr><p>
  <tr><p>
    <td>0</td><p>
    <td>0</td><p>
    <td>1</td><p>
    <td>Green Tea (3 minutes)</td><p>
  </tr><p>
  <tr><p>
    <td>0</td><p>
    <td>1</td><p>
    <td>0</td><p>
    <td>Black/Oolong Tea (4 minutes)</td><p>
  </tr><p>
  <tr><p>
    <td>0</td><p>
    <td>1</td><p>
    <td>1</td><p>
    <td>Herbal Tea/Infusions (5 minutes)</td><p>
  </tr><p>
  <tr><p>
    <td>1</td><p>
    <td>0</td><p>
    <td>0</td><p>
    <td>Chai Tea (8 minutes)</td><p>
  </tr><p>
  <tr><p>
    <td>1</td><p>
    <td>0</td><p>
    <td>1</td><p>
    <td>Rooibos Tea (6 minutes)</td><p>
  </tr><p>
  <tr><p>
    <td>1</td><p>
    <td>1</td><p>
    <td>0</td><p>
    <td>Other1 (1 minute)</td><p>
  </tr><p>
  <tr><p>
    <td>1</td><p>
    <td>1</td><p>
    <td>1</td><p>
    <td>Other2 (30 seconds)</td><p>
  </tr><p>
</table>

Now, this isn't the most accurate timer, as I'm not using the crystal, but it's accurate enough to steep a good cup of tea (believe me, I've used it a lot since I hacked it together), and my stopwatch tells me it's accurate to within around 6 seconds on average.

In the future, I'd like to use a better input mechanism (I might be geeky enough to remember binary codes for tea types, but most are not, so a rotary switch or something would be perfect), maybe a cheap LCD for a status indicator, even showing how much time remains, and potentially having the last two codes (110 and 111) be user programmable for any time in second increments up to half of an unsigned long (as the ticks are half-second ticks). Maybe even shove it all into an Altoids tin for portability and the geek-chic factor. Who knows?

Anyways, here's the schematic, and a photo of it in action:

Tea-Timer in action! (notice the LaunchPad is only used as a power supply here... I don't have a battery clip yet.)

![tea-timer in action!](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/g2xxxteatimer/teatimer.png)

schematic

![schematic](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/g2xxxteatimer/schematic.png)

Thanks for reading!

Keep tweaking~

**EDIT:** Featured on 43oh! again! Check it [here](http://www.43oh.com/2010/11/msp430_tea_timer_steep/)!

**EDIT THE SECOND:** Ended up tied for 4th place. Congratulations to the winners, AMagill and simpleavr! Check out the results [here](http://43oh.com/forum/viewtopic.php?f=9&t=167&start=0). 
