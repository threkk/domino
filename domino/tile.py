"""
Models the tiles of a domino game. Each time has two sides with a number
each. The numbers range between 1 and 6
"""
from collections import namedtuple

Tile = namedtuple('Tile', ['x', 'y'])


def make_tile(a, b):
    """Creates a new tile ensuring the restrictions on the parameters"""
    assert a >= 1 and a <= 6
    assert b >= 1 and b <= 6
    return Tile(x=a, y=b)


def find_compatible(number, tile):
    """
    Checks which side of the tile (if any) is compatible with the given
    number
    """
    assert number >= 1 and number <= 6
    if tile.x == number:
        return 'x'
    elif tile.y == number:
        return 'y'
    else:
        return None
