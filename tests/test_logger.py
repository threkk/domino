import unittest
import unittest.mock
from io import StringIO
from .context_tile import Tile
from .context_player import Player
from .context_logger import start_game
from .context_logger import player_plays_connect
from .context_logger import player_skips_turn
from .context_logger import board_state
from .context_logger import player_cant_play
from .context_logger import win_message


class TestLogger(unittest.TestCase):
    # https://stackoverflow.com/a/34738440
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_start_game(self, mock_stdout):
        output = 'Game starting with first tile: <4:1>\n'
        start_game(Tile(x=4, y=1))
        self.assertEqual(mock_stdout.getvalue(), output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_player_plays_connect(self, mock_stdout):
        alice = Player('Alice')
        tile = Tile(x=0, y=4)
        board = Tile(x=4, y=1)
        output = 'Alice plays <0:4> to connect to tile <4:1> on the board\n'
        player_plays_connect(alice, tile, board)
        self.assertEqual(mock_stdout.getvalue(), output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_board_state(self, mock_stdout):
        tiles = [Tile(x=0, y=4), Tile(x=4, y=1)]
        output = 'Board is now: <0:4> <4:1>\n'
        board_state(tiles)
        self.assertEqual(mock_stdout.getvalue(), output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_player_cant_play(self, mock_stdout):
        player = Player('Bob')
        tile = Tile(x=1, y=6)
        output = 'Bob can\'t play, drawing tile <1:6>\n'
        player_cant_play(player, tile)
        self.assertEqual(mock_stdout.getvalue(), output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_player_skip_turn(self, mock_stodout):
        player = Player('Alice')
        output = 'Alice can\'t draw or play a tile, skips turn!\n'
        player_skips_turn(player)
        self.assertEqual(mock_stodout.getvalue(), output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_win_message(self, mock_stdout):
        player = Player('Alice')
        output = 'Alice has won!\n'
        win_message(player)
        self.assertEqual(mock_stdout.getvalue(), output)


if __name__ == '__main__':
    unittest.main()
