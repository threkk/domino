import argparse
from domino.game import Game
from domino.player import Player


def start_game(player_names):
    """
    Starts a game with the given player names. It creates the players, draws 7
    tiles for each and starts the game.

    :param player_names: Name of the players to play the game.
    """
    players = [Player(name) for name in player_names]

    game = Game(players)

    for player in players:
        for i in range(0, 7):
            player.draw(game.pop_top())

    game.run()


def cli():
    """
    Creates a simulation of a dominoes game. It takes the defined players to
    play the match until one of them wins. Starting with 7 tiles in hand and
    one randomly chosen on the board, the players alternatively place one tile
    on the board by matching the free numbers with their own tiles. If a player
    cannot play a tile, the player will draw tiles until is able to play a
    tile. In case there are no more tiles to play, the player will skip its
    turn. The first player to empty its hand wins. If given a board state no
    player can place a tile neither draw, the game finishes with a tie.
    """
    parser = argparse.ArgumentParser(prog='domino', description=cli.__doc__)
    parser.add_argument('players', metavar='<players>', type=str, nargs='+',
                        help='Players who will be part of the emulation.')
    args = parser.parse_args()
    start_game(args.players)


if __name__ == '__main__':
    cli()
