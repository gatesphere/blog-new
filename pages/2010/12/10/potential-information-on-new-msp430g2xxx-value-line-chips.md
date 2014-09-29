---
title: Potential information on new MSP430G2xxx Value Line chips?
date: 2010-12-10

Hello everybody.

I might have stumbled upon some new information for chips coming to the MSOP430G2xxx Value Line series soon. In a recent update of TI's CCSv4, a bunch of new headers were (stealthily) installed. I just happened upon these headers, and decided to take a look. What I found was four new families of chips, each available in 4 flash sizes (or so I assume) for a total of 16 new chips. These new chips are also (not very stealthily) available in the CCS New Project Wizard after the update. But, from scouring the headers, here is what I've found. Please note, all flash sizes are just speculations, based upon educated observation of TI's numbering schema. These could probably be confirmed by looking in the linker files, but I'm not educated in their makeup, so I did not try to confirm any of this. Also, x in a part number anywhere below can be replaced with your choice of 1, 2, 3, or 4.

Family 1: The MSP430G2x02 Family

  - Flash2 (1 / 2 / 4 / 8k?)
  - TimerA_3
  - USI
  - Calibration data for 16/12/8/1MHz

Family 2: The MSP430G2x12 Family

  - Comparator A+
  - Flash2 (1 / 2 / 4 / 8k?)
  - TimerA_3
  - USI
  - Calibration data for 16/12/8/1MHz

Family 3: The MSP430G2x32 Family

  - ADC10
  - Flash2 (1 / 2 / 4 / 8k?)
  - TimerA_3
  - USI
  - Calibration data for 16/12/8/1MHz

Family 4: The MSP430G2x52 Family

  - ADC10
  - Comparator A+
  - Flash2 (1 / 2 / 4 / 8k?)
  - TimerA_3
  - USI
  - Calibration data for 16/12/8/1MHz

Three important things to note. First, if my speculations for flash size hold true, then this batch would mark the first value line devices that reach more than 2k. Second, all of these chips have calibration data for speeds above 1MHz, making these the first value line devices that don't have to be [hacked](http://naturetm.com/?p=91) to add the "missing" calibration data. Third, the G2x52 family chips are the first in the value line to contain both the ADC10 and Comparator A+ modules. One other small note is the switch from TimerA_2 used in all the previous value line chips to the TimerA_3 module. I'm not sure what change, if any, this will have on TimerA code (all the usual registers are defined), but it's worth noting, if only on a technical level.

Searching for any of these part numbers on TI's website currently gives a valid product page, but without any information at all, including data sheets and samples. They are also unlisted on the MSP430G2xxx Value Line page.

I, for one, am really looking forward to the G2432 and G2452 chips. Hopefully these will give me a bit more room to breathe, code-wise.

Keep tweaking~

**EDIT:** I have done some snooping around in the lnk_msp430g2xx2.cmd files, and confirmed the flash sizes for these new chips. Also, NatureTM pointed out that they all have 256 bytes of RAM, always a good thing. So, according to the linker files, the G2102, G2112, G2132, and G2152 all have 1k, the G2202, G2212, G2232, and G2252 all have 2k, the G2302, G2312, G2332, and G2352 all have 4k, and the G2402, G2412, G2432, and G2452 all have 8k of flash space. Thanks to OCY for pointing me in the right direction, and to NatureTM for noticing the RAM size.

**EDIT 2:** Featured on 43oh!, [here](http://www.43oh.com/2010/12/new-ti-msp430g2xxx-parts-on-their-way/). 