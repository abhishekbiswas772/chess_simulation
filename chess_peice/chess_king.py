from chess_peice.chess_peice import ChessPiece
import operator
from chess_peice.chess_points import ChessPointsConstants

class King(ChessPiece):
    def get_moves(self, board):
        moves = []
        moves += self.get_horizontal_moves(board)
        moves += self.get_vertical_moves(board)
        return moves

    def get_vertical_moves(self, board):
        moves = []
        for op in [operator.add, operator.sub]:
            x = op(self.x, 1)
            if board.has_empty_block(x, self.y) or board.has_opponent(self, x, self.y):
                moves.append((x, self.y))
            if board.has_empty_block(x, self.y + 1) or board.has_opponent(self, x, self.y + 1):
                moves.append((x, self.y+1))
            if board.has_empty_block(x, self.y - 1) or board.has_opponent(self, x, self.y - 1):
                moves.append((x, self.y - 1))
        return moves

    def get_horizontal_moves(self, board):
        moves = []
        for op in [operator.add, operator.sub]:
            y = op(self.y, 1)
            if board.has_empty_block(self.x, y) or board.has_opponent(self, self.x, y):
                moves.append((self.x, y))
        return moves
    
    def get_score(self):
        return ChessPointsConstants.king

