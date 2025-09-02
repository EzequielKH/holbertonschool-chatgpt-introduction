#!/usr/bin/env python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Revisar filas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]
    # Revisar columnas
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Revisar diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers only (0, 1, or 2).")
            continue
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            break

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid input. Numbers must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Cambiar jugador
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

