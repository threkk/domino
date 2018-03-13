from domino.tile import is_compatible


class Player(object):
    """
    Models a player who will take part in the game. The player has a hand
    holding tiles and can draw cards or play them.
    """
    def __init__(self, name):
        """
        Constructor

        :param name: Name to display for the player.
        """
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def draw(self, tile):
        """
        Adds a tile to the player's hand

        :param tile: Tile to be added to the hand.
        """
        self.hand.append(tile)

    def play(self, head, tail):
        """
        The player reads the top and bottom numbers of the current game board
        and plays a tile of his hand if any of them matches.

        :param head: Number of the top part of the top tile.
        :param tail: Number of the bottom part of the bottom tile.
        :return: The tile played. If not tile is played, False.
        """
        for tile in self.hand:
            if is_compatible(head, tile) or is_compatible(tail, tile):
                self.hand.remove(tile)
                return tile
        return False
