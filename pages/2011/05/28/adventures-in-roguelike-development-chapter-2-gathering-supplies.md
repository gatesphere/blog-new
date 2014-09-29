---
title: "Adventures in Roguelike Development, Chapter 2: Gathering Supplies"
date: 2011-05-28
tags: [code-dump]

Hello all,

Welcome to part two of my roguelike development journal. (You can read part 1 [here](/?c=36).) This week, I take a divergent path from the guide I started to follow in the first post, but only to get some important steps out of the way. And I even have a source snapshot for you! So, let's begin.

In the last post I mentioned that I was going to work on a random map generator. Well, I've decided to keep that until a later date. However, I have implemented most of the features that I will require to make that work at a base level. This week, I instead chose to focus on cleaning up the code and making it cross-platform from an early stage (and I hope to keep it that way) while implementing some minor features.

New features
------------

Firstly, I added a scrolling message log, which is accessed when the user presses `M`. This outputs all of the messages that the player has received to the screen, starting at the most recent, and working up towards the beginning of the game. The user can scroll this list with `up arrow` and `down arrow` one line at a time, and arrows show up at the top right and bottom right of the screen indicating whether or not there are more messages to see. There is a screenshot at the end of the post to view this in action.

From then, I implemented room drawing (which is bugged, rooms end up being one more tile wide and tall than desired; I will fix it in the next week). To test this, I used randomly generated rooms (without regards to staying within the bounds of the map) and ended up with some interesting cases of collisons. And, as I now was spawing sometimes within solid rock, I decided to implement a `findInitialPosition()` method for the Player class, which looks randomly for an initial position that is not solid. So, at this point I had random rooms filling up a dungeon and I could walk around in them (and sometimes off the map due to how I handle collision).

After this, I added corridors and corridor drawing (which suffers the same bug as room drawing, in respects to length), and added doors to the ends of corridors. This is fine, but the player couldn't open doors yet, so I added that in as well. If the player tries to move onto a location occupied by a door, it is replaced by an open one, and a message is printed to the message buffer, and the player is moved. Simple as pie, but coded inflexibly. I'll touch this up in a later week.

Finally, I added a test map, just to check out if moving between rooms through corridors worked, and it did. The code snapshot below ships with this static map enabled. The player will start out in a random location every time, but the map will remain the same.

Adventures in cross-platform coding
-----------------------------------

I'm sad to say that most of the time that I spent this week was on getting the code to run on my Linux box as easily as it runs on my Windows machine. This was fairly easy due to rlutil's awesome capabilities, but I did hit a few speedbumps along the way. Since this game expects to be run in an 80x25 terminal, I modified the script that came with the Linux version of [DoomRL](http://doom.chaosforge.org/) to run the program in an xterm window of the correct size. This is included in the snapshot as `rl_xterm`.

Due to my own stupidity, I was parsing input in a way that would work perfectly under Windows (due to the arrow keys being single keycodes rather than escape sequences as in *nix) but would fail miserably under Linux. When I first ran the game, it would exit every time an arrow key was pressed. This is partially due to the way that rlutil implements it's `rlutil::getkey()` method, which reads how many characters are waiting to be parsed, and then calls the blocking version of `getch()` on it. Essentially, if you call `getkey()` without checking first to see that there is input to parse, it will call `getch()`, and block, making it seem to act normally. But, because the buffer is checked before the call to `getch()`, the method won't know that there are multiple characters to be examined, and will just examine the first, which in the case of the arrow keys on Linux, end up being the escape character. On Windows, this problem didn't show up, thanks to the fact that arrow keys report one character on Windows machines. But, a simple empty while loop to check `kbhit()` before the call to `getkey()` saved the day.

And one more hurdle to jump, it seems that on Linux consoles, sometimes the output of keyboard interaction is echoed to the console. To work around this, I simply placed the cursor in a location that I know will be overwritten in the next frame. Simple, but kludgy. I'll look for other ways around this.

A word on setting
-----------------

Lastly, I finally came up with a setting for this game. Well, actually two, but only one that I'm sharing with you. It will be an infinite rogue clone. Basically, a coffee break roguelike, you create a character and see just how many levels you can progress down the dungeons of doom/peril/strange sounds. There will be no end-game to speak of, just insane difficulties in lower levels, and maybe a shop every 20 floors or so to restock.

The other setting/game idea I have is much more interesting, but I want to try the basics first. :)

A word on the code
------------------

Thanks to the prodding of jimdoescode and hugoblack on [/r/roguelikedev](http://reddit.com/r/roguelikedev), I'm including a snapshot with each post from now on. The build instructions are simple, and should work on any system with a decent GCC installation (excepting Cygwin, rlutil won't compile on Cygwin witout serious modification, and MinGW works so much nicer anyway). Simply gunzip and untar the archive, and do a `make`. You might want to check your system's compatibility with rlutil first by running `make test & ./rlutil-test`. Either way, the roguelike itself will be named `rl` (unique, huh?). If you're on a Linux box, I recommend running `./rl_xterm` to run it for now, but feel free to run it in anything you like. Oh, and I also included a small utility I used to test keycodes in rlutil. To compile it, run `make key`. It will check for input, and print out the keycode as they're pressed. `^C` to kill it. And as always, `make clean` will clean it all up for you.

The license is in the header of the `main.cpp` file, and rlutil is released under the [WTFPL](http://tapio.github.com/rlutil/docs/License.txt).

Screenshots: 

the message buffer

![message buffer](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/roguelike/roguelike-messagebuffer.png)

random rooms

![random rooms](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/roguelike/roguelike-randomrooms.png)

random corridors

![random corridors](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/roguelike/roguelike-randomcorridors.png)

test map

![test map](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/roguelike/roguelike-firstmap.png)

Code: [snapshot 20110528](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/rlprototype-20110528.tgz)

Keep tweaking~ 