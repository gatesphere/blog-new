---
date: 17/12/2013
tags: silica, pl theory, music, code
title: Thoughts on Silica2

This post is really just a place for me to 'think in public' -- not meant to be terribly interesting to anyone but myself, but also to allow me to get my thoughts out there.

Silica2 (which will just be called Silica) will be the new version of my previous work on [silica](https://github.com/gatesphere/silica).  The original silica is written in Io, with a rendering engine in Java and Processing.  As my current language of choice is Python, Silica2 will be written in Python.  I intend on supporting the following features:

  - A good chunk of the Clay programming language (primitives, macros, commands, transforms, scales, modes, etc.).  I will be renaming some of these, however.  With Silica2, I'd like to draw a bit more of a distinction between Clay and Silica.
  - Namespaces, as silica implemented them
  - Functions, as silica implemented them
  - User-defined Scales + Modes, as silica implemented them
  - A plugin architecture
  - Multiple rendering modes (sonic, visual, score, text, MIDI, etc)
  - Embedded python
  - Scripting, with environment bootstrapping (ala .silicarc)
  - World images exportable and importable (as .leo files)
  - Multiple UI choices: cli (default), GUI, Leo-bridge

The embedded python feature is what I'm really interested in.  Allowing users to run python code *within* silica scripts will allow some very easy *runtime manipulation* of silica itself.  This Aha was inspired by my work with Leo, and I think it will be absolutely *vital* to silica2's adoption.  Silica2 will be perfectly capable of running without the embedded python scripting, but advanced users will be able to implement plugins in silica scripts!  The entire silica2 api will be exposed with a few simple objects (again, thanks to Leo for this idea), and can be manipulated as silica2 is running.  This includes adding stages to the parser, changing/adding new primatives, manipulating MIDI data directly, the whole shebang!

These are exciting times.  Very, very exciting times.

Oh, for technology:

  - Python 2.7 (perhaps also make it python3 compatible)
  - mingus
  - fluidsynth
  - PyQt4
  - pyparsing (perhaps -- I might roll my own parser instead)
  - Leo (optional)

I also intend to make easy installers for it all as well.  We'll see how it goes.

Thanks for reading!