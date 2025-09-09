# Keep Score
# Inputs:
    # Game winner as string
# Outputs:
    # Score after each game
    # Winner of match
# Explicit rules:
    # A match is won by the first player to win 5 games
    # Reset the scores to 0 when beginning a new match
    # Don't use global variables except symbolic constant for number of games needed to win a match
# Data structure:
    # Maybe a dictionary for player and computer scores
# Algorithm:
    # Given `game_winner`
        # `detect_winner(board)` returns winner as string
    # Keep a running score after each game
        # Set `running_score` to empty dictionary
        # If `game_winner` is not in `running_score`
            # Add key `game_winner` to `running_score` w/ value of 0
        # Add 1 to `game_winner` value
    # Once a player has 5 wins, announce the overall winner
        # If 'game_winner' value is 5, output overall winner message
        # Reset scores to 0
    
# Code:
# The code below is the entire tic tac toe program, with comments indicating where code was added for the Keep Score features
import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_SCORE = 5  # added

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

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], 
        [1, 4, 7], [2, 5, 8], [3, 6, 9], 
        [1, 5, 9], [3, 5, 7]
    ]

    for line in winning_lines:
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

# keep_score, display_score, is_winner functions added
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
    running_score = {'Player': 0, 'Computer': 0}  # added

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
            game_winner = detect_winner(board)  # added
            prompt(f'{game_winner} won!')  # refactored to replace function call
            keep_score(running_score, detect_winner(board))  # moved and removed variable assignment
            prompt(display_score(running_score))  # moved

            # these 4 lines moved up to if block
            match_winner = is_winner(running_score)
            if match_winner != 'Not yet':
                prompt(f'{match_winner} wins the match!')
                running_score.clear()
        else:
            prompt("It's a tie!")
            prompt(display_score(running_score))  # added for tie

        prompt('Play again? y/n')
        play_again = input().lower()

        if play_again[0] != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()