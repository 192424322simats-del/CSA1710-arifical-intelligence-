N = 8

# Check whether queen can be placed
def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking function
def solve(board, row):

    if row == N:
        print_board(board)
        return True

    for col in range(N):

        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            board[row] = -1

    return False


# Print chess board
def print_board(board):

    for row in range(N):
        for col in range(N):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# Main program
board = [-1] * N

if solve(board, 0):
    print("8-Queen Solution:")
    print_board(board)
else:
    print("No solution found")
