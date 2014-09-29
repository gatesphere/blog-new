---
date: 04/11/2013
tags: leo, nodewatch, plugin, ltd, productivity, code-dump
title: Nodewatch for Productivity

Recently, I contributed the nodewatch.py plugin to Leo.  I wrote this as a way to keep myself productive, and have an at-a-glimpse look at important nodes in my workbook.leo file.  I thought I'd share the `@nodewatch` definitions I hacked together to help with this.

Some important notes:

  1. The snippets below are on gist, which does not to my knowledge allow syntax highlighting without a file suffix.  Ignore the .py in the filenames -- those are node headlines.
  2. These definitons require Terry Brown's todo.py plugin to be enabled, else they will throw exceptions and not work.
  3. These definitions use python-dateutil's relativedelta to make my life easier.  You'll need to `pip install python-dateutil` to get these scripts to work.

Some preliminaries first.  All four of the @nodewatch definitions I have below use the same `<< imports >>` and `get_tasks_by_date` nodes as children.  I used clones for this, to keep them all in sync.  Here's `<< imports >>`:

<script src="https://gist.github.com/gatesphere/7306696.js?file=<<+imports+>>.py"></script>

And here's `get_tasks_by_date`:

<script src="https://gist.github.com/gatesphere/7306696.js?file=get_tasks_by_date.py"></script>

Alright... now, get_tasks_by_date() returns a list of vnodes that are not marked 'done' by todo.py, but have a duedate or nextworkdate such that comparator(date,otherdate) is True.  That does *all* the hard work.  Next up is 4 very similar @nodewatch definitions:

<script src="https://gist.github.com/gatesphere/7306696.js?file=%40nodewatch+Past+Due.py"></script>

<script src="https://gist.github.com/gatesphere/7306696.js?file=%40nodewatch+Due+Today.py"></script>

<script src="https://gist.github.com/gatesphere/7306696.js?file=%40nodewatch+Due+Tomorrow.py"></script>

<script src="https://gist.github.com/gatesphere/7306696.js?file=%40nodewatch+Due+This+Week.py"></script>

Putting this all together under your `@settings` node, and clicking the Refresh button (or running the command `nodewatch-update`), you now have 4 categories in your Nodewatch GUI's drop-down box: 'LTD: 00 Past Due', 'LTD: 01 Due Today', 'LTD: 02 Due Tomorrow', and 'LTD: 03 Due This Week'.  This will help you get fast looks at what you need to focus on today, tomorrow, and this week.

Unfortunately, the `get_tasks_by_date` code is a bit ugly and really dense, and it required a read through of the todo.py source, and understanding of the operator module... but it packs a lot of filtering power into those lines, making other due-date sorting @nodewatch definitions easier in the future.  For example, you could define a `@nodewatch Due This Month` script with:

<script src="https://gist.github.com/gatesphere/7306696.js?file=%40nodewatch+Due+This+Month.py"></script>

Plenty of other things can be done with nodewatch, but this is my primary usage so far.