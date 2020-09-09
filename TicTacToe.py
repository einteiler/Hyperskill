cells = input("Enter board:")
board = [[[],[],[]],[[],[],[]],[[],[],[]]]
x = 2
counter = 0
while x >= 0:
    y = 0
    while y < 3:
        board[y][x] = cells[counter]
        y += 1
        counter += 1
    x -= 1

def winner(board, player):
    return ((board[0][0] == player and board[0][1] == player and board[0][2] == player) or
            (board[1][0] == player and board[1][1] == player and board[1][2] == player) or
            (board[2][0] == player and board[2][1] == player and board[2][2] == player) or
            (board[0][0] == player and board[1][0] == player and board[2][0] == player) or
            (board[1][0] == player and board[1][1] == player and board[1][2] == player) or
            (board[2][0] == player and board[2][1] == player and board[2][2] == player) or
            (board[0][0] == player and board[1][1] == player and board[2][2] == player) or
            (board[0][2] == player and board[1][1] == player and board[2][0] == player))


# def game_state(board):
#     if (winner(board, 'X') and winner(board, 'O')) or abs(x_count - o_count) > 1:
#         print("Impossible")
#     elif winner(board, 'X'):
#         print("X wins")
#     elif winner(board, 'O'):
#         print("O wins")
#     elif '_' not in board:
#         print("Draw")
#     else:
#         print("Game not finished")

def player_move():
    try:
        move_x, move_y = input("Enter the coordinates:").split()
        if int(move_x) > 3 or int(move_x) < 1 or int(move_y) > 3 or int(move_y) < 1:
            print("Coordinates should be from 1 to 3!")
            return False
        elif board[int(move_x) - 1][int(move_y) - 1] != "_":
            print("This cell is occupied! Choose another one!")
            return False
        else:
            board[int(move_x) - 1][int(move_y) - 1] = "X"
            return True
    except:
        print("You should enter numbers!")
        return False

def display(board):
        print(f"""---------
| {board[0][2]} {board[1][2]} {board[2][2]} |
| {board[0][1]} {board[1][1]} {board[2][1]} |
| {board[0][0]} {board[1][0]} {board[2][0]} |
---------"""
    )

#game_state(board)
display(board)
finished = False
while not finished:
  finished = player_move()
display(board)

