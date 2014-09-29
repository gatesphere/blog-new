---
title: Another blahgger update
date: 29/09/2010

Hello all,
I've pushed out a new version of blahgger to the server. This release contains very minor changes to the appearance of certain aspects of the blog, but add some interesting functionality in the form of a user-definable top-bar.

The bar at the top with the links is dual purpose. Using the same table in the MySQL database, the user can define either a static link to an external site, or a link to an internal custom content page. By setting a flag (called "link") to 1, it is marked as a link by the DB parser and generates a link out of the value of "content". However, if "link" is set to 0, the value of "content" is used to generate a hidden page of sorts, and the top-bar links to this page. This all happens in a simple 4 field table. The thought occurred to me today, and I somehow found enough free time to implement it.

This feature will also be making its way (under the hood) into ceekrt, sometime in the future, to remove the dependency on external pages for the "contact", "disclaimer", and "about" pages.

I still need to write a backend, and re-format the comment form before I'll be comfortable in releasing the source, but until then, I think that this blog (and blahgger) is looking good and shaping into something really professional and minimalist.

That's all for now. Any comment is appreciated :)

Keep tweaking~ 