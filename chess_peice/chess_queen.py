from chess_peice.chess_peice import ChessPiece
from chess_peice.chess_rook import Rook
from chess_peice.chess_bishop import Bishop
from chess_peice.chess_points import ChessPointsConstants

class Queen(ChessPiece):
    def get_score(self):
        return ChessPointsConstants.queen
    

    def get_moves(self, board):
        moves = []
        rook = Rook(self.color, self.x, self.y, self.unicode)
        bishop = Bishop(self.color, self.x, self.y, self.unicode)
        rook_moves = rook.get_moves(board)
        bishop_moves = bishop.get_moves(board)
        if rook_moves:
            moves.extend(rook_moves)
        if bishop_moves:
            moves.extend(bishop_moves)
        return moves
