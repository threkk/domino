from domino.tile import make_tile
from domino.logger import start_game
from domino.logger import board_state
from domino.logger import player_cant_play
from domino.logger import player_plays_connect
from domino.logger import win_message
from domino.logger import player_skips_turn
from random import shuffle
from functools import reduce


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
        self.winner = None
        self.tie = {str(player): False for player in self.players}

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
        if reduce(lambda v, values: v and values, self.tie.values(), True):
            self.winner = 'It is a tie. None'
            return True

        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return True
        return False

    def next_player(self):
        """
        Gets the next player to play in the game.
        """
        return next(self.player_generator)

    def pop_top(self):
        """
        Gets the top tile of the pile. If there are no tiles, it returns None.
        """
        if not self.tiles:
            return None
        return self.tiles.pop()

    def place_tile(self, tile):
        if not tile:
            return False

        first_tile = self.game[0]
        first_number = first_tile.x
        last_tile = self.game[-1]
        last_number = last_tile.y
        x, y = tile

        # ...:last_number><x:y>
        if x == last_number:
            self.game.append(make_tile(x, y))
            return last_tile
        # <y:x><first_number:...
        elif x == first_number:
            self.game.insert(0, make_tile(y, x))
            return first_tile
        # <x:y><first_number:...
        elif y == first_number:
            self.game.insert(0, make_tile(x, y))
            return last_tile
        elif y == last_number:
            self.game.append(make_tile(y, x))
            return first_tile
        else:
            return False

    # Fix case no more tiles.

    def run(self):
        first_tile = self.tiles.pop()
        self.game.append(first_tile)
        start_game(first_tile)

        while not self.is_finish():
            player = self.next_player()
            top = self.game[0]
            tail = self.game[-1]

            movement = player.play(top.x, tail.y)
            connector = self.place_tile(movement)
            while not connector:
                new_tile = self.pop_top()
                if not new_tile:
                    player_skips_turn(player)
                    self.tie[str(player)] = True
                    break
                player.draw(new_tile)

                player_cant_play(player, new_tile)

                movement = player.play(top.x, tail.y)
                connector = self.place_tile(movement)
                self.tie[str(player)] = False

            if movement and connector:
                player_plays_connect(player, movement, connector)
                board_state(self.game)

        win_message(self.winner)
