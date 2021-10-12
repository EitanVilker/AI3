import chess
from random import shuffle
from math import inf

class AlphaBetaAI():
    def __init__(self, depth):
        self.depth = depth
        self.nodes_visited = 0
        self.reordering = "capture"

    # Function that decides the next move the AI will play. 
    # Basically does the first round of minimax so that the algorithm doesn't have to pass any moves down
    def choose_move(self, board):

        if self.reordering == "random":
            legal_moves = self.randomize_legal_moves(board)
        elif self.reordering == "capture":
            legal_moves = self.order_moves_by_capture(board)

        alpha = -inf
        beta = inf

        # If white
        if board.turn:
            max_move = None
            max_move_val = -inf
            for move in legal_moves:
                board.push(move)
                temp_val = self.get_min(board, alpha=alpha, beta=beta)
                board.pop()
                if temp_val > max_move_val:
                    max_move = move
                    max_move_val = temp_val
                alpha = max(alpha, max_move_val)
                if beta <= alpha:
                    break
            
            return max_move

        # If black
        min_move = None
        min_move_val = inf
        for move in legal_moves:
            board.push(move)
            temp_val = self.get_max(board, alpha=alpha, beta=beta)
            board.pop()

            if temp_val < min_move_val:
                min_move = move
                min_move_val = temp_val

            beta = min(beta, min_move_val)
            if beta <= alpha:
                break

        return min_move
        
    # Function that determines if a terminal or cutoff node has been reached
    def cutoff_test(self, board, current_depth):
        return current_depth >= self.depth or board.is_game_over()

    # Function that gets the maximum value possible against a minimizing opponent
    def get_max(self, board, alpha=-inf, beta=inf, current_depth=0):

        if self.reordering == "random":
            legal_moves = self.randomize_legal_moves(board)
        elif self.reordering == "capture":
            legal_moves = self.order_moves_by_capture(board)
        else:
            legal_moves = board.legal_moves

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
        for move in legal_moves:
            board.push(move)
            temp_val = self.get_min(board, alpha=alpha, beta=beta, current_depth=(current_depth+1))
            board.pop()
            if temp_val > max_val:
                max_val = temp_val
        
            alpha = max(alpha, max_val)
            if beta <= alpha:
                break

        return max_val

    # Function that gets the minimum value possible against a maximizing opponent
    def get_min(self, board, alpha=-inf, beta=inf, current_depth=0):

        if self.reordering == "random":
            legal_moves = self.randomize_legal_moves(board)
        elif self.reordering == "capture":
            legal_moves = self.order_moves_by_capture(board)
        else:
            legal_moves = board.legal_moves
        
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
        for move in legal_moves:
            board.push(move)
            temp_val = self.get_max(board, alpha=alpha, beta=beta, current_depth=(current_depth+1))
            board.pop()
            if temp_val < min_val:
                min_val = temp_val
            beta = min(beta, min_val)
            if beta <= alpha:
                break
        
        return min_val

    # Function to randomize the order of the available moves
    def randomize_legal_moves(self, board):

        legal_moves = list(board.legal_moves)
        shuffle(legal_moves)
        return legal_moves

    # Function to put all capture moves at beginning of list
    def order_moves_by_capture(self, board):

        reordered_moves = []
        for move in board.legal_moves:
            target_square = move.to_square
            if board.piece_type_at(target_square) is not None:
                reordered_moves.insert(0, move)
            else:
                reordered_moves.append(move)
        return reordered_moves


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