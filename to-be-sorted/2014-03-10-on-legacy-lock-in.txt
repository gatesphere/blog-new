---
date: 10/03/2014
tags: networking, rfc, email, legacy, lock-in, sctp, protocols, folly
title: On Legacy Lock-in

The internet is grand achievement in human history -- I refuse to budge on this point.  It has enabled the entire world to connect, share information, circumvent censorship, and spread creativity and research in a completely unprecidented manner.  And for the most part, it works great... just try not to fall down the rabbit hole and think too hard about what problems the future holds...

I was reading earlier today about how you do not want to use a regular expression to validate email addresses ([seriously](http://www.ex-parrot.com/pdw/Mail-RFC822-Address.html)), when it was mentioned that comments are legal in email addresses, [per RFC 822](http://www.ietf.org/rfc/rfc0822.txt?number=822).  That little tidbit points to a time when engineers were working hard to open as much space as possible for the future.  The addition of comments to email addresses was most likely a 'eh, why not?' kind of deal, but it shows the vast amount of flexibility these early RFCs baked in, 'just in case'.

Perhaps one of the largest 'problems' facing the global internet today is the exhaustion of the IPv4 address space.  We have a fix, it's been in place for ages... we just need the adoption.  But due to legacy applications, lack of foresight, and refusal to move onto something new when the old still 'works', IPv6 has instead been languishing, while countless workarounds and patches and switches have been installed to deal with the IPv4 space rather than time spent transitioning to IPv6.  The engineers opened up 32 bits of space to play in thinking it would be far more than ever needed, but here we are today...  No complaints to the early engineers -- computers and their corresponding technologies have always astounded people.

[SCTP](http://en.wikipedia.org/wiki/Stream_Control_Transmission_Protocol) is the little transport layer protocol you (likely) have never heard of.  Believe it or not, it as just as much of a standard as TCP and UDP, and actually combines the best of both of these protocols while avoiding some of their downfalls.  But it is another casualty of legacy lock-in.  This isn't to say that TCP and UDP should be abandoned -- they should not.  But SCTP has shown benefits in many applications, but developers are all but disallowed from using it due to lack of hardware support in most consumer routers and switches.

[SPDY](http://en.wikipedia.org/wiki/SPDY), on the other hand, is actually being built and working... but this is completely software-bound.  Software always moves faster than hardware, at least in established fields.  We're still trying to figure out the best way to use FPGAs, but that's another story...

We've experienced tremendous growth in the global internet thus far.  I fear its future may be stifled if we can't come together and move towards the new.  The old ways don't need to be abandoned, but they do need to stop being shackles...

Oh well.  We'll see where it all goes.

Thanks for reading.
