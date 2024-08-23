# Tic-Tac-Toe game in Python

# Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


# Check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


# Check if the board is full
def check_full(board):
    return all([cell != ' ' for row in board for cell in row])


# Get the player's move
def get_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Try again.")
            elif board[move // 3][move % 3] != ' ':
                print("Cell already taken. Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")


# Main game function
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        move = get_move(board)
        board[move // 3][move % 3] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
