from board import Board
from player import Player
from game_logic import GameLogic

def main():

    # create objects
    board = Board()
    player = Player(board)
    game_logic = GameLogic(board)

    # game loop
    while True:

        # display board
        board.display_board()

        # take input
        position = player.get_player_input()

        # update board
        board.update_board(position, player.current_player)

        # check for winner
        winner = game_logic.check_winner()
        if winner:
            board.display_board()
            print(f"Player {winner} wins!")
            break
        
        # check for draw
        if game_logic.check_draw():
            board.display_board()
            print("It's a draw!")
            break
        
        #  switch player
        player.switch_player()

if __name__ == "__main__":
    main()
