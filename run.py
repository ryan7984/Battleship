import random

"""
This function creates the board for the game.
"""

def game_board(size):
    board = []
    for i in range(size):
        row = ["0"]* size
        board.append(row)
    return board    


"""
This function prints the game board.
"""
def print_board(board):
    for row in board:
        print("".join(row))

"""
This function will place the ships randomly on the board
"""
def place_ships(board,num_ships):
    for i in range(num_ships):
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0] - 1)
        board[ship_row][ship_col] = "S"

"""
This function will check if the users guess is on the board.
"""
def valid_guess(guess, size):
    row, col = guess
    if board[row][col] == "S":
        return "hit"
    elif board[row][col] == "x":
        return "already guessed"
    else:
        return "miss"

"""
This function will check if the players guess is hit or miss.
"""
def check_guess(guess, board):
    row, col = guess
    if board[row][col] == "S":
        return "hit"
    elif board[row][col] == "X":
        return "already guessed"
    else:
        return "miss"









