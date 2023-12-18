from board import Board
from player import Player
from game_logic import GameLogic

def main():
    board = Board()
    player = Player(board)
    game_logic = GameLogic(board)

    while True:
        board.display_board()
        position = player.get_player_input()
        board.update_board(position, player.current_player)

        winner = game_logic.check_winner()
        if winner:
            board.display_board()
            print(f"Player {winner} wins!")
            break

        if game_logic.check_draw():
            board.display_board()
            print("It's a draw!")
            break

        player.switch_player()

if __name__ == "__main__":
    main()
