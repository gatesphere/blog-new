--- 
date: 21/09/2012
tags: raspberry pi, rpi, raspi, sysadmin, embedded, raspbian, io
title: Adventures with a Raspberry Pi

Hello all,

When I came home Wednesday afternoon, I was surprised to see my Raspberry
Pi waiting for me.  Well, that's a lie, as I had been tracking it all
day online.  But I was happy that it was here!

One of my goals with the Raspberry Pi is assembling a small, cheap computing
cluster, so that I might understand more about distributed computing and 
clustering in general.  My initial plan is a 4+1 node cluster, running distributed
python software by built with the use of the [dispy framework](http://dispy.sourceforge.net/).
I have no real goals for what I want this software to do yet, but the idea
is that if I can get a cluster up and running and talking to each other
with dispy, I can find an embarrasingly parallel problem and tackle it.  
I'm already thinking of running huge Game of Life simulations and such, 
with each node rendering roughly a quadrant of the world.  And other things
too, but that's not important at the moment.

So, what do I mean by a 4+1 cluster?  Well, perhaps my recent system administration
leanings are kicking in here, but I would like there to be a dedicated 
administration and monitoring node, which controls and looks after the
other four nodes, and also acts as the central server which collects
the compute data from the other nodes and stitches it together, massaging
it into a form that's useful.  So there will be four compute nodes, and 
one command and control node.  This might be a bottleneck, and I'm aware
of that.  But I'm not looking for the absolute best performance, I'm looking
for something that's stable, managable, and scalable... plus, the 10/100
NIC on the RPi kind of prevents massive throughput anyway.  As for the
monitoring side of things, I'm writing a package of shell scripts
at the moment to collect system information and generate a webpage.  I
know there are packages out there to do this for me, but I want to write
it myself... it's fun.

So, the RPi I currently have, which I'm calling orison at the moment, 
will end up being the command control node, orison-locus.  The compute
nodes, orison-foci-1 throubh orison-foci-4, will need to be ordered.

Until I have a bit more cash to throw down for this,  I've decided to
play around with what I have.  So, here's a list of what I've done on 
orison so far, and what will probably make it into orison-locus and
orison-foci in the end.

  - Formatted SD card with most recent version of the official Raspian Wheezy distro
  - Enabled sshd to start on system startup
  - Enabled overclocking - Turbo mode (mine has Samsung ram, so it should be fine)
  - Tested overclocking - it works!
  - Set up wi-fi
  - Updated + upgraded all packages from the apt repositories
  - Set up the [watchdog timer](http://binerry.de/post/28263824530/raspberry-pi-watchdog-timer), so if my RPi is ever hung, it will reboot itself, tested this with a forkbomb
  - Changed hostname from 'raspberrypi' to 'orison'
  - Installed avahi-daemon, to allow connecting to the machine with orison.local
  - Installed sysstat
  - Installed gcc-4.7 (gcc-4.6, installed by default, is broken and buggy)
  - Installed git
  - Installed [rpi-update](https://github.com/Hexxeh/rpi-update)
  - Managed to get [Io](http://iolanguage.com/) to compile (iobin package coming later today!)
  - Changed password on the default 'pi' user
  - Created a new user account for myself (should delete the pi user)
  - Edited sudoers to require a password for sudo
  - Set up ssh keys for key-based auth

So I have a fairly stable, overclocking on-demand system now.  I'm happy.
