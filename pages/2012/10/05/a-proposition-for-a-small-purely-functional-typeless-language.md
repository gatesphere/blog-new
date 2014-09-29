--- 
date: 05/10/2012
tags: axio, functional, language, Turing, lambda
title: A proposition for a small purely functional, typeless language

So, one of my favorite pasttimes is language design, and a few weeks ago
I whipped up the following grammar for a purely functional, typeless
language, which consistes solely of lambdas and symbols.  It's essentially
the \\(\lambda\\)-calculus, with global, immutable binds (much like 
substituting a symbol).

Anyways, here's the grammar:

    lam ::= (\ var1 ... varn :: exp)
    
    exp ::= lam
          | var
          | (prim exp1 ... expn)
          | (exp1 ... expn)
         
    prim ::= #bind | #halt

Aside from the grammar, comments are defined with double slashes and run
to the end of the line, C++/Java style.

The two primitives have the following meaning:

    (#bind sym val) => binds sym to val in the global symbol table
    (#halt exp)     => evaluates exp and returns that value to the 
                       calling context (OS level) as a string

As I mentioned, it's small.  Masochistically small, it appears.  There's
also absolutely no concept of I/O aside from return values.  But it fully 
supports the \\(\lambda\\)-calculus, and therefore is Turing complete.

However, in implementation, a few things would be pre-bound to make
the programmer's life simpler.  These would not be part of the grammar,
and therefore not a part of the syntax of the language, as they would be
stored like any other bound symbol internally.  There would be one exception
to these pre-bound values, and that's the storage of numbers.  Church numerals
would be auto-converted on the fly, and then cached into the global bind
table.

Semantically speaking, functions would be evaluated identically to the
\\(\lambda\\)-calculus.  Also, the interpreter would perform automated
currying internally.

    (\ a b :: b a) => (\ a :: (\ b :: b a))
    (\ a b :: b a) someval => (\ a :: (\ b :: b a)) someval => (\ b :: b someval)

Here's an example program in this small language, which I'd like to call
axio:

    // fibonacci generator
    // supporting functions
    (#bind succ (\ w y x :: y (w y x)))
    (#bind + (\ a b :: a succ b))
    (#bind phi (\ a b f :: f a b))
    (#bind sigma (\ x :: phi (x false) (+ (x true) (x false)))) 
    (#bind fib (\ n :: (n sigma (phi 0 1)) false))

    // fib
    (fib (fib 5))

    // exit
    (#halt)

This would calculate the 5th Fibonacci number, let's call it f_5, and then
would calculate the f_5th Fibonacci number.

There really isn't much purpose to this language, especially given the 
complete lack of I/O, other than it may be a neat challenge to implement,
and an excuse to write a state-machine interpreter.

Ah well, that's axio.

Thanks for reading!
