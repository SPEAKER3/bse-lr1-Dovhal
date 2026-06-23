def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board):
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            return board[a]
    return None


def is_draw(board):
    return all(cell in ("X", "O") for cell in board)


def choose_player():
    while True:
        symbol = input("Choose your symbol (X/O): ").strip().upper()
        if symbol in ("X", "O"):
            return symbol
        print("Invalid choice. Please enter X or O.")


def show_end_screen(message):
    border = "*" * (len(message) + 4)
    print()
    print(border)
    print(f"* {message} *")
    print(border)
    print()


def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter a move (1-9): ")
            if move.lower() in ("q", "quit", "exit"):
                print("Game exited.")
                raise SystemExit
            position = int(move) - 1
            if position < 0 or position > 8:
                print("Invalid move. Please choose a number between 1 and 9.")
                continue
            if board[position] in ("X", "O"):
                print("That square is already taken. Choose another one.")
                continue
            return position
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9 or q to quit.")


def main():
    board = [str(i + 1) for i in range(9)]
    user_symbol = choose_player()
    opponent_symbol = "O" if user_symbol == "X" else "X"
    current_player = user_symbol

    print("Tic Tac Toe")
    print("Enter a number from 1 to 9 to place your mark. Type q to quit.")
    print(f"You are {user_symbol}. {current_player} goes first.")

    while True:
        display_board(board)
        position = get_move(current_player, board)
        board[position] = current_player

        winner = check_winner(board)
        if winner:
            display_board(board)
            if winner == user_symbol:
                show_end_screen("Congratulations! You win!")
            else:
                show_end_screen("Sorry, you lose.")
            break

        if is_draw(board):
            display_board(board)
            show_end_screen("The game is a draw.")
            break

        current_player = opponent_symbol if current_player == user_symbol else user_symbol


if __name__ == "__main__":
    main()
