---
date: 2014-01-13
tags: [dice, fudge, probabilities]
title: Strange Dice

So, in the Fate mailing list, people are discussing what the various effects of
replacing a Fudge die with a normal polyhedral die are.  This is an interesting
conversation to me, and I thought I'd do some math to get a grip on it...

# 4dF
First up is the standard 4dF distribution (which I've [talked about](/2013/04/04/fudge-is-logarithmic/) before)

    4dF | %
    ----|-------------
      -4|1.23456790123
      -3|4.93827160494
      -2|12.3456790123
      -1|19.7530864198
       0|23.4567901235
      +1|19.7530864198
      +2|12.3456790123
      +3|4.93827160494
      +4|1.23456790123

This is a baseline for my comparisons below.

# 3dF + 1d4
An interesting option is replacing 1dF by 1d4.

    3dF + 1d4 | %
    ----------|--------------
            -2|0.925925925926
            -1|3.7037037037
             0|9.25925925926
            +1|15.7407407407
            +2|20.3703703704
            +3|20.3703703704
            +4|15.7407407407
            +5|9.25925925926
            +6|3.7037037037
            +7|0.925925925926
        
Here it's shifted the average from 0 to +2.5, and increased the range--but not uniformly!  The low end has been shifted from -4 to -2, a +2 increase, while the high end has been shifted from +4 to +7, a +3 increase!

# 3dF + 1d6

A bit more extreme is replacing 1dF by 1d6.

    3dF + 1d6 | %
    ----------|--------------
            -2|0.617283950617
            -1|2.46913580247
             0|6.17283950617
            +1|10.4938271605
            +2|14.1975308642
            +3|16.049382716
            +4|16.049382716
            +5|14.1975308642
            +6|10.4938271605
            +7|6.17283950617
            +8|2.46913580247
            +9|0.617283950617

The average has shifted from 0 to +3.5, a significant boost.  Again, the low end has shifted by +2, but the high end has shifted from +4 to +9, a +5 shift!  This seems very high-powered.

# 2dF + 2d4

A rather extreme option, this removes negative results from the equation altogether... though it does make a very nice bell curve centered around 5 in the range [0,10].  This could be very handy as a normalized d10 replacement, perhaps... but so could 4dF + 4, and that wouldn't have to worry about rerolling on 10.  Anyways..

    2dF + 2d4 | %
    ----------|--------------
             0|0.694444444444
            +1|2.77777777778
            +2|6.94444444444
            +3|12.5
            +4|17.3611111111
            +5|19.4444444444
            +6|17.3611111111
            +7|12.5
            +8|6.94444444444
            +9|2.77777777778
           +10|0.694444444444

Neat to me, perhaps not so much to others... If you're interested, [here's an anydice link](http://anydice.com/program/31aa) where you can see graphs and such, and play around with it yourself.

Thanks for reading!