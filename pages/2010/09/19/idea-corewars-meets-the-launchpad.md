---
title: "Idea: CoreWars meets the LaunchPad"
date: 19/09/2010

Hello all,
I stumbled upon a really cool project called [Battle Droids](http://battledroids.net/) for the Atmel AVR microcontrollers. Basically, you build a physical representation of a battle droid by building a circuit of sensors around an AVR, then program it with their firmware, connect it to your computer, and have it do battle online through a client software. Your droid would gain experience, level up, and be able to purchase upgrades by winning fights. Unfortunately, this project has stagnated and seems to be out of development, and stuck in pre-beta with nothing of any note released.

Now, years ago, as a kid, I used to play [Core War](http://en.wikipedia.org/wiki/Core_War) (or CoreWars, how I say it). Basically, in CoreWars, you write a program in Red Code, a modified version of ASM, and have it do battle on a virtual "hill" to claim the title King of the Hill.

Here's where the idea is... I would like to something smimilar to CoreWars (with the emphasis on programming), but add in a physical layer like Battle Droids. Basically, you would choose a core, build a circuit of sensors and other input devices, write a program to control it, and have it fight other internet-connected bots. I think I'd call it something like "LaunchBots" or something else equally cheesy.

Here are some basic rules:

  1. All programs would have to be submitted to the administrator of the hill for verification and compilation. This is to allow the administrator to add a bit of security code to the file to allow the program to be authenticated by the server, to help prevent cheating. All programs will be checked against the guidelines set forth in the bot protocol document, and against the hill it was submitted for. An approved program will be sent back, compiled, with a secret security code added into the binary. This compiled binary is what the commander would upload to their bot.
  2. All programs must be written in C or MSP430 ASM, and have specific notes regarding which compiler to use. Programs which do not compile will not be accepted for obvious reasons.
  3. All bots would need to have a photo and a schematic submitted along with the program.
  4. All bots would need to connect using the client software, unmodified. This is to allow the authentication of bots and programs, and to prevent cheating. The client software will be open source, but will contain obfusticated encryption algorithms to help preserve the integrity of the competition.
  5. All commanders would be required to have their bot connected and the client software running during the entirety of the scheduled battle time. Any bots not connected when the battle is scheduled to begin will be disqualified, as will any who lose connection more than twice in a match. Disqualified bots will recieve maximum negative points for their leaderboard standings.
  
There will be a bot protocol document describing the various items to take into consideration during programming, including specifications which must be adhered to. There will be different speed classes (directly proportional to baud rate)- 4800 baud, 2400 baud, 1200 baud, 600 baud, 300 baud, 110 baud for stock, higher classes may be created for those using an external serial or usb-serial converter (such as an FTDI). Such classes would be subject to approval by a judge. Speed class is directly related to how quick your bot would be able to issue commands, but comes at a price of code size and efficiency.

There will also be various core classes, depending on the MSP430 device used (only ones supported directly by the LaunchPad's 14/20 pin socket will be allowed to compete).

The server software will be open source, allowing for people to run their own hills with or without the verification steps, and also to allow the builders/coders to test their bot before submitting it.

That's it for the basic idea. I'm going to look into this as a serious idea, and I welcome any suggestions/help from anyone else who thinks this would be a cool idea. If anything comes of this, it would be a LONG way away, but it would still be a really fun thing, I think. Let me know below!

Keep tweaking~ 