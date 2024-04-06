class TicTacToe3D:
    def main(self):
        ai_player = AIPlayer()
        board = Board()

        board.display_board()

        # Prompt the user for who will make the first move
        print("Who makes the first move? (1)Computer (2)User: ")
        choice = int(input())
        if choice == 1:
            ai_player.perform_mcts(board)
            board.place_a_move(ai_player.return_best_move(), 1)
            board.display_board()

        # While the game isn't over prompt the user for their next move
        while not board.is_game_over():
            print("Your move: layer (1, 2, or 3), row (1, 2, or 3), column (1, 2, or 3)")
            user_move = Point(int(input()) - 1, int(input()) - 1, int(input()) - 1)
            while board.get_state(user_move) != 0:
                print("Invalid move. Make your move again: ")
                user_move.x = int(input()) - 1
                user_move.y = int(input()) - 1
                user_move.z = int(input()) - 1
            board.place_a_move(user_move, 2)
            board.display_board()

            if board.is_game_over():
                break

            # Calculate the AI move and updating board accordingly
            ai_player.perform_mcts(board)
            board.place_a_move(ai_player.return_best_move(), 1)
            board.display_board()

        # display the final outcome of the game
        if board.has_x_won():
            print("Unfortunately, you lost!")
        elif board.has_o_won():
            print("You win!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    ttt3d = TicTacToe3D()
    ttt3d.main()
