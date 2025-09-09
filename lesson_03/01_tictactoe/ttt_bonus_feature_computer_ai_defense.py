# PEDAC for Computer AI: Defense
# Understand the Problem
# Inputs:
    # Human has two squares in a row
# Outputs:
    # Computer attempts to block 3rd square
# Requirements:
    # If no threat, computer picks at random

# Keep in mind:
    # Any implicit requirements
    # The example, including formatting
    # Any inputs to validate
    # Any edge cases

# Mental Model:
    # If Player has two squares in a winning line where the third square is empty, have Computer choose the third square

# Data Structure:
    # List, dictionary

# Algorithm:
    # Check if an empty_square is in a winning_line list
        # Make winning_lines available to computer_chooses_square
            # Remove winning_lines from detect_winner and make it global constant WINNING_LINES
    # Check if HUMAN_MARKER is in winning line twice
        # Create list comprehension of dictionaries with square num as key and marker as value
        # For each empty_square in empty_squares list
            # For line in find_defensive_move list
                # If empty_square in line and line.count(HUMAN_MARKER) == 2
                    # Computer chooses empty_square
                # Else Computer chooses random square
# Code:
import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
# moved WINNING_LINES to global scope from detect_winner function
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], 
    [1, 4, 7], [2, 5, 8], [3, 6, 9], 
    [1, 5, 9], [3, 5, 7]
]
WINNING_SCORE = 5

def prompt(message):
    print(f'=> {message}')

def display_board(board):
    os.system('clear')
    prompt(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')
    print('')
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     ')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(lst, delimiter=', ', conjunction='or'):
    empty_squares = [str(num) for num in lst]

    if len(empty_squares) == 0:
        return ''
    elif len(empty_squares) == 1:
        return empty_squares[0]
    elif len(empty_squares) == 2:
        return f'{empty_squares[0]} {conjunction} {empty_squares[1]}'
    else:
        empty_squares[-1] = f'{conjunction} {empty_squares[-1]}'
        return delimiter.join(empty_squares)

def player_chooses_square(board):
    while True:
        valid_squares = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square: {join_or(empty_squares(board))}')
        square = input().strip()
        if square in valid_squares:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

# added find_defensive_move function
def find_defensive_move(board):    
    for line in WINNING_LINES:
        squares_in_line = [board[square] for square in line]
        if squares_in_line.count(HUMAN_MARKER) == 2:
            for square in line:
                if board[square] == INITIAL_MARKER:
                    return square     
    return None

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    
    # added
    defensive_square = find_defensive_move(board)
    if defensive_square:
        board[defensive_square] = COMPUTER_MARKER
    else:  # choose at random if no defensive squares needed
        square = random.choice(empty_squares(board))    
        board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):  # changed winning_lines to WINNING_LINES and moved to global scope
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER 
              and board[sq2] == HUMAN_MARKER 
              and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER 
              and board[sq2] == COMPUTER_MARKER 
              and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    
    return None

def keep_score(running_score, game_winner):
    running_score[game_winner] += 1
    return running_score

def display_score(running_score):
    return (
        f'Player: {running_score['Player']}   '
        f'Computer: {running_score['Computer']}'
        )

def is_winner(running_score):
    for key, value in running_score.items():
        if value == WINNING_SCORE:
            return key

    return 'Not yet'

def play_tic_tac_toe(): 
    running_score = {'Player': 0, 'Computer': 0}

    while True:
        board = initialize_board()

        while True:
            display_board(board)
            
            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
            
        display_board(board)

        if someone_won(board):
            game_winner = detect_winner(board)
            prompt(f'{game_winner} won!')
            keep_score(running_score, detect_winner(board))
            prompt(display_score(running_score))

            match_winner = is_winner(running_score)
            if match_winner != 'Not yet':
                prompt(f'{match_winner} wins the match!')
                running_score.clear()
        else:
            prompt("It's a tie!")
            prompt(display_score(running_score))

        prompt('Play again? y/n')
        play_again = input().lower()

        if play_again[0] != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()