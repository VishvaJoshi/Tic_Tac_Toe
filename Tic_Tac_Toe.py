def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def make_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row and column): ").split()
        if len(move) != 2:
            print("Please enter two numbers.")
            continue
        row, col = move
        if not (row.isdigit() and col.isdigit()):
            print("Please enter valid numbers.")
            continue
        row, col = int(row), int(col)
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Move out of bounds. Try again.")
            continue
        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue
        board[row][col] = player
        break

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    while True:
        print_board(board)
        make_move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
