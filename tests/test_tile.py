import unittest

from .context_tile import Tile
from .context_tile import make_tile
from .context_tile import is_compatible


class TestTile(unittest.TestCase):
    def test_tile_str(self):
        tile = Tile(x=0, y=6)
        self.assertEqual(tile.__str__(), '<0:6>')

    def test_make_tile(self):
        self.assertRaises(TypeError, make_tile, ['a', 'b'])
        self.assertRaises(TypeError, make_tile, [0, 'b'])
        self.assertRaises(TypeError, make_tile, [-1, 1])
        self.assertRaises(TypeError, make_tile, [1, 7])
        self.assertEqual(make_tile(0, 6), Tile(x=0, y=6))

    def test_is_compatible(self):
        self.assertRaises(TypeError, is_compatible, ['a', 'a'])
        self.assertRaises(TypeError, is_compatible, [-1, 'a'])
        self.assertRaises(TypeError, is_compatible, [7, 'a'])
        self.assertFalse(is_compatible(4, Tile(x=1, y=2)))
        self.assertTrue(is_compatible(4, Tile(x=4, y=2)))
        self.assertTrue(is_compatible(4, Tile(x=2, y=4)))


if __name__ == '__main__':
    unittest.main()
