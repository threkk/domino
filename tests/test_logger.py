import unittest
import unittest.mock
from io import StringIO
from .context_tile import Tile
from .context_logger import start_game
from .context_logger import board_state


class TestLogger(unittest.TestCase):
    # https://stackoverflow.com/a/34738440
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_start_game(self, mock_stdout):
        output = 'Game starting with first tile: <4:1>\n'
        start_game(Tile(x=4, y=1))
        self.assertEqual(mock_stdout.getvalue(), output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_board_state(self, mock_stdout):
        tiles = [Tile(x=0, y=4), Tile(x=4, y=1)]
        output = 'Board is now: <0:4> <4:1>\n'
        board_state(tiles)
        self.assertEqual(mock_stdout.getvalue(), output)
