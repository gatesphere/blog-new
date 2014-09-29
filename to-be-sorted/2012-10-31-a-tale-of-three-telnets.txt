--- 
tags: telnet, negotiation, protocol
date: 31/10/2012
title: A tale of three telnets

Recently I've been building a telnet-compliant server in Io.  Well, 
pseudo-compliant, but that's another story.  But, in doing so, I've
had to overcome how three different popular telnet clients interpret
the standards, and had to work around these issues, especially with
respect to negotiation.

A primer on negotiation
-----------------------
Negotiation is the method that telnet clients and servers use to express
how they are going to behave to each other.  It consists of sending 
sequences of bytes back and forth, leading to an understanding between
the client and server.  In the traditional implementations, the server 
almost always initiated negotiation with the client, rather than 
vice-versa.

Well, at least in theory, that's how things should operate.  But in
the three common clients that I'm using to test, this is not the case.

`telnet` from GNU inetutils
-------------------------
This is the standard telnet client for unix-like operating systems, such
as Linux.  

This client likes to initiate negotiation, firing a stream off to the 
server as soon as it connects.  It will handle either \n or \n\r as
a newline character.  It also listens to renegotiations (i.e., asking
it to turn off it's local character echoing for entering a password,
and then turning it back on).

PuTTY
-----
PuTTY is a common and widely used ssh, telnet, and serial terminal client
for multiple platforms.  I prefer it over any of the others I've used,
but that's probably because I use it every day for hours at a time for
my job.

Much like the GNU `telnet` package, PuTTY likes to initiate negotiation
upon connection, though it sends fewer commands over the wire than
`telnet` does right off the bat.  However, it needs a \n\r for a newline
character.  It also handles renegotiations gracefully.

Windows `telnet`
----------------
This one is the ugly duckling of the group.  Included by default with
Windows, this one acts the strangest of the group.

This client does not initiate negotiation at all.  It needs a \n\r for 
the newline character.  It does *not* handle renegotiations at all.

Well, it actually does handle the negotiation itself, but it doesn't
listen to them.  The moment it recieves a negotiation stream, it shuts
off local character echoing permanently.  It will not re-enable it,
even though it replies that it will.

Just some observations.  Thought I'd share.
