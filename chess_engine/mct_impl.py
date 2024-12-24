import math
import random
from collections import defaultdict
from chess_peice.chess_peice import ChessPiece

class Node:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.visits = 0
        self.value = 0
        self.children = []

    def is_fully_expanded(self):
        return len(self.children) == len(self.get_legal_moves())

    def get_legal_moves(self):
        moves = []
        for i in range(8):
            for j in range(8):
                if isinstance(self.board[i][j], ChessPiece) and self.board[i][j].color == self.board.get_player_color():
                    piece = self.board[i][j]
                    moves.extend([(piece, move) for move in piece.get_moves(self.board)])
        return moves

    def expand(self):
        legal_moves = self.get_legal_moves()
        for piece, move in legal_moves:
            child_board = self.board.copy()  # Assume `copy` method creates a deepcopy of the board
            child_board.make_move(piece, move[0], move[1], keep_history=True)
            child_node = Node(child_board, parent=self, move=(piece, move))
            self.children.append(child_node)

    def best_child(self, exploration_weight=1.0):
        return max(
            self.children,
            key=lambda child: child.value / (child.visits + 1) +
            exploration_weight * math.sqrt(math.log(self.visits + 1) / (child.visits + 1))
        )

def mcts(board, iterations=1000, exploration_weight=1.0):
    root = Node(board)
    
    for _ in range(iterations):
        node = root

        # Selection
        while node.children and node.is_fully_expanded():
            node = node.best_child(exploration_weight)

        # Expansion
        if not node.children:
            node.expand()

        # Simulation
        child = random.choice(node.children)
        result = simulate_random_game(child.board)

        # Backpropagation
        while child:
            child.visits += 1
            child.value += result
            child = child.parent

    best_move_node = root.best_child(exploration_weight=0)
    return best_move_node.move

def simulate_random_game(board):
    """Simulates a random game starting from the given board."""
    while not board.is_terminal():
        legal_moves = []
        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], ChessPiece):
                    piece = board[i][j]
                    legal_moves.extend([(piece, move) for move in piece.get_moves(board)])
        if not legal_moves:
            break
        piece, move = random.choice(legal_moves)
        board.make_move(piece, move[0], move[1], keep_history=False)
    return board.evaluate()
