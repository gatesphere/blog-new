---
title: steg.io, A brief example of steganography
date: 2012-03-20
tags: [code-dump]

Hello all,

Thought I'd give you a short introduction to the process of hiding data in plain sight, also called steganography.

First, a bit of theory. The script I'm going to introduce here hides data in a 24-bit uncompressed bitmap image. That sounds awfully specific, but don't worry... it's the most common type of bitmap. The reasons I went with this format are as follows:

  - Simple header and data format.
  - Enough wiggle room to store a relatively large amount of data.

So, let's get started. In a 24-bit uncompressed bitmap image, there are two headers (back to back, for a total of 54 bytes). Within these headers are data containing the resolution of the image, the image's filesize in bytes, etc. We're interested in the resolution, but we'll see why later.

After the header is the image data, 24 bits (3 bytes) per pixel. The data is stored in the RGB format, and it's stored in the order blue (1 byte), green (1 byte), and red (1 byte). With a full byte for each color, this allows for extremely subtle, hard to visually detect, variations in shade.

So, since the human eye is not as good as we'd like to think, this actually gives us some wiggle room in terms of how to store data. It turns out that the human eye is far more sensitive to green than red or blue, and in any case, manipulating the least significant bits of this data is almost inperceptible. The idea here, is to turn a 24 bit image into a 16 bit image, giving us 8 bits to store data.

Using the following scheme, we are able to fit a full byte of data per pixel in the image file! If we take the 3 LSB of blue, 2 LSB of green, and 3 LSB of red, we have 8 bits. So now it's simply a matter of bitshifting.

Of course, it's not that simple, but it's close. If we were simply shoving 1 byte per pixel, when decoding, how would we know where to stop? So we need to hide another header, within the data. I propose a 4 byte (therefore 4 pixel) header, which is simply a 32-bit integer signifying how many bytes long the hidden data is. This is stored least significant byte first, to mirror the way that the bitmap format handles data. After this, we have the rest of the file to hide data. When decoding, we read the first 4 hidden bytes, and use that to determine how much further to read. This means that we have (height * width) - 4 bytes of storage within any particular image file.

That's about it, for now. If you'd like to check this out, please go see my example (in Io) on github: [io-codejams](https://github.com/gatesphere/io-codejams/tree/master/2012/03/20120310_bmp_steganography).

Keep tweaking~ 