import argparse
from domino.game import Game
from domino.player import Player


def start_game(player_names):
    players = [Player(name) for name in player_names]

    game = Game(players)

    for player in players:
        for i in range(0, 7):
            player.draw(game.pop_top())

    game.run()


def cli():
    parser = argparse.ArgumentParser(prog='domino',
                                     description='Dominoes simulator')
    parser.add_argument('players', metavar='<players>', type=str, nargs='+',
                        help='Players who will be part of the emulation.')
    args = parser.parse_args()
    start_game(args.players)


if __name__ == '__main__':
    cli()
