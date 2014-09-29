---
title: MSPhere initial release!
date: 2010-09-15
tags: [code-dump]

I am pleased to announce the initial release of the MSPhere framework for the TI LaunchPad platform! I have decided that it was time to let this code breathe, and find new life.

This release comes with a few caveats, however. It is an initial release, meaning that much of the planned functionality is missing. It also does not support MSPGCC4 at the moment, though it is easily portable. And, lastly, it does not have many of the features I outlined in my last MSPhere post. I decided that due to classes, and lack of free time, it would be more of a motivation to release this now and give me incentive to continue working on it, rather than let it stagnate on my hard drive. That being said, it does contain a lot of functionality, with 4 modules outside of the main module. It does not contain ADC code, TIMERA code, LPM code, or WDT+ code outside of a simple wdtHold() function. Also, the documentation is incomplete, but will be worked on as I find time. But I felt that if I didn't release it now, it would be buried under my studies, and neglected until the winter, or even later. So, here it is.

It does contain two demo programs, showcasing the features of the library: a simple '595 based binary counter, and a push-button led toggling program to show off interrupt handling and the internal pullup/pulldown resistor code.

Those of you who would wish to try it are invited to download it at the MSPhere site, [here](http://msphere.suspended-chord.info/).

Thanks for reading!

Keep tweaking~ 