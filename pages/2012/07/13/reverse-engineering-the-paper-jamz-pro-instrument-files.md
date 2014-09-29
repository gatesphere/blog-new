---
title: Reverse Engineering the Paper Jamz Pro instrument files
date: 2012-07-13
tags: [reversing, paperjamz, bits, bytes, markov, audio]

So, I'm working on a musical project, and I've decided to use only toy instruments.
Specifically, the Paper Jamz Pro series of instruments from Wowwee.  These are fun
toys to play with, but what had me interested in them is the fact that they're 
customizable, to a certain extent.

There are 3 instruments in the Pro series line, of which I'm interested in two 
(guitar and drums).  I was able to pick up mine relatively cheap as they're on 
clearance almost everywhere around where I live.  Bonus.  But, price aside, the
reason I'm interested in these two instruments specifically is that using the 
free app from the [Paper Jamz Pro website](http://paperjamzpro.com/), you can
change the voice of the instrument to one of a number of voices included with
the app.

I've decided that I'll try to reverse engineer these instrument voice files, to
see if I can manage to get my own samples onto these instruments.

Here's what I've gleaned so far.  The instrument files for both guitar and drums
seem to be structured similarly.  There is a large header, which starts with a
magic number (0xPJIG or 0xPJID) and several other bits of information that I
cannot decode yet.  Following that seems to be a series of audio frames.  Using
audacity's "import raw audio" feature, I've tinkered around and discovered that
importing these instrument files as ADPCM VOX files at 22,050Hz, you get a decent
sounding approximation of the sounds the instrument produces.  However, the frames
are filled with clicks, leading me to believe that there are interstitial headers
throughout the file, perhaps between every frame, which hold metadata for the 
instrument to use.

Either way, it's been fun so far.  Let's see what else I can figure out.