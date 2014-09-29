---
title: "Adventures in Roguelike Development, Chapter 4: Beginning to See"
date: 2011-06-12
tags: [code-dump]

Hello all,

Welcome to the fourth installment of my roguelike development journal. You can read the previous parts below:

  - [Chapter 1: The Quest Begins!](/?c=36)
  - [Chapter 2: Gathering Supplies](/?c=37)
  - [Chapter 3: Bumps in the Road](/?c=39)
  
This week, I was able to add very basic, buggy FoV and map drawing. I still have to clean the code up a lot, but it works... slowly. The problem with it is that it draws the entire map, every frame. This shouldn't be too much of an issue to work around, but it's annoying right now. But, it works.

When the player is in a room or a corridor, the entire room/corridor lights up (simplified Rogue style). As the player explores the map, it gets saved and when out of range, displayed in a darker grey. This allows for automated map making, while at the same time preventing everything from showing up.

Screenshot: 

Basic FoV

![basic FoV](https://github.com/gatesphere/blog-resources/raw/master/downloads/images/roguelike/roguelike-fov1.png)

Code: [snapshot 20110612](https://github.com/gatesphere/blog-resources/raw/master/downloads/source/rlprototype-20110612.tgz)

Thanks for reading, and

Keep tweaking~ 