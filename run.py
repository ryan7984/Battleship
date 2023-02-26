import random

# function to create the game board
def create_board(size):
    board = []
    for i in range(size):
        row = ["O"] * size
        board.append(row)
    return board

# function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# function to place the ships randomly on the board
def place_ships(board, num_ships):
    for i in range(num_ships):
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0]) - 1)
        board[ship_row][ship_col] = "S"

# function to check if the user's guess is on the board
def valid_guess(guess, size):
    row, col = guess
    return 0 <= row < size and 0 <= col < size

# function to check if the user's guess is a hit or a miss
def check_guess(guess, board):
    row, col = guess
    if board[row][col] == "S":
        return "hit"
    elif board[row][col] == "X":
        return "already guessed"
    else:
        return "miss"

# function to update the board with the user's guess
def update_board(guess, board):
    row, col = guess
    if board[row][col] == "S":
        board[row][col] = "X"
        return True
    else:
        board[row][col] = "."
        return False

# main function to run the game
def play_battleships():
    size = int(input("Enter the size of the game board: "))
    num_ships = int(input("Enter the number of ships: "))
    board = create_board(size)
    place_ships(board, num_ships)
    print_board(board)
    num_guesses = 0
    while True:
        guess_str = input("Enter your guess (row, col): ")
        guess = tuple(map(int, guess_str.split(",")))
        if not valid_guess(guess, size):
            print("Invalid guess. Try again.")
            continue
        result = check_guess(guess, board)
        if result == "already guessed":
            print("You already guessed that spot. Try again.")
            continue
        num_guesses += 1
        if update_board(guess, board):
            print("Hit!")
            if all(all(c != "S" for c in row) for row in board):
                print("Congratulations! You sank all the battleships in", num_guesses, "guesses.")
                break
        else:
            print("Miss.")

