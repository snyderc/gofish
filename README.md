# Go Fish

The classic card game about getting 4-of-a-kinds. For two players sitting at the same computer.

## Installing

This program runs on the command line and is compatible with Python 2.7. Run "python2 card.py" to start the game.

## Known Bugs

- When player is at end of game, and draws last card in deck, (and the card matches cards player has), game says "your turn again" when really it's the end of the game at that point, because the end of game condition isn't evaluated yet.
- When player is dealt a 4-of-a-kind, it isn't evaluated until after the player asks about a card. (Low priority because low odds that the player will be dealt a 4-of-a-kind when they only get dealt 5 cards.)

## Future Potential Features
- Sort cards in order of rank on each turn, maybe with consistent ordering of suits
- Allow player input to be case-insensitive, and/or to be numerical
- Allow gameplay by more than 2 players
- Create an "AI" to play the game against the human opponent
- Turn the file into an executable (see: https://stackoverflow.com/questions/1957054/is-it-possible-to-compile-a-program-written-in-python)
- Clean up debug code

## Author

Chris Snyder

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.