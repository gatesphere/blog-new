---
date: 18/11/2013
tags: tag, your, life, away
title: Leo Things Done Revised

# Introduction

This is a rewrite of my earlier article [Leo Things Done](/2013/09/20/leo-things-done/),
explaining my LTD productivity system as it stands currently.  It is much simplified
from the original version, and now is pretty much just Leo, a few plugins, and
a few scripts.

# The system
LTD is a combination of parts of ZTD and GTD, and it uses Leo to maintain itself.

## What you need
  - A computer with Leo
  - Willpower

## Setting up Leo
The core of this system is Leo.  You'll need the following plugins enabled:
  
  - mod_scripting.py
  - todo.py
  - nodewatch.py
  - contextmenu.py
  
Additionally, you'll need at least the following python module installed:

  - python-dateutil

A .leo outline with the following LTD chapters should be kept:

  - Recurring (for daily, weekly, monthly, etc. tasks)
  - Long-term Projects
  - Notes
  - Ideas
  - Reports
  
I also have a few other chapters, as I run LTD from my workbook.leo file:

  - RSS Feeds (for rss.py plugin)
  - Web Bookmarks

Within each of those LTD chapters, create the following 3 nodes:

  - Work
  - Responsibility
  - Leisure

Within the 'main' chapter, create an '@settings' node.  This will store various LTD-centric
settings, buttons, and scripts.  The scripts themselves are in the ltd-barebones.leo file, 
[up on Github](https://github.com/gatesphere/ltd-barebones).

## Using the system
Use the Notes chapter to scribble down notes that are related to tasks.  You can clone from notes to a child of a task if you wish, to keep
yourself organized.

Use the Ideas chapter to scribble down ideas that are unrelated to current tasks.  Ideas are always good to keep in mind, because in the
future they may be promoted to tasks, once you have the time to approach them, or the desire to do something new.

Use the Recurring chapter for daily, weekly, monthly, etc tasks.  Tasks need a task-type directive (one of '@work', '@responsibility', or '@leisure') in their bodies.
Additionally, recurring tasks need a valid recurrance, one of '@daily', '@daily-weekdays', '@weekly', '@biweekly', '@monthly', '@bimonthly', '@quarterly', '@triannually', '@semianually', '@anually', '@yearly' (a synonym for @anually).  These two directives are used by the LTD scripts, and are very important.  Lastly, using the todo.py Task
tab, set a due date, next-work date, or both.  The scripts will take care of re-setting the dates for you when you complete a recurring task. 

Use the Long-term Projects chapter to keep yourself on track with the long term projects you're working on. Be sure to include a tasktype.  A due-date/next-work-date is not necessary, but supported.

Each day, your flow should be like this:

  - Skim through your Nodewatch 'LTD: 00 Past Due' list and do them -- you've slacked off!
  - Skim through your Nodewatch 'LTD: 01 Due Today' list and do them.
  - If you have time, skim through your Nodewatch 'LTD: 02 Due Tomorrow' or 'LTD: 03 Due This Week' nodes to prepare yourself.
  
When you complete a task, right click on the headline and select 'Mark task done'.  This does a few non-trivial actions for you:

  - Sends a copy of the node to your Reports chapter, under the correct date and category, marking it 'done'.
  - If the task recurrs, it sets the next work date according to the recurrence directive.

Additionally, once a week, write a summarized bullet point list of what you did.  I'm doing mine publicly on this blog.  LTD provides a script for this, too: select a week node in your Reports chapter, and right click on the ltd button, selecting 'generate-week-report'.  You'll now have a nice categorized report for your use of your week's activities.

Thanks for reading!