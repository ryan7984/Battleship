import random

"""
This function creates the board for the game.
"""


def create_board(size):
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


def place_ships(board, num_ships):
    for i in range(num_ships):
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0]) - 1)
        board[ship_row][ship_col] = "S"


"""
This function will check if the users guess is on the board.
"""


def valid_guess(guess, board):
    row, col = guess
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    elif board[row][col] == "S":
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


"""
This function will update the board with the users guess
"""


def update_board(guess, board):
    row, col = guess
    if board[row][col] == "S":
        board[row][col] = "X"
        return True 
    else:
        board[row][col] = "."
        return False


"""
This is the main function to run the game where the player enters the game
board size, the number of ships and there guess.
"""


def play_battleships():
    size = int(input("Enter the size of the game board:\n"))
    num_ships = int(input("Enter the number of ships:\n"))
    board = create_board(size)
    place_ships(board, num_ships)
    print_board(board)
    num_guesses = 0
    while True:
        guess_str = input("Enter your guess (row, col): \n")
        guess = tuple(map(int, guess_str.split(",")))
        if not valid_guess(guess, size):
            print("Invalid guess. Try again.")
            continue
        result = check_guess(guess, board)
        if result == "Already guessed":
            print("You already guessed that spot. Try again")
            continue
        num_guesses += 1
        if update_board(guess, board):
            print("Hit!")
            if all(all(c != "S" for c in row) for row in board):
                print("Congratulations! You sank all the battleships in",
                      num_guesses, "guesses.")
                break

        else:   
            print("Miss.")