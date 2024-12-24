from chess_peice.chess_peice import ChessPiece
import operator
from chess_peice.chess_points import ChessPointsConstants

class Bishop(ChessPiece):
    def get_moves(self, board):
        moves = []
        add = operator.add
        sub = operator.sub
        operators = [(add, add), (add, sub), (sub, add), (sub, sub)]
        for ops in operators:
            for i in range(1, 9):
                x = ops[0](self.x, i)
                y = ops[1](self.y, i)
                if not board.is_valid_move(x, y) or board.has_friend(self, x, y):
                    break
                if board.has_empty_block(x, y):
                    moves.append((x, y))
                if board.has_opponent(self, x, y):
                    moves.append((x, y))
                    break
        return moves

    def get_score(self):
        return ChessPointsConstants.bishop