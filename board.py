class Board:
    def __init__(self):
        self.board = [None] * 9

    def display_board(self):
        for i in range(3):
            row = [" " if x is None else x for x in self.board[i*3:(i+1)*3]]
            print("|".join(row))
            if i < 2:
                print("-----")

    def update_board(self, position, symbol):
        self.board[position] = symbol
