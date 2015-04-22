---
date: 2014-01-28
tags: [leo, scripting, tutorial]
title: Intro to Leo scripting

Hello all,

I thought I'd do a tutorial on scripting Leo today.  It's a tricky but powerful feature of my favorite editor, and one I think deserves more attention.  For those who are interested in learning more than what I touch on here, the [official Leo documentation](http://leoeditor.com/leo_toc.html) has both a [tutorial](http://leoeditor.com/tutorial-scripting.html) and a [neat script tricks](http://leoeditor.com/scripting-miscellany.html) page.  Also, a very useful (but regrettably incomplete) resource is the [Leo API documentation](http://leo-editor.readthedocs.org/en/latest/).

## **Before we begin**
This tutorial assumes you have Leo installed, and know the basics of its operations -- i.e., how to create and move nodes around, how to use `<< section >>` references and the `@others` driective, and how to configure Leo's settings.  Additionally, it assumes you have the `mod_scripting.py` plugin enabled, but Leo ships with this by default, so you should be set.  Also, you can't script Leo if you don't know basic Python, so brush up on that first too.

## **Your first script**

Let's begin simple.  Open up a new .leo file and create a node.  Let's call it 'hello'.

The body of this node should be the following:

    @language python
    g.es('Hello, world!')

That is your very first Leo script!  It's the Leo equivalent of the famous 'Hello World' program.  One note -- 'g.es' isn't a very clear name.  It means 'echo string', where the target of the echo is the Log pane. It is short and easy to remember, so it's stuck around a while.  Also, it's used often, so it is good to have a short name.

Let's run it.  Make sure you have the node selected in the outline pane, and then type Ctrl-B.  You should see `Hello, world!` in the Log pane.

## **About Ctrl-B**
What's so magical about Ctrl-B?  Nothing, really.  it is just a keybinding for executing the command `execute-script`.  Instead of doing a Ctrl+B, you could instead do Alt-X `execute-script` in the minibuffer, and the script would run as well.

## **About Buttons**
There's another way of running your 'hello' script: a script button.  Up at the top of the Leo screen you should see a yellow button that says 'script-button' on it.  Clicking this button adds another button to the bar which runs the script that you had selected when you clicked the yellow button.  Highlight your 'hello' node and click script-button.  A new 'hello' button should now be on the bar.  Click it -- you'll see that your hello script runs!

Note, buttons are powerful.  They run their script no matter which node is selected in the outline pane.  This is an important feature that we'll run into later when we write scripts that modifiy other nodes!

To make a button automatically when your .leo outline runs, simply put `@button` in front of the script's headline.  Do this with 'hello' (so that the headline now reads '`@button hello`'), save your outline, and close Leo.  Now reopen Leo and your outline.  You should have a 'hello' button automatically created.

## **Leo Scripts -- the important facts**
The unique thing about Leo is that the entirety of Leo's codebase is accessible from Leo scripts.  This means that your scripts can modify and access the data in your current outline.

Another powerful feature is that your Leo scripts are fully-functioning python scripts.  Any valid python code is a valid Leo script.

The third powerful feature is that Leo expands your scripts just like it expands your @files, meaning you can (and should) use `@others` and `<< section >>` references in your scripts to make them more readable.

Lets combine some of these features to make a more powerful script.

## **Going Deeper -- Leo's API**
Say we wanted a button that would create a new @file node with some pre-filled information gathered from the outline.  I use a similar script to the one we'll be building here in the .leo file I use to write this very blog, actually!

Say you had a 'design-notes' node, under which you had various 'class' nodes, under which there were 'method' and 'property' nodes.  These are just notes, but you'd like a script to transform them into a proper Python file filled with functions you can stub out.  Here's the data I'm going to be using for this example (Headlines start with '-', but that's not actually a part of the headline.  Body text is indented two spaces beneath the headline.  Child headlines are indented 4 spaces from the parent headline):

    -design-notes accumulator.py
      A general accumulator and reverse accumulator class library
        -class Accumulator
          An accumulator that counts up
            -method __init__
              constructor
            -property value
              the current count
            -method tick
              increases value by 1
        -class ReverseAccumulator
          An accumulator that counts down
            -method __init__
              constructor
            -property value
              the current count
            -method tick
              decreases value by 1

Create this outline in a new .leo file -- our script will be needing it.  If you want, you can use clones for the 'method \__init__' and 'property value' nodes, as they're identical.  Our script won't care one way or the other.

## **First things first**
The first thing we want from our script is a button.  This is simple.  Create a new top-level node named '@button design-to-file'

The body of that node at this point should look like this:

    @language python

    << declarations >>
    
    #to do: logic
    @others


Next, to make our lives easier, make a child node named '<< declarations >>', with this body:

    # the following are Leo directives, so we have to trick 
    # Leo by constructing them in the script
    # we'll be using them a lot, so doing it once here saves
    # typing later
    others = '@' + 'others'
    docstring = '<' + '<' + ' docstring ' + '>' + '>'
    imports = '<' + '<' + ' imports ' + '>' + '>'
    declarations = '<' + '<' + ' declarations ' + '>' + '>'

Alright, now to do something.

## **Make an @file node**
The first step to getting our design-notes into a @file is to create a new node and fill its headline and body with the right stuff.

