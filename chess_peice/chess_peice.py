class ChessPiece:
    eaten_pieces_history = []
    has_moved_history = []
    position_history = []


    def __init__(self, color, x, y, unicode):
        self.color = color
        self.x = x
        self.y = y
        self.unicode = unicode
        self.moved = False
        self.type = self.__class__.__name__
    

    def get_moves(self, board):
        pass


    def get_score(self):
        return 0
    
    def get_last_eaten(self):
        return self.eaten_pieces_history.pop()
    
    def set_last_eaten(self, peice):
        return self.eaten_pieces_history.append(peice)
    
    def set_position(self, x, y, keep_history):
        if keep_history:
            self.position_history.append(self.x)
            self.position_history.append(self.y)
            self.has_moved_history.append(self.moved)
        self.x = x
        self.y = y
        self.moved = True
    
    def set_old_position(self):
        position_y = self.position_history.pop()
        position_x = self.position_history.pop()
        self.y = position_y
        self.x = position_x
        self.moved = self.has_moved_history.pop()
    

    def filter_moves(self, moves, board):
        final_moves = moves[:]
        for move in moves:
            board.make_move(self, move[0], move[1], keep_history=True)
            if board.king_is_threatened(self.color, move):
                final_moves.remove(move)
            board.unmake_move(self)
        return final_moves

    def __repr__(self):
        return '{}: {}|{},{}'.format(self.type, self.color, self.x, self.y)


