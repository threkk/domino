from domino.tile import make_tile
from random import shuffle


class Game:
    def __init__(self, players):
        self.players = players
        self.game = []
        self.tiles = []
        for i in range(1, 7):
            for j in range(1, i + 1):
                tile = make_tile(i, j)
                self.tiles.append(tile)
        shuffle(self.tiles)

    def is_finish(self):
        for player in self.players:
            if len(player.tiles) == 0:
                return player
        return False

    def next_player(self):
        while True:
            for player in self.players:
                yield player

    def run(self):
        first_tile = self.tiles.pop()
        self.game.append(first_tile)

        while not self.is_finish():
            player = self.next_player()
            player.draw(self.tiles)
            player.play()
