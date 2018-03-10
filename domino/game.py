from domino.tile import make_tile
from random import shuffle


def infinite_generator(elements):
    while True:
        for element in elements:
            yield element


class Game:
    def __init__(self, players):
        assert len(players) > 0
        self.players = players
        self.player_generator = infinite_generator(players)
        self.game = []
        self.tiles = []
        for i in range(0, 7):
            for j in range(0, i + 1):
                tile = make_tile(i, j)
                self.tiles.append(tile)
        shuffle(self.tiles)

    def is_finish(self):
        """
        Evaluates the game state. The game finishes when a player wins. A
        player wins when he has 0 tiles.
        """
        for player in self.players:
            if len(player.tiles) == 0:
                return player
        return False

    def next_player(self):
        """
        Gets the next player to play in the game.
        """
        return next(self.player_generator)

    def draw(self):
        return self.tiles.pop()

    def place_tile(self, tile):
        last_tile = self.game[-1]
        last_number = last_tile.y
        x, y = tile

        if x == last_number:
            self.game.append(make_tile(x, y))
            return True
        elif y == last_number:
            self.game.append(make_tile(y, x))
            return True
        else:
            return False

    def run(self):
        first_tile = self.tiles.pop()
        self.game.append(first_tile)

        while not self.is_finish():
            player = self.next_player()
            current_move = self.game[-1]
            player.draw(self.draw())
            while not self.place_tile(player.play(current_move)):
                player.draw(self.draw())
