def print_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                print('X', end=' ')
            elif board[i][j] == 2:
                print('O', end=' ')
            else:
                print(' ', end=' ')
        print()


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] > 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] > 0:
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]) and board[1][1] > 0:
        return board[1][1]
    return 0


board = [[0 for _ in range(3)] for _ in range(3)]
player = 1
steps = 0
winner = 0
print_board(board)
while steps < len(board) ** 2:
    print(f'Ходит игрок {player}')
    row, col = map(int, input('Введите номер строки и столбца: ').split())
    if (not 0 <= row <= 2 or not 0 <= col <= 2) or board[row][col] != 0:
        print('Попробуйте еще раз')
        continue
    board[row][col] = player
    steps += 1
    print_board(board)
    winner = check_winner(board)
    if winner != 0:
        break
    player = 3 - player
if winner:
    print(f'Победил игрок {winner}')
else:
    print('Ничья!')