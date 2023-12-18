def make_ai_move(board):
    def is_winner(board, symbol):
        # check for winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(board[i] == symbol for i in combo):
                return True
        return False

    # priority 1
    # check if AI can win in the next move
    for i in range(9):
        if board[i] is None:
            board[i] = 'O'
            if is_winner(board, 'O'):
                board[i] = None
                return i
            board[i] = None

    # priority 2
    # block opponent's winning move
    for i in range(9):
        if board[i] is None:
            board[i] = 'X'
            if is_winner(board, 'X'):
                board[i] = None
                return i
            board[i] = None

    # priority 3
    # play center if available
    if board[4] is None:
        return 4

    # priority 4
    # play in a corner
    for i in [0, 2, 6, 8]:
        if board[i] is None:
            return i

    # priority 5
    # play in a side
    for i in [1, 3, 5, 7]:
        if board[i] is None:
            return i

    # no move available
    return None
