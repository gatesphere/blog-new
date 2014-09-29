---
date: 2013-11-26
tags: [acme, ui, ux, editors]
title: Exploring Acme

For this post, I want to try a little something different.  I'd like to examine the text editor [Acme](http://en.wikipedia.org/wiki/Acme_(text_editor\)) from [Plan 9 from Bell Labs](http://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs) and [Inferno](http://en.wikipedia.org/wiki/Inferno_(operating_system\)).  I think Acme represents a fundamentally different way of interacting with a system than what the vast majority of users use today -- and one I wouldn't have even been inclined to give a shot if I hadn't already been mired in Leo's UI.

# What is Acme
Acme is one of the default text editors for the Plan 9 OS.  Plan 9 in itself is fascinating, and a real study on 'the future, yesterday' in OS design... but that's another topic altogether.

Acme is a mouse-heavy design, which has been optimized for developers, or at least that's what its author claims.  I find this approach of mouse-dependence to be refreshing in an increasingly keyboard-is-king UI world.  Acme actually *requires* a three button mouse... but it fully uses those three buttons to their fullest extent.

Acme also presents what I'm going to call a 'fluid UI'.  Everything in Acme is text, and editable text at that.  Gone are notions of tabs, widgets, controls, and other traditional UI trappings -- text is king.  And it works surprisingly well.

# Mouse functions
As mentioned above, Acme requires three mouse buttons to use.  This is due to each of these being assigned a specific action:

  - Left: move cursor (click), select (drag)
  - Middle: execute (click), select+execute (drag)
  - Right: get (click), select+get (drag)

The left mouse button operates as expected, moving the cursor around the screen and selecting text.  The other two are where it gets interesting.

The right mouse button performs a command called 'get'.  This is a combination of things, depending on what you're 'getting':
  
  - Scope: if nothing is highlighted, it's the nearest 'chunk' to the mouse pointer.  If something is highlighted and that is right-clicked on, the whole hightlighted item is what 'get' looks for.
  - Types: 
    - First, 'get' looks for the item as a file or directory.  If the item is a directory, 'get' dumps the contents of the dir into a new window.  If the item is a file, the contents of the file are dumped into a new window.  If the filename has a :linenumber, the cursor is automatically moved to that line.
    - Next, it checks if it's a manpage definition, i.e. 'cat(1)'.  If so, it loads the manpage in a new window.
    - Next, it checks if it's a URI, and if so dumps the contents of that into a new window.
    - Finally, if it's none of the above, it performs a wrap-around, case-sensitive search for the chunk in the current window.

Handy!

Middle mouse acts similar:

  - Scope: identical to 'get'
  - Types:
    - Shell command, like 'ls -l'.  Executes the selected code and dumps the result into a new window.
    - Acme command, which do various things:
      - 'Cut': as expected
      - 'Del': deletes the current window
      - 'Delcol': deletes the current column and all it's windows
      - 'Dump': saves the state of acme to a dumpfile
      - 'Edit': executes a [Sam](http://en.wikipedia.org/wiki/Sam_(text_editor\)) command in the current window
      - 'Exit': as expected
      - 'Get': load file
      - 'Load': load dumpfile created by 'Dump'
      - 'Look': see right-mouse 'get'
      - 'New': make a new window
      - 'Newcol': make a new column
      - 'Paste': as expected
      - 'Put': write a window to a file
      - 'Redo': as expected
      - 'Snarf': called copy in most other editors
      - 'Undo': as expected
      - 'Zerox': make a copy of the window with the selected text

It's important to note that as Acme provides a completely fluid interface, all of these are simply typed in and then middle-clicked.  No buttons!  The interface stays out of your way until you explicitly *tell* it to exist.

# Mouse chording
The last neat thing that Acme does to squeeze every ounce of utility out of the mouse is mouse-chording, or binding commands to combinations of mouse clicks.

Select some text with the left button, and while still holding left, middle click is a 'cut'.  Right click with left held down is a 'paste'.  Left held down, followed by middle then right click is a 'snarf'.

Double clicking left mouse allows for quick text selection.  Beginnings of lines when double clicked select the whole line.

Fun stuff.  I highly suggest giving it a whirl.  :)
  

  