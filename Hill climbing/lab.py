import random

N = 8

# One queen per column
def random_board():
    board = list(range(N))
    random.shuffle(board)
    return board


# Count all attacking pairs
def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            # Same row or same diagonal
            if (board[i] == board[j] or
                abs(board[i] - board[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


def hill_climbing():
    while True:
        board = random_board()

        while True:
            current = heuristic(board)

            if current == 0:
                return board

            best_board = None
            best_h = current

            for col in range(N):
                for row in range(N):
                    if row != board[col]:
                        neighbor = board[:]
                        neighbor[col] = row

                        h = heuristic(neighbor)

                        if h < best_h:
                            best_h = h
                            best_board = neighbor

            if best_board is None:
                break

            board = best_board


def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


solution = hill_climbing()

print("Solution:", solution)
print("Heuristic:", heuristic(solution))

print("\nChessboard:")
print_board(solution)
