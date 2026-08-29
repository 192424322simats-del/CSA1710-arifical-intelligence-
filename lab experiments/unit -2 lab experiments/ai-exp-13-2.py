def minimax(board, depth, is_maximizing):

    # Check terminal states
    if check_winner(board, 'O'):
        return 1

    if check_winner(board, 'X'):
        return -1

    if ' ' not in board:
        return 0

    # Maximizing player - O
    if is_maximizing:

        best_score = -100

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'O'

                score = minimax(
                    board, depth + 1, False
                )

                board[i] = ' '

                best_score = max(best_score, score)

        return best_score

    # Minimizing player - X
    else:

        best_score = 100

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'X'

                score = minimax(
                    board, depth + 1, True
                )

                board[i] = ' '

                best_score = min(best_score, score)

        return best_score


def check_winner(board, player):

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        if board[a] == board[b] == board[c] == player:
            return True

    return False


def find_best_move(board):

    best_score = -100
    best_move = -1

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            score = minimax(board, 0, False)

            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# Main program
board = [
    'X', 'O', 'X',
    ' ', 'O', ' ',
    ' ', ' ', 'X'
]

print("Current Board:")
print(board[0], "|", board[1], "|", board[2])
print("--+---+--")
print(board[3], "|", board[4], "|", board[5])
print("--+---+--")
print(board[6], "|", board[7], "|", board[8])

move = find_best_move(board)

print("\nBest move for O:", move + 1)
