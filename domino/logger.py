def start_game(initial_tile):
    print('Game starting with first tile: %s' % str(initial_tile))


def player_plays_connect(player, tile, board):
    print('%s plays %s to connect to tile %s on the board' %
          (str(player), str(tile), str(board)))


def board_state(board):
    print('Board is now: %s' % ' '.join([str(tile) for tile in board]))


def player_cant_play(player, tile):
    print('%s can\'t play, drawing tile %s' % (str(player), str(tile)))


def win_message(player):
    print('Player %s has won!' % str(player))
