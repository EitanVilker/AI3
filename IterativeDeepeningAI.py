import chess
from math import inf

class IterativeDeepeningAI():
    def __init__(self, depth):
        self.depth = depth
        self.current_max_depth = 0
        self.nodes_visited = 0

    # Function that decides the next move the AI will play
    def choose_move(self, board):

        legal_moves = board.legal_moves

        # If white
        if board.turn:
            
            for i in range(self.depth):
                max_move = None
                max_move_val = -inf
                self.current_max_depth += 1
                for move in legal_moves:
                    board.push(move)
                    temp_val = self.get_min(board)
                    board.pop()
                    if temp_val > max_move_val:
                        max_move = move
                        max_move_val = temp_val
            
                print("Best move at depth " + str(i + 1) + " is " + str(max_move))
            self.current_max_depth = 0
            return max_move

        # If black
        for i in range(self.depth):
            min_move = None
            min_move_val = inf
            self.current_max_depth += 1
            for move in legal_moves:
                board.push(move)
                temp_val = self.get_max(board)
                board.pop()
                if temp_val < min_move_val:
                    min_move = move
                    min_move_val = temp_val            
            
            print("Best move at depth " + str(i + 1) + " is " + str(min_move))
        self.current_max_depth = 0
        return min_move
        
    # Function that determines if a terminal or cutoff node has been reached
    def cutoff_test(self, board, current_depth):
        return current_depth >= self.current_max_depth or board.is_game_over()

    # Function that gets the maximum value possible against a minimizing opponent
    def get_max(self, board, current_depth=0):

        self.nodes_visited += 1
        
        if self.cutoff_test(board, current_depth):
            
            # If terminal state reached
            if board.is_game_over():
                result = board.outcome()
                # If draw
                if result is None:
                    return 0
                # If black won
                if result.winner == chess.BLACK:
                    return -inf
                # If white won
                return inf

            # If cutoff state reached
            return self.material_diff_heuristic(board)
        
        current_best_move = None
        max_val = -inf
        for move in board.legal_moves:
            board.push(move)
            temp_val = self.get_min(board, current_depth=(current_depth+1))
            board.pop()
            if temp_val > max_val:
                max_val = temp_val
        
        return max_val

    # Function that gets the minimum value possible against a maximizing opponent
    def get_min(self, board, current_depth=0):

        self.nodes_visited += 1
        
        if self.cutoff_test(board, current_depth):

            # If terminal state reached
            if board.is_game_over():

                result = board.outcome()

                # If draw
                if result is None:
                    return 0
                
                # If black won
                if result.winner == chess.BLACK:
                    return -inf
                
                # If white won
                return inf

            # If cutoff state reached
            return self.material_diff_heuristic(board)
        
        min_val = inf
        for move in board.legal_moves:
            board.push(move)
            temp_val = self.get_max(board, current_depth=(current_depth+1))
            board.pop()
            if temp_val < min_val:
                min_val = temp_val
        
        return min_val

    # Heuristic that returns the current value of the board state 
    # based on the values of the current pieces from the perspective of white
    def material_diff_heuristic(self, board):

        white_ahead_by = 0

        # Queens
        white_ahead_by += 8 * (len(board.pieces(chess.QUEEN, chess.WHITE)) - len(board.pieces(chess.QUEEN, chess.BLACK)))
        # Rooks
        white_ahead_by += 5 * (len(board.pieces(chess.ROOK, chess.WHITE)) - len(board.pieces(chess.ROOK, chess.BLACK)))
        # Knights
        white_ahead_by += 3 * (len(board.pieces(chess.KNIGHT, chess.WHITE)) - len(board.pieces(chess.KNIGHT, chess.BLACK)))
        # Bishop
        white_ahead_by += 3 * (len(board.pieces(chess.BISHOP, chess.WHITE)) - len(board.pieces(chess.BISHOP, chess.BLACK)))
        # Pawns
        white_ahead_by += 1 * (len(board.pieces(chess.PAWN, chess.WHITE)) - len(board.pieces(chess.PAWN, chess.BLACK)))

        return white_ahead_by