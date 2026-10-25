# TIC-TAC-TOE GAME
# Player = X, AI = O


def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i : i + 3]))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(board, symbol):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # Rows
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # Columns
        (0, 4, 8),
        (2, 4, 6),  # Diagonals
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == symbol:
            return True

    return False


def find_move(board, symbol):
    # Check if a winning move is possible
    for i in range(9):
        if board[i] == " ":
            board[i] = symbol
            if check_winner(board, symbol):
                board[i] = " "
                return i
            board[i] = " "
    return None


def ai_move(board):
    # 1. Check if AI can win
    move = find_move(board, "O")
    if move is not None:
        board[move] = "O"
        return

    # 2. Block the player's winning move
    move = find_move(board, "X")
    if move is not None:
        board[move] = "O"
        return

    # 3. Take the center if available
    if board[4] == " ":
        board[4] = "O"
        return

    # 4. Take a corner if available
    corners = [0, 2, 6, 8]
    for corner in corners:
        if board[corner] == " ":
            board[corner] = "O"
            return

    # 5. Take any available empty cell
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return


def play_game():
    board = [" "] * 9

    print("TIC-TAC-TOE")
    print("You are X")
    print("AI is O")

    display_board(board)

    while True:
        # Player's turn
        try:
            position = int(input("Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Enter a number between 1 and 9.")
                continue

            if board[position - 1] != " ":
                print("Cell already occupied. Try again.")
                continue

            board[position - 1] = "X"

        except ValueError:
            print("Please enter a valid number.")
            continue

        display_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break

        if " " not in board:
            print("It's a draw!")
            break

        # AI's turn
        print("AI is thinking...")
        ai_move(board)
        display_board(board)

        if check_winner(board, "O"):
            print("AI wins!")
            break

        if " " not in board:
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()