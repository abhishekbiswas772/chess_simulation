import chess_graphics.graphics as graphics
from chess_board.chess_board import *


if __name__ == '__main__':
    keep_playing = True

    board = ChessBoard(game_mode=0, ai=True, depth=1, log=True)

    while keep_playing:
        graphics.initialize()
        board.place_pieces()
        graphics.draw_background(board)
        keep_playing = graphics.start(board)
        