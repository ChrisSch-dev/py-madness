def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win = [player]*3
    return (any(row == win for row in board) or
            any([board[i][j] for i in range(3)] == win for j in range(3)) or
            [board[i][i] for i in range(3)] == win or
            [board[i][2-i] for i in range(3)] == win)

def main():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    for turn in range(9):
        print_board(board)
        move = input(f"Player {player} move (row col): ")
        r, c = map(int, move.split())
        if board[r][c] != " ":
            print("Cell taken, try again.")
            continue
        board[r][c] = player
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    print_board(board)
    print("Draw!")

if __name__ == "__main__":
    main()