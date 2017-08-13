# gofish
My first Python project, the classic card game Go Fish.


Bugs -- To Fix

When player is at end of game, and draws last card in deck, (and the card matches cards player has), game says "your turn again" when really it's the end of the game at that point, because the end of game condition isn't evaluated yet.

When player is dealt a 4-of-a-kind, it isn't evaluated until after the player asks about a card. (Low priority because low odds that the player will be dealt a 4-of-a-kind when they only get dealt 5 cards.)


Bugs -- Fixed

[Fixed 8/11/17]
When player runs out of cards, it doesn't automatically draw a card
--> Fixed

[Fixed 8/11/17]
When Turn() returns 1 to signal deck out of cards, it actually returns 0 (None). Only after another Turn() call does it actually return 1.
Reason:
- In recursion, it's returning to the most recent call of Turn() and not the original caller.
- See: https://stackoverflow.com/questions/11356168/return-in-recursive-function
- I fixed it by making my recursion say "return Turn()" rather than simply "Turn()"

[Fixed 8/11/17]
When one player runs out of cards, crashes
--> Fixed: Had player.hand.add_card instead of player.add_card

[Fixed]
When draw a card, it doesn't check for 4-of-a-kind condition
--> Fixed by calling player.isfour()
--> Fix tested and passed

[Fixed]
When the other player has multiple matches, the print other_player.hand[i] crashes "list index out of range"
Detailed case:
P2 asked for an Ace
P1 had eleven cards
P1 had Ace in the 4 and 10 indices (5th and 11th cards)
[-->] I know why! When you remove the first card, all the indices shift, so when you look for the 2nd ace in the 10 index position, that ace is actually in the 9 index position. The error "list index out of range" occurs because the list is too short.
You had this same problem on the 4-of-a-kind function too! You need to mark the cards for deletion somehow and then delete -- or traverse the list backward.
--> Fixed by using reversed(list) to traverse the list in reverse order
--> Fix tested and passed

Features

Sort cards in order of rank on each turn
maybe with consistent ordering of suits

Allow player input to be case-insensitive, and/or to be numerical

Allow gameplay by more than 2 players

Create an "AI" to play the game against the human opponent

Turn the file into an executable (see: https://stackoverflow.com/questions/1957054/is-it-possible-to-compile-a-program-written-in-python)

Clean up debug code
