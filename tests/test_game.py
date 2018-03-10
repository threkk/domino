from .context import Game
import unittest


class TestGame(unittest.TestCase):
    def setUp(self):
        self.players = ['Alice', 'Bob', 'Charlie']
        self.game = Game(self.players)

    def test_createGame(self):
        # There are 3 players.
        self.assertEqual(len(self.game.players), 3)
        # The game is empty.
        self.assertEqual(len(self.game.game), 0)
        # There are 28 unique tiles.
        self.assertEqual(len(self.game.tiles), 28)
        self.assertEqual(len(self.game.tiles), len(list(set(self.game.tiles))))

    @unittest.skip('TODO')
    def test_is_finish(self):
        pass

    def test_next_player(self):
        self.assertEqual(self.game.next_player(), self.players[0])
        self.assertEqual(self.game.next_player(), self.players[1])
        self.assertEqual(self.game.next_player(), self.players[2])
        self.assertEqual(self.game.next_player(), self.players[0])
        self.assertEqual(self.game.next_player(), self.players[1])
        self.assertEqual(self.game.next_player(), self.players[2])

    def test_draw(self):
        original_len = len(self.game.tiles)
        self.game.draw()
        new_len = len(self.game.tiles)

        self.assertEqual(original_len, new_len + 1)


if __name__ == '__main__':
    unittest.main()
