class GameLogic:
    # game logic constructor 
    def __init__(self, board):
        self.board = board

    # method to check winner
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in winning_combinations:
            if self.is_winning_combo(combo):
                return self.board.board[combo[0]]
        return None

    # method to if check winning combo satisfied
    def is_winning_combo(self, combo):
        first, second, third = combo
        return self.board.board[first] == self.board.board[second] == self.board.board[third] and self.board.board[first] is not None

    # method to check draw
    def check_draw(self):
        return all(cell is not None for cell in self.board.board)

