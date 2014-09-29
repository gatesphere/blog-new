---
date: 25/02/2014
tags: elo, rating, multiplayer
title: WhiteWhale - A multiplayer Elo rating system

Last week I was poking around some with the Elo rating system, attempting to make it work for multiplayer, ranked games, where rank means a player has, at the end of the game, a numerical rank, such as first, second, third, etc.  Here's what I came up with.  Note, it diverges from Elo in several points.

Let \\(E_x\\) be the Expected score of player \\(x\\), \\(N\\) be the number of participants, \\(T_x\\) be the numerical rank of player \\(x\\), \\(S_x\\) be the actual score of player \\(x\\), \\(R_x\\) be the rating of player \\(x\\), where \\(100\\) is a decent average, \\(R'_x\\) be the new rating of player \\(x\\), \\(\sigma\\) be the average rating of all the players of a given game, \\(K_x\\) be the \\(K\\)-value for player \\(x\\), and \\(P_x\\) be the number of rated games that player \\(x\\) has played.

First, we find the expected score for each player:

$$Q_x = (\sigma - R_x) / 20$$
$$E_x = \frac{1}{1 + 10**{Q_x}}$$

(Where \\(**\\) is exponentiation.  Superscripts are not possible here due to a conflict between markdown and mathjax...)

Then we determine the actual score for each player:

$$S_x = \frac{N - T_x}{N - 1}$$

Next we determine the \\(K\\) value for the player:

$$K_x = \frac{50}{P_x}$$

Finally, we use this to determine the new rating of the player:

$$R'_x = R_x + K_x (S_x - E_x)$$

Now, what to do in case of ties?  Simple -- all tied partcipants are dropped down to a single rank.  So, in a 10-player game (i.e., \\(N = 10\\)), if 4 people tied for third place, they all have a \\(T_x\\) of \\(6\\).

This system is automatically scaled so new players have more volatile ratings than established players, so that their scores level out and reflect their true skill eventually.  However, once a player is past 50 games, it is difficult if not impossible to significantly change their rating, so perhaps this needs to be reworked.

It's not perfect, but it was fun to come up with :)

Thanks for reading.