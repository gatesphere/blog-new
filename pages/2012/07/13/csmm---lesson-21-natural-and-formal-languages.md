---
title: ! 'CSMM - Lesson 2.1: Natural and Formal Languages'
date: 2012-07-13
tags: [csmm, languages, set theory]

An introduction
---------------
Hello all, and welcome to chapter 2 of CSMM.  This chapter is a short one, discussing
the various linguistic concepts as they relate to computer science.  First up is
a discussion of natural languages, and how they differ from formal languages, which
are what computer scientists think of when discussing languages.  Let's get to it!

Natural language
----------------
So, what is natural language?  To be quite blunt, a natural language is a language
spoken by humans, such as English, Spanish, German, etc.  Natural languages allow
us to express ourselves and communicate information to others who listen.  And they
have a lot going for them--they've worked for many thousands of years and they will
continue to work until we evolve past vocal communication.  But, for all their perks,
natural languages have some faults which make them unsuitable for discussing in a
computational sense.

Formal language
---------------
To move into the realm of discussing languages as a computer scientist, we need a
formalism of some sort.  A so-called formal language is just that formalism.

A formal language is defined as some set of words derived over an alphabet.  But
the terms "word" and "alphabet" probably have a different meaning than you're thinking.
The alphabet is a set of symbols which can be combined into words, and words are
a combination of zero or more symbols from the alphabet.  This makes sense, right?
Well, yes, except that if you were to map English, say, onto a formal language,
the alphabet would consist of every English word, and the words would consist of
every possible English sentence.  That is, the concept of a "sentence" in a natural
language is roughly equivalent to the concept of a "word" in a formal language, as
is "words" to "alphabet".

Business casual
---------------
In general, a language \\(L\\) is defined as a subset of the list of all possible 
words \\(\Sigma\\)\* over the alphabet \\(\Sigma\\).  In set theory terms, \\(\Sigma\\)\*
is the Kleene closure over \\(\Sigma\\), meaning that \\(\Sigma\\)\* contains *every*
possible combination of symbols from \\(\Sigma\\), including the null or empty word, 
usually denoted \\(\varnothing\\).

So the following language is perfectly valid:

$$L = \\{a, b, ab, aab, abb, aa, bb\\}$$
$$\Sigma = \\{a, b\\}$$

Using the same alphabet \\(\Sigma\\), so is this one:

$$L = \\{a, aa, aaa, aaaa, aaaaa\\}$$

As long as \\(L \subset \Sigma\\)*, \\(L\\) is a valid formal language.  However,
note that \\(\Sigma\\)\* is an infinite set so long as \\(\Sigma\\) has at least
one symbol.  There are infinite combinations of even a single symbol.  This means
that by definition, \\(L\\) may be an infinite subset of \\(\Sigma\\)\*, meaning 
\\(L\\) is an *infinite* language.  Surely writing out the entirety of \\(L\\) in
this situation is unfeasable.  Instead, we can define a number of rules that *define
legal words within \\(L\\)*.  

Keep it simple
--------------
Here's an example of an infinite language \\(L\\) defined over the alphabet 
\\(\Sigma = \\{a,b\\}\\):

  1. A word is in \\(L\\) if it begins with exactly one \\(a\\).
  2. A word which ends in any number of \\(b\\) symbols is in \\(L\\) *only if* it
     begins with another valid word in \\(L\\).
     
Following this, we see that the first few words we can define in \\(L\\) are:

$$L = \\{a, ab, abb, abbb, abbbb, \ldots\\}$$

We can see that this language is infinite, but we have a clear, complete discription
of \\(L\\) without performing a miracle and writing out the infinite set.  More 
often than not, as a computer scientist, you'll be interested in infinite languages,
and you'll be describing them in terms of a list of rules.

Wrapping up
-----------
Well, that was a short, sweet introduction to the world of formal languages.  Next
lesson, we'll see the concept of a grammar arise, giving us a formal way of writing
a set of rules upon which a formal language can be derived.  But until then, don't
forget your [homework](https://github.com/gatesphere/blog-resources/raw/master/downloads/csmm/lesson2-1.pdf)!