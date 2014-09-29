
---
date: 01/02/2013
tags: leo, literate programming, text editor
title: Leo is Love

Hello all.

Today I'm writing to evangelize my newest addiction, [Leo](http://leoeditor.com/).

Leo is a text editor, PIM tool, outliner, visual literate programming IDE, database, and way of life.  Since
discovering it a few days ago, I've started using it exclusively.  In fact, this very article was written with
it.

I thought I'd share a few tips on how to get it up and running on Windows systems, and then a few little 
snippets of fun that I've picked up along the way.

Installing Leo on Windows systems
---------------------------------
Getting Leo running on Windows systems isn't as difficult as it seems.  You do need a few things, though:

  1. Python 2.7, 32-bit.  Available [here](http://python.org/ftp/python/2.7.3/python-2.7.3.msi).  64-bit 
     Python does not work for PyEnchant, meaning that you won't have spellcheck if you go that route.  Also,
     there isn't a 64-bit setuptools package at the moment, so installing docutils will be difficult.  But Leo 
     doesn't need much RAM, so this isn't a problem.
  
  2. PyQT for 32-bit Python 2.7.  Available [here](http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.9.6/PyQt-Py2.7-x86-gpl-4.9.6-1.exe).
  
  3. PyEnchant for Python 2.7.  Available [here](http://pypi.python.org/packages/any/p/pyenchant/pyenchant-1.6.5.win32.exe).
  
  4. setuptools for Python 2.7.  Available [here](http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe#md5=57e1e64f6b7c7f1d2eddfc9746bbaf20).
  
  5. The latest Leo snapshot.  Available [here](http://www.greygreen.org/leo/leo-editor-latest.zip). 
  
  6. Optional: create-leo.bat, available [here](https://gist.github.com/4692706).

### Install Python, PyQT, PyEnchant, and setuptools, in that order.
Pretty straight forward.  Just accept the defaults and continue.

### Install pip and docutils
Open up a command prompt, and enter the following commands:

    cd C:\Python27\Scripts
    easy_install.exe pip
    pip install docutils
    
### Unzip the leo snapshot
Pick somewhere you'll remember it.

That's it.  You can now run Leo by doubleclicking `launchLeo.py`.  However, we can integrate it into 
the OS a bit more, making it much nicer to use.

### Optional: run create-leo.bat
Copy `create-leo.bat` to your Leo directory (the one with `launchLeo.py`).  Now open a command prompt,
and do the following:

    cd C:\path\to\leo
    create-leo.bat "C:\Python27\python.exe" register
    
That will do 2 things: create some .bat files, and register the .leo file extension to open with Leo.
You are free to move `leo.bat` and `leoc.bat` anywhere on your system... double-click them and Leo
will run (`leoc.bat` keeps the console open).  Sinde .leo was registered to open with Leo, you can
double-click on any .leo file to open it in Leo, too.

Congratulations, you have Leo on your system.

Some Leo Tricks
---------------
### Set up your myLeoSettings.leo file
Seriously, there's crazy power in this file.  It allows you to change the way most of Leo works.

Me? Mine's pretty simple at the moment.

    @settings
    - Plugins
    --- @enabled-plugins <- I've disabled the nav_qt.py
                            plugin, as I find it annoying
    - Keyboard Shortcuts
    --- @shortcuts MyKeybindings <- I've assigned `tab-cycle-previous` 
                                    and `tab-cycle-next` to 
                                    `ctrl+shift+tab` and `ctrl+tab`, 
                                    respectively, as it mimics how 
                                    Firefox and Chrome handle 
                                    tab-switching

### Make some @buttons with external script references
I wanted to make some @button nodes which would call a function with different parameters.  Due
to the way Leo scopes things, it wouldn't work to write the function in a separate script and
reference it with a `<< script reference >>` notation, as in a @file node -- it won't be expanded.

The solution, provided to me on the leo-editor Google group by the author of Leo himself, is brilliant.

> Use exec to "inject" shared code into the namespace of the script being executed.   This is a cute trick, but it doesn't seem to be in the faq.  There are example of this trick in unitTest.leo:  search for "@common".
> 
> Do the following:
> 
> A. Put the common code somewhere, say in a node called "@common code".  Note that the node can be called anything: I use @common to draw they eye, but it's just my convention.
> 
> B. Start each script using the common code with::
> 
>     exec(g.findTestScript(c,'@common code'))
> 
> `g.findTestScript` returns the *expanded* code of the entire subtree whose head is the node "common code".  Thus, you can use @others and section references in the "common code" subtree! It's cute.

This translates into something like this:

    Node `@common code`:
      def foo(bar):
        g.es("Hiya, %s!" % bar)
        
    Node `@button george`:
      exec(g.findTestScript(c,'@common code'))
      foo('george')
      
    Node `@button clem`:
      exec(g.findTestScript(c,'@common code'))
      foo('clem')
    
2 buttons calling 1 script, without code repetition!  This is nice, and it shows the power that Leo has, by
giving you the ability to access your entire document programmatically.  Simply beautiful, in my book.

I've used what I've learned so far to begin creating a Leo workbook helpful for running tabletop RPGs.  It's
on Github if you're curious: [gatesphere/rpg.leo](https://github.com/gatesphere/rpg.leo).

Thanks for reading!