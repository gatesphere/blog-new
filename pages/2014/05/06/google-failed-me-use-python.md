---
date: 2014-05-06
tags: [python, stupid tricks, sysadmin, Solaris 10]
title: Google failed me, use Python!

So, yesterday I needed to know whether or not Solaris 10 enforces the maximum open file handles limit for processes running as root (I know, root-level processes are bad form... but it's legacy, so there's my excuse).  Google told how to set it, how to check it, and what it defaults to, but didn't give me the all-important info of whether or not root is limited by it.  So I decided to hack together a quick script to test it empirically on the server in question.

I was going to try it in bash, but it turns out that bash is too smart for it's own good here -- there's no trivial way of opening a file descriptor without it autoclosing on you.  So I went with Python instead, carefully avoiding the `with` keyword.  Here's what I hacked together:

    #!/usr/bin/env python
    
    n = 10000
    
    fds = []
    
    for i in range(n):
      fname = 'testfile' + str(i)
      fds.append(open(fname, 'w+'))
      print i
    
Its short, hacky, depends on throwing an exception to kill it (if indeed there is an imposed limit), and forces the user to manually clean out the filesystem of all `testfile*` files, but it worked.  The result: yes, root is indeed slave to the kernel, and can only open up as many file descriptors as `plimit $$` claims.

I love Python. :)
