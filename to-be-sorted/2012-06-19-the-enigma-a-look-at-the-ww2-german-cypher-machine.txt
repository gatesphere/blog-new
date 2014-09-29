---
title: The Enigma, a look at the WW2 German cypher machine
date: 19/06/2012
tags: enigma, ww2, german, cypher, cryptology, code-dump, github

As of late, my fascinations have been turned toward the physical machines used
to encrypt messages in wartime, particularly during World War II.  Chief among
such machines lies [The Enigma](http://en.wikipedia.org/wiki/Enigma_machine).  
The Enigma has a sort of air of legend surrounding it, at least among cryptologists,
mathematicians, computer scientists with a hankering for history, and WW2 intelligence
buffs.  But how did it actually work?  This article will attempt to explain, an
an easy to understand manner, how the Enigma managed to encode it's messages, and
at the end, I will provide a link to a program I wrote yesterday simulating the 
workings of an Enigma-style machine.

Before we get started, it's worth noting that whenever I refer to "The Enigma" as
a singular, I'm referring to any of a class of cypher machines that went by the name
Enigma.  There were several different models of Enigma machines produced for different
branches of the German military, each with subtle differences, but they all operate
on the same basic principles which I lay out below.

So, hopefully, most of us have created simple cyphers as kids.  You know the kind,
you write down a little key somewhere (1=A, 2=B, etc.) and then use your key to encode
a message.  Then you send your message and key to a friend and they decode it.  Simple,
insecure, but fun.  Believe it or not, this is the same principle that the Enigma
machine uses, but evolved a bit to make it *much* more secure.

The scenario above describes what's known as a substitution cypher, where one symbol
in the coded message maps to one character in the decoded message, and the mappings
between symbols and characters never change.  In essence, you're substituting one
alphabet for another, and so long as your friend knows how to determine your mapping,
your friend can read your message.  Simple as pie.  Below is a key and an encoding of
a message in such a system:

    key         original message        encoded message
    ----        ----------------        -------------------------
     1=A        HELLO WORLD             8-5-12-12-15 23-15-18-12-4
     2=B
     3=C
     4=D
     5=E
     6=F
     7=G
     8=H
     9=I
    10=J
    11=K
    12=L
    13=M
    14=N
    15=O
    16=P
    17=Q
    18=R
    19=S
    20=T
    21=U
    22=V
    23=W
    24=X
    25=Y
    26=Z

This code is pretty simple to break, and not just because the mapping is 1=A, 2=B,
etc., but because for example, every L is encoded to 12.  If someone figured out 
just that one bit, they'd be able to see 3 letters of the above message, and with
a bit of finagling, they could probably work out the rest.  Simple substitution 
cyphers are fragile and insecure.

Now suppose you wanted to increase the security of your substitution cypher a bit.
One thing you could do is make your cypher *rotate*, or have a new mapping apply
for *each* character in the source text.  One way you could do this is by shifting
the encoding alphabet one position forward each time you encode a character.  For 
example, starting with the key above, we would encode the `H` as `8`, like we expect,
but then we shift the indexes up one position, so that `2=A`, `3=B`, `...`, `26=Y`, `1=Z`.
Now when we encode the `E`, we encode it as `6` instead of `5`.  The whole message,
encoded with a rotating substitution cypher is now:

    original message     encoded message
    ----------------     --------------------------
    HELLO WORLD          8-6-14-15-19 2-21-25-20-13
    
Here, we see that this cypher is much more secure, as every L is encoded as a
different symbol, first `14`, then `15`, and finally `20`.  In fact, you'd have
to go 25 characters between L's to have them encode to the same symbol.  This kind
of cypher is harder to crack, because you've now shifted it from a single substitution
to a polyaphabetic substitution, meaning that you've used multiple, unique alphabets
to encode a single message.

The Enigma machine operates on this rotating substitution cypher principle, but adds
several layers of obfuscation to the mix just for added security.  One of these layers
is having *multiple* rotating cyphers that a single message is sent through.  The enigma
machine accomplished this with a series of interchangable rotors, each of which implemented
a very complex mapping of wires internally, with markings on the outer rings to inform
the operator of the number and orientation of the rotor.

The most widely used Enigma machines came with 5 rotors, of which 3 were used at a time in series, 
in any combination.  The rotors themselves were marked with a roman numeral, identifying 
them as either I, II, III, IV, or V.  The Enigma came with one each of these, and they 
are unique with respect to one another, but every I rotor is identical, as is every II, 
every III, and so on.  These rotors were also marked on the outside with a ring of the
letters of the alphabets, which were used as an index when the operator was setting up
the machine.  In this way, an operator could write down a key extremely simply and concisely
as follows: I-IV-II K-C-S means left-to-right ordering of the rotors is I, IV, and then
II, and they are indexed at K, C, and S, respectively.  In this way, the key could be
transmitted to the decoder.

To the far left of the rotors is a part known as the reflector, which is hard-wired
in identical fashion on every machine of the same model.  The reflector's purpose is
two-fold: first, it re-encodes the character through the three rotors a second time
by a different pathway, making for 6 total transformations (three in, reflect, three out),
and second, it allowed a message to be decoded by setting up the machine identically
to the way it was set up when the message was encoded.

So, to encode a message, the operator selects three rotors and their positions,
places them in the machine, and types the message, one character at a time.  As he
types each character, a light is lit, indicating the encoded character.  This character
is written down, becoming the encoded message as the last character is encoded.  Simple
operation, but what's happening inside the machine to make this secure?

When the operator presses a key, an electrical signal is sent through a wire in the 
right-most rotor, which is wired so that another wire in the middle rotor is powered,
which is wired to another wire in the left-most rotor.  Upon leaving the left-most rotor,
the reflector re-routes the signal to another path in the left-most rotor, which
powers another path in the middle rotor, which powers another path in the right-most
rotor, which finally powers a tiny lamp.  This is nice, but there's a step missing
here, and it's vital.  Before any of the electrical pathways are formed, the right-most
rotor is rotated forward one position, just like in the rotating cypher earlier.  And,
if the first rotor has advanced enough, the second rotor is turned as well.  And
if the second rotor has advanced enough, the third rotor is also turned.  All this
variation makes the rotating cypher *many orders of magnitude stronger* than a
simple rotating cypher.  This is where the Enigma's strength lies. The following 
diagram hopefully explains this
better (from Wikipedia, original [here](http://en.wikipedia.org/wiki/File:Enigma-action.svg))

![Enigma action](http://upload.wikimedia.org/wikipedia/commons/6/6c/Enigma-action.svg)

Here, we see an A being encoded to a G, and then, the next key press, the A is encoded
to a C instead.  Note also that the pathways work just as well backwards as forwards thanks
to the reflector, such that encoding GC with the initial setup will result in AA--the original
text!

Now, the Enigma is *already* an extremely strong machine with this form of operation,
but just to throw a wrench into the works, there was another component of the machine
designed to scramble the letters before and after encoding, called the plugboard.
The plugboard was filled with as many as 13, but usually 10, pairs of plug cables,
which paired two letters together.  These letters were switched both before going
into the first rotor, and after coming out of the first rotor before switching on
the light.  The following diagram shows an example encoding with the plugboard
populated (from Wikipedia, original [here](http://en.wikipedia.org/wiki/File:Enigma_wiring_kleur.svg))

![Enigma with plugboard](http://upload.wikimedia.org/wikipedia/commons/5/53/Enigma_wiring_kleur.svg)

Following along with the numbers, we can trace the electrical signal from (1) the 
battery, to (2) the depressed switch of the A key, to (3) the plugboard (notice how
there is no plug in A, so it is not transformed), to (4,5,6) the rotor/reflector
assembly (went in as A, came out as S), to (7) the plugboard again, to (8) the plug
cord (S was matched with D, so S becomes D), finally to (9) the light for D.

All of this complexity, and the Enigma machine was still cracked thanks to some serious
efforts put forward by the mathematicians at Bletchley Park and also independent
Polish researchers.  It turns out that there are still two flaws with the Enigma,
but only one of them is inherent with in the design.  Firstly, due to the reflector,
no symbol will *ever* be encoded to itself.  If there's an X in some position in the
cyphertext, you know it cannot possibly be an X in the cleartext.  Secondly, user
error, compounded with the stresses of war and captured equipment, helped the Allies
crack the code.  Turns out that for all the obfuscation the plugboard was included
to add, the Germans didn't use it correctly, causing patterns to arise in encoded
messages.  It is estimated that if the plugboard was used correctly, the Enigma
codes would have been uncrackable.  But, hey, who's to say for certain?

Anyways, I'll leave you with a bit of code.  I hope you've enjoyed this post,
as I had a lot of fun writing it, and it's an incredibly fascinating topic to me.

My Enigma machine simulator in Io is available on github.  Get it [here](https://github.com/gatesphere/io-codejams/blob/master/2012/06/20120618_enigma/enigma.io).
It's not a 100% accurate simulation, and a lot of it is guesswork.  Most notably
missing is the double-step feature of the Enigma.  But it was fun to write.

Thanks for reading!
