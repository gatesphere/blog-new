---
title: Reverse-engineering a simple software licensing scheme
date: 2011-09-20

Hello all,

This post should have the subtitle "or, DON'T DO THIS". So, today I was curious about what makes independently developed commercial software licensing work. My target software shall remain unnamed (I'll call it X here), but lets say that it is a drawing tool of some sort, and programmed in Java. Java is relatively easy to decompile, with the right tools, providing next to no security if your validation scheme is embedded in the code itself. But how else is one to check licensing keys? I'll move on to that one later. First, onto the goods.

So, X comes in two versions: free and paid. The free version is more than most people will ever need or use, but the paid version offers some nice functionality. The free version and the paid version are the same executable, simply feature-locked without a valid license key. Hmm...

Decompiling the code was easy. Finding the validation section was even easier (it was clearly labled "VALIDATE CODE"). Finding this section of the code revealed all I needed to know about the license key to craft one myself that would give me a perpetual license to the paid version.

Here's what I found in X's validation section:

The license key must be exactly 16 characters.

All characters in the license key must be numbers.

The sum of the first twelve characters modulo 10 must exactly equal the 14th digit (first checksum).

The sum of the first twelve characters and the first checksum must equal exactly the two digit number formed by the 15th digit\*10 + the 16th digit (second checksum).

There is a license expiration date encoded into the above characters, formed by the value of the 3rd digit\*1000 + 5th digit\*100 + 8th digit\*10 + 13th digit.

This expiration date is a 4 digit number that corresponds to a certain number of days from January 1st, 2000.

If this expiration date manages to add up to a number between 7581 inclusive and 7694 inclusive, a perpetual license is granted.

With this in mind, I worked with pencil and paper to generate the following code:

0070600403000020

As you see, the value of X3\*1000 + X5\*100 + X8\*10 + X13 = 7640, a number chosen at random to fall in the perpetual license range. The value of X1 + ... + X12 = 20. 20 % 10 = 0, which equals X14, satisfying the first checksum. 20 + 0 = 20, which is X15\*10 + X16, satisfying the second checksum. So, in theory, this should work. And trying it in the software (which doesn't "phone home" except to pull updates) gives a successful update of license, and unlocks the paid version's features. Simple as pie.

But that's not all that reversing X's license did. X happens to be one of a family of software, also containing product Y. The validation code for Y's licenes is essentially the same thing, with the digit order scrambled around. So for Y, the following code grants perpetual paid access:

0070603400200000

You'll notice that the 7640 is embedded in the same location. The checksums have moved, such that X10 is the first checksum and X11*10 + X12 is the second checksum. The sum to compare these against is formed by X1 + ... + X8 + X13 + ... + X16. Like I said, just re-arranging numbers. This code was tested and verified to unlock Y perpetually.

Now, for the bad. THIS IS INCREDIBLY STUPID. Granted, most users won't have the knowhow to do this, but coding a simple verification scheme like this allows those with knowhow to generate licenses on demand with little more than pencil and paper, as well as distribute them to whomever they wish, reducing your profits and dilluting your efforts. Granted, for a software like X (and it's cousin Y), this is simple enough. The target demographic isn't usually the technically minded. X (and to a lesser extent, Y) is a very nicely presented software, and is almost bug free. The free version is way more than what one would expect for a crippled version of a shareware. But, this is still an issue if one is attempting to maintain a strong level of security in their licensing scheme.

What could have been done better? Well, for one, length doesn't typically matter, if you're simply using a checksum or two with embedded data like this. Once the algorithm is figured out, any number of keys can be generated regardless of length. So, short keys like the above are acceptable for this purpose.

Using all numeric characters is also fine, in as much as if your licensing scheme relies upon checksums and encoded data, numbers or not if it is cracked, keys can be generated. The same argument as above applies.

Not phoning home is the lynchpin of safe licensing. Each license should be generated and added to a master database, and checked upon entry for validity against the home server. Each license should also have a limited amount of legal activations before the license no longer unlocks a piece of software. But this is a minor point.

Essentially, the problem with licensed software is that there is nearly always a way to break it. If it is downloadable to the user's own computer, an intrepid cracker will find a way around the registration. If it is a web-service, someone will share a validated account. So, I suppose, the only way to win in software licensing and use-limiting, is to not play at all.

Just my two cents.

Keep tweaking~ 