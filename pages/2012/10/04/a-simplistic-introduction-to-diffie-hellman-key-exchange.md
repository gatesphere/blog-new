--- 
tags: [encryption, Diffie-Hellman, key, xor, shared secret, code-dump]
date: 2012-10-04
title: A Simplistic Introduction to Diffie-Hellman Key Exchange

So, recently, I've been getting into encryption.  In that vein, I thought
I'd give a quick overview of two topics: simple XOR encryption, and 
Diffie-Hellman key exchange.

XOR encryption
--------------
The first topic is almost mindnumbingly simple, but it is a simple, cheap,
easy to afford encryption algorithm which has several nice features: it's
symmetric, composable, and stupid fast.

So, for XOR encryption to work, you need two things: a payload (the 
'cleartext') and an encryption key.  The algorithm takes the key and uses
it to modify the payload, creating what is known as the 'cyphertext'.  
Both the key and payload are typically strings, but anything that can be 
converted to binary numbers will work.  To make things simple, I'm going 
to use numbers in my examples that follow, instead of strings, so as to 
avoid encoding concerns, which are really something that shouldn't be 
worried about when looking at encryption concepts, as they're more of an 
implementation detail.

Alright, so let's start off with an example.  Say that I want to encrypt
the payload '117' with the encryption key '18'.  These are arbitrary numbers
chosen for the purpose of this example.

First we start by converting these to binary numbers:

    payload = 117 = 0b01110101
    key     =  18 = 0b00010010
    
Then, to create the cypertext, we simply XOR the numbers together:

        01110101          117  cleartext
    XOR 00010010      XOR  18  key
    ------------      -------
        01100111          103  cyphertext
        
So we've successfully encrypted the payload to the cyphertext.  Decryption
is simply XORing the cyphertext with the same key.  This is why it's a 
so-called symmetric encryption scheme--encryption and decryption are the
exact same operation.

        
        01100111          103  cyphertext
    XOR 00010010      XOR  18  key
    ------------      -------
        01110101          117  cleartext
        
What does it mean then, that this algorithm is composable?  Well, what
would happen if I were to encrypt the data with one key, and then a
second, different key?  Would it matter which order I applied the decryption?
Composable encryption algorithms work regardless of the order of decryption.
That is, the following works:

      cleartext  117  01110101
           key1   18  00010010
    --------------------------
    cyphertext1  103  01100111
           key2  201  11001001
    --------------------------
    cyphertext2  174  10101110
    
    Decrypt order: key2, key1:
    cyphertext2  174  10101110
           key2  201  11001001
    --------------------------
     cleartext1  103  01100111
           key1   18  00010010
    --------------------------
      cleartext  117  01110101
      
    Decrypt order: key1, key2:
    cyphertext2  174  10101110
           key1   18  00010010
    --------------------------
     cleartext1  188  10111100
           key2  201  11001001
    --------------------------
      cleartext  117  01110101
      
Cool huh?

Key Exchange
------------
Now, how do two people get the same key?  Surely, one could just tell
the other, and trust that they'll keep it secret.  But someone could
be listening (the walls have ears, you know!).  This won't work.

What does work is something called Diffie-Hellman key exchange.  It involves
both participants agreeing on a "shared secret", which will become part
of the key, as well as each individually choosing a secret number that
they won't tell anyone, not even each other.  They then do some simple
XORing on these and swap.  Because XOR is composable, as explained
above, both participants will be able to generate the same secret key
without ever sharing it with the other, allowing them to communicate
freely.

How does this work though?  Here are the steps (don't worry, there's a 
textual flowchart of this later in the post):

  1. Both participants agree on a shared secret.  Let's use 34.
  2. Each participant independently chooses a secret key.  Let's use 12 
     and 21.
  3. Each participant XORs their secret key with the shared secret. 
     This gives us 46 and 55.
  4. The participants swap these composed keys.
  5. The participants XOR their private keys with the coposed keys that
     they just recieved.  This gives us 59 and 59.
  6. They've generated the same key! They can communicate.
  
Diagrammed out a bit, here's how it looks:

    Person 1          Person2
          34  shared  34
          12  secret  21
          46 composed 55
          55   swap   46
          59   key!   59
          
This does not completely prevent man-in-the-middle attacks, but it does
a good bit to make it harder for people to find the encryption key.

Do note, however, that this implementation is highly flawed: Person 1 can
glean Person 2's secret key, and vice versa, after the swap!  It's a simple
matter of XORing by the shared secret.  True key exchange mechanisms use
stronger encryption schemes that prevent simple means of ascertaining the
private keys of other people.


Some code
---------
As always with these posts, I try to provide some working code to explain
what my words can't convey.  Here's an example in Io:

<script src="https://gist.github.com/3835917.js"> </script>

Enjoy.
