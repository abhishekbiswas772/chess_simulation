from chess_peice.chess_peice import ChessPiece
import operator
from itertools import product
from chess_peice.chess_points import ChessPointsConstants

class Knight(ChessPiece):
    def get_moves(self, board):
        moves = []
        add = operator.add
        sub = operator.sub
        op_list = [(add, sub), (sub, add), (add, add), (sub, sub)]
        nums = [(1, 2), (2, 1)]
        combinations = list(product(op_list, nums))
        for comb in combinations:
            x = comb[0][0](self.x, comb[1][0])
            y = comb[0][1](self.y, comb[1][1])
            if board.has_empty_block(x, y) or board.has_opponent(self, x, y):
                moves.append((x, y))
        return moves

    def get_score(self):
        return ChessPointsConstants.knight