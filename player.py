from ai_player import make_ai_move

class Player:
    # player constructor
    def __init__(self, board, turn='player'):
        self.current_player = 'X'
        self.board = board
        self.turn = turn

    # method to take input
    def get_player_input(self):
        while True:
            try:
                # take player input
                if self.turn == 'player':
                    position = int(input(f"Enter your move (1-9): "))-1

                # take AI input
                if self.turn == 'ai':
                    print("AI's move:")
                    position = make_ai_move(self.board.board)

                # check for input validity
                if position < 0 or position > 8:
                    print("Invalid position. Please enter a number between 1 and 9.")
                elif self.board.board[position ] is not None:
                    print("This position is already occupied. Try another one.")
                else:
                    return position
                
            except ValueError:
                print("Invalid input. Please enter a number.")

    # method to switch player
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.turn = 'ai' if self.turn == 'player' else 'player'
