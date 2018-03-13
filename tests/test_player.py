from .context_player import Player
from .context_tile import Tile
import unittest


class TestPlayer(unittest.TestCase):
    def test_player_str(self):
        player = Player('Alice')
        self.assertEqual(str(player), 'Alice')

    def test_draw(self):
        tile = Tile(x=0, y=5)
        player = Player('Alice')
        player.draw(tile)
        self.assertEqual(player.hand[-1], tile)

    def test_no_play(self):
        tile = Tile(x=0, y=5)
        player = Player('Alice')
        player.draw(tile)
        movement = player.play(2, 3)
        self.assertFalse(movement)

    def test_play(self):
        tile = Tile(x=0, y=5)
        player = Player('Alice')
        player.draw(tile)
        self.assertEqual(len(player.hand), 1)
        movement = player.play(0, 4)
        self.assertEqual(movement, tile)
        self.assertEqual(len(player.hand), 0)
