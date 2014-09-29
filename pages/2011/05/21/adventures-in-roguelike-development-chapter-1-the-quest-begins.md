---
title: "Adventures in Roguelike Development, Chapter 1: The Quest Begins!"
date: 2011-05-21

Hello all,

This is the first post in a multi-part series chronicling my efforts in creating a roguelike game. For those of you unfamilliar with the roguelike genre, you can read more about them on [RogueBasin's "What a roguelike is"](http://roguebasin.roguelikedevelopment.org/index.php?title=What_a_roguelike_is) page.

In order to give myself some guidance for this project, I've decided to adopt (with some slight variations) the development path laid out in [How to Write a Roguelike in 15 Steps](http://roguebasin.roguelikedevelopment.org/index.php?title=How_to_Write_a_Roguelike_in_15_Steps). And, each part of this series will be broken down into a number of these steps.

Step 1: Decide to Write a game
------------------------------

Well, for this, I've pretty much decided the bare minimum. I want a basic roguelike game, with one screen maps (no scrolling), with a console only interface (I don't personally like tiles, they distract me). That was simple.

Step 2: Hello world!
--------------------

I've chosen to write this in C++, using GCC compilers whenever possible, which should be on any of the three major platforms. To assist with console work, I've chosen to use (and subsequently modified) [rlutil](http://tapio.github.com/rlutil/). Everything else, I've decided to roll on my own using the C++ standard library and the STL. After writing a few test programs, I've determined that everything works (with some minor modifications to rlutil--to be released at a later date).

Step 3: It's a boy!
-------------------

For the screen layout, I've decided that the top two lines are to be messages, the bottom three lines are to be status, and the map itself will take up the middle twenty, with one column of buffer on both the left and right, to a total size of 78x20. This brings the console window to the standard 80x25, and looks quite nice as a layout (screenshot later).

From then on, I built a basic "@ running around a screen demo" (the roguelike hello world, as it were), and then added message handling. I then decided that the player will be the '@' symbol, walls will be '#', closed doors will be '+', open doors will be '/', and open ground will be '.'. Everything else didn't need to be settled yet, and in fact, the open door symbol is pointless at this stage as well.

Step 4: The map
---------------

Here's where I diverged from the path a bit. I started off with a hard-coded map (just an array of chars at first, later expanded into MapEntity instances), and allowed the player to walk overtop of the map, ignoring collision. I then added collision detection (along with a proper message in the message buffer), at first just to walls, and then to closed doors. Other entities (such as creatures) will be easy to add later to this collision detection scheme.

At this point, I began thinking of how to implement field of view. I've decided that a part of the player's map will remain drawn on the screen in dark grey after it has been visited, but it will be out of the range of vision, leaving monsters and items and the like unseeable. For things in direct vision, I've decided to go with a modified version of Rogue's field of view. In Rogue, the player is able to see the entire contents of any room they are in, even if they're just standing in the door way. In corridors, they are able to see just one tile ahead and behind them. My version of this will light up entire rooms of contents while they are in the room, and light up a longer range of tiles in corridors, maybe 4 or 5 in each direction, to allow for a bit more strategic play.

In order to implement this, I need to implement rooms (already done) and corridors (next on my todo list), and I decided that just for fun, I should implement a random level generator in the process, just to do something fun before I dive back into the nuts and bolts work. So, I'm going to write a rough level generator, then work on field of view, and then go back to the path.

And there's my progress thus far. I have 6 basic commands implemented (4 movement - bound to the arrow keys, rest - bound to 'r', and exit - bound to 'ESC'). There is also a turn counter, just as a rudamentary system for time (to be extremely expanded later, I'm thinking in the style of [DoomRL](http://doom.chaosforge.org/)). When the player tries to do something it can't, there is an appropriate message pushed to the message buffer, and the turn count isn't incremented. Resting does nothing at the moment but push "You rest." to the buffer and increment the turn count, but in future versions, it will act as it does in most roguelikes to restore health and mana while allowing monsters to move.

Here's a screenshot:

Roguelike Prototype screenshot 1

![rl-proto-1](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/roguelike/roguelike-1.png)

And as I've found these resources to be helpful, here's a list of good places for people who are looking to get into roguelike dev to check out:

  - [RogueBasin](http://roguebasin.roguelikedevelopment.org/index.php?title=Main_Page)
  - [RoguelikeDevelopment.org](http://roguelikedevelopment.org/)
  - [Temple of the Roguelike](http://www.roguetemple.com/)
  - [rec.games.roguelike.development newslist](http://groups.google.com/group/rec.games.roguelike.development/topics) (on Google Groups)
  - [GameDev subreddit](http://www.reddit.com/r/gamedev)
  - [Roguelikes subreddit](http://www.reddit.com/r/roguelikes/)
  - [RoguelikeDev subreddit](http://www.reddit.com/r/roguelikedev/) (moderated by me, in the efforts of full disclosure)
  
Thanks for reading, and comments are always welcome! Oh, and yes, I do intend to opensource most of this project (if not all) when I'm done with it, including my modified rlutil.

Keep tweaking~ 