At this point, I should mention the three variables that Leo exposes to scripts.  `g` is the 'globals' variable, and contains all sorts of useful functions that work all throughout Leo (including the `g.es` we used earlier).  `c` is the current outline's 'controller', an object that has information and methods pertaining to the current outline, such as controlling the selection, redrawing, etc.  `p` is the currently selected node in the outline pane, and is really just a shortcut for `c.p`.

We're mostly interested in `p` today, particularly `p.h`, `p.b`, and `p.insertAsLastChild()`.  `p.h` is the headline of the node `p`, and `p.b` is the body.  `p.insertAsLastChild()` returns a new node as the last child of `p`.  We'll also be seeing `p.copy()` which returns a copy of `p`, and `p.insertAfter()` which returns a new node that is a sibling of `p`, as well as `p.children()`, which is a python generator that yields all the child nodes of `p`.

If you understood the above, you're likely beginning to see the power of these three variables.  Indeed, the entirety of Leo's codebase is accessible through them.  But we'll slow down a bit now.  Let's make a @file node.

In `@button design-to-file`, add the following below the `@others` line:

    # get the design node
    designnode = p.copy()
    if not designnode.h.startswith('design-notes'):
      g.es('Not a design-notes node, exiting.', color='red')
    else:
      # create the @file node
      filenode = create_file_node(designnode)
      
      # create the class nodes
      create_class_nodes(designnode, filenode)
      
      c.redraw_now()
      g.es('Done', color='forestgreen')

That's the body of our script -- the heavy lifting will be handled by the various functions defined in it.  The `p.copy()` bit is needed because we're going to be changing the outline.  When the outline changes, positions become invalid, so we need to get a copy of the position before that happens.

We see that we're going to need `create_file_node` and `create_class_nodes` functions.  We're starting with the `create_file_node` function here.  Create a child node named 'create_file_node' and fill it with this:

    def create_file_node(designnode):
      # create the @file node
      filename = designnode.h.split(' ',1)[1] # trim the 'design-notes'
                                              # from the headline
      filenode = designnode.insertAfter() # create a new child
      filenode.h = '@file %s' % filename # set the headline of 
                                         # the new node
      # set the body
      filenode.b = """@language python
      
    %s
    %s
    %s
    
    %s
    """ % (docstring, imports, declarations, others)
      
      # create the docstring node
      docstringnode = filenode.insertAsLastChild()
      docstringnode.h = docstring
      docstringnode.b = '"""%s"""' % designnode.b
      
      # create the imports node (empty)
      importsnode = docstringnode.insertAfter()
      importsnode.h = imports
      
      # create the declarations node (empty)
      declarationsnode = importsnode.insertAfter()
      declarationsnode.h = declarations
      
      # return the filenode
      return filenode
    
The code is fairly straightforward, but basically it creates a new @file node, gives it a proper body, and then creates the << docstring >>, << imports >>, and << declarations >> nodes that the body references.  It also fills in the << docstring >> node with the note we typed into the design-notes outline.

If you comment out the `create_class_nodes` line from the script body, this script will already run.  Make sure the design-notes node is selected, and click the button.  You should get an @file node with some << section >>-style children.  Hooray, progress!

## **Make the class nodes**
Next up is `create_class_nodes`, which will search through the children of a node that it was passed and create nodes specifying classes with the appropriate methods.

The first part of this is to create the class nodes.  Here's the code for create_class_nodes, which goes into a node called 'create_class_nodes':

    def create_class_nodes(designnode, filenode):
      for ch in designnode.children():
        create_class_node(filenode, ch)

This doesn't do much at all!  It just cycles through every child node of the designnode, which is the node with the name 'design-notes blah...', and then calls a helper method `create_class_node` with it, and the destination @file node.

Here's what `create_class_node` looks like (again, in a node called 'create_class_node'):

    def create_class_node(filenode, classnode):
      # create the class node
      newclassnode = filenode.insertAsLastChild()
      newclassnode.h = classnode.h
      newclassnode.b = """%s:
      %s
      %s
    """ % (classnode.h, docstring, others)
      # create the docstring node
      docstringnode = newclassnode.insertAsLastChild()
      docstringnode.h = docstring
      docstringnode.b = '"""%s"""' % classnode.b
      
      # create the method nodes
      # ignore the property nodes -- they're notes
      create_method_nodes(newclassnode, classnode)
      
This code creates a new child node under the @file node, and fills in the headline and body appropriately.  It then creates a child << docstring >> node underneath that, and fills that in appropriately too.  Finally, it calls yet another helper, which creates the method nodes underneath it.

`create_method_nodes` is similar to `create_class_nodes`, in that it is a wrapper around a helper:

    def create_method_nodes(classnode, designnode):
      for ch in designnode.children():
        if ch.h.startswith('method'):
          create_method_node(classnode, ch)

This time around, `designnode` refers to the node with the name 'class Blah...'.  And our good friend the helper method comes along again with `create_method_node`:

    def create_method_node(classnode, methodnode):
      newmethodnode = classnode.insertAsLastChild()
      newmethodnode.h = methodnode.h.split(' ',1)[1]
      newmethodnode.b = """def %s(self):
        \"\"\"%s\"\"\"
        pass
    """ % (newmethodnode.h, methodnode.b)

This method does perhaps the least bit of work in the whole script.  It creates a new node, gives it a proper headline, and fills in the body with a empty method definition (all it does is `pass`), along with a docstring.
