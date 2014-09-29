---
date: 02/12/2013
tags: model, python, code-dump, segregation, complexity, schelling
title: A Simplified Schelling Model

I coded up a simplified version of the [Schelling segregation model](http://en.wikipedia.org/wiki/Thomas_Schelling#Models_of_segregation) today.  I thought I'd share the code below.

<script src="https://gist.github.com/gatesphere/7757287.js"></script>

Here's some output (with `numcells` above changed to `40`):

<pre>
+.++++++ .+.+.....++.++....++...++....+..+.. ++.++
+.++++++ .+.+.....++.++....++...++....+..+.. ++.++
+.++++++ .+.+.....++.++....++...++....+..+.. ++.++
+.+++++++.+.+.....++.+ ....++...++....+..+.. ++.++
+.+++++++.+.+.....++.+ ....++...++....+..+.. ++.++
+.+++++++.+.+.....++.+ ....++...++....+..+.. ++.++
+.+++++++.+.+.....++.+ ....++...++....+..+.. ++.++
+.+++++++.+.+.....++.+ ....++...++....+..+.. ++.++
+.+++++++.+.+.....++.+ ....++...++....+..+. .++.++
+.+++++++.+.+.....++.+ ....++...++....+..+. .++.++
<...snip...>
+++++++++++++......++++....+ ... +............++++
+++++++++++++......++++....+ ... +............++++
+++++++++++++......++++....+ ... +............++++
+++++++++++++......++++....+ ... +............++++
Done
</pre>

Pretty neat -- it works!  I love complexity.