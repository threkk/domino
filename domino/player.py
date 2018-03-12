from domino.tile import is_compatible


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def draw(self, tile):
        self.hand.append(tile)

    def play(self, top, tail):
        for tile in self.hand:
            if is_compatible(top, tile) or is_compatible(tail, tile):
                self.hand.remove(tile)
                return tile
        return False
