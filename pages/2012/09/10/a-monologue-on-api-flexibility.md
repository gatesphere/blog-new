--- 
date: 2012-09-10
title: A Monologue on API Flexibility
tags: [java, blackberry, api, ruby, verbosity, complexity, expression, language]

Hello everyone.

It's been a while since I've written here.  Sorry about that.  I've been working,
and getting accustomed to my new responsibilities.

Don't worry about CSMM, more lessons are forthcoming!  I really want to finish 
that course material.  I'm really excited about it.

But today, I want to write about a topic that has recently become a focal point
for me.  I'd like to discuss API design a bit.

This is a topic that has been beaten to death.  "Design simple APIs".  But, 
it's not that easy, apparently.

This past week I've been working with both Ruby on Rails, and the BlackBerry
Java Development Environment.  And let me tell you... one of those two is a
joy to work with.

Here's an example from Ruby on Rails which exemplifies the qualities of an
easy-to-use API that I'm looking for:

    1.day.from_now.in_time_zone('Eastern Time (US & Canada)')
    
One line, and it tells you EXACTLY what it does.  Not only that, but the
API is simple, succinct, and elegant.  Compare that to the corresponding
Java:

    Calendar c = Calendar.getInstance(TimeZone.getTimeZone("EST"));
    c.setTime(new Date());
    c.add(Calendar.DATE, 1);
    
Atrocious.  But this highlights my main bone of contention between these
APIs.  Atomically, they're both *simple*.  The difference is that the RoR
API was built for *molecular simplicity*.  

When you put simple parts together in RoR, or in Ruby in general, you 
usually end up with something that is still pretty simple, reducing the 
cognitive load.  You build a simple molecule out of simple atoms.  Java,
on the other hand, suffers when making this leap.  As atomic parts of Java
calls are glued together, you get something that grows unweildy farily 
quickly.

Now, do not get me wrong here.  I enjoy programming in Java.  It is not my
favorite language by far, but it is nice.  And I also know that I am unfairly
comparing two different languages here, each with their own idioms that
support their unique uses.  But the problem remains... and is being added
to by professional APIs that are over-engineered and over-verbalized.

To prove my point further, here's an example from the BlackBerry Java API docs,
on how to scan a QR code:

    Hashtable hints = new Hashtable();
    Vector formats  = new Vector();
    formats.addElement(BarcodeFormat.QR_CODE);
    hints.put(DecodeHintType.POSSIBLE_FORMATS, formats);
    BarcodeDecoder decoder = new BarcodeDecoder(hints);

That's the setup code for initializing the decoder to read a QR code.  5 lines.

Now, this makes a lot of sense if you want to scan multiple different types,
or provide several different hints to the decoder, but let's look at what's
going on here if you want to scan just QR codes:

  1. Create an empty `Hashtable`
  2. Create an empty `Vector`
  3. Populate the `Vector` with a single entry
  4. Put that `Vector` into the `Hashtable` as it's only entry
  5. Hand that `Hashtable` to the `BarcodeDecoder`'s constructor
  
So, we've created two junk objects just to pass a single parameter to the
decoder.  This is unacceptible, in my opinion.  While allowing flexibility
is good, allowing clean, succinct code should also be a priority.  No one
will like using your API if it's simple to make misakes, just because you
decided that you want your api to allow people to shoot off their own leg.

I suppose my argument here is, if you design an API, the users will have
to bend to your will.  Make their life pleasant.  Design clean interfaces.
And don't be afraid to limit their flexibility in order to make their life
simpler.  Developers are an interesting bunch, but I don't know many who
prefer to write five lines for something that should be done in 1.  We are
lazy, and proud of it.  Allow us to work efficiently, and your API will 
prosper.