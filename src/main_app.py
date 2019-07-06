'''
Connect 4 in Python3 written by Stephen Kim for CSB2019 @ Coder Acd

A terminal app written for assessment in Week 5 of Term 1
To look at using variables, variable scopes, loops, functions, conditionals, try/excepts, PEP8 coding
Testing with PyTest and Arguments

'''

import random
import time
import math
from os import system, name
import numpy as np #additional package to create arrays to represent connect 4 board -- instal with the command 'pip install numpy'

# size of board
# allows the changing of board size however not fully implemented within AI logic
ROW_COUNT = 6
COLUMN_COUNT = 7

# values to define players/AI turns
PLAYER_ONE = 0
PLAYER_TWO = 1
AI = 1

# values to represent player tokens
PLAYER_PIECE = 1
AI_PIECE = 2 #also representing player 2

#Part of AI logic
WINDOW_LENGTH = 4
EMPTY = 0

def create_board():
# creates the intial playing board
    board = np.full((ROW_COUNT, COLUMN_COUNT), 0)
    return board

def main_display():
# launches main menu that branches off into AI or Player vs Player modes
    error_count = 0
    gamemode = 'unknown'
    mode = 'unknown'
    clear()
    print('Welcome to Connect 4 within your terminal\nWould you like to versue the AI (Y/N)?\nY = versue the computer\nN = versue a friend')
    while True:
        try:
            mode = input()
            if mode in ('Y', 'y'):
                print('Normal AI or Smart AI? Normal/Smart N/S')
                gamemode = ai_selection()
                print('Launching AI')
                time.sleep(2)
                return gamemode
            elif mode in ('N', 'n'):
                print("Loading two player setup")
                time.sleep(2)
                gamemode = 'pvp'
                return gamemode
            else:
                if error_count <= 0:
                    print("\033[1A\033[KUnknown Input")
                    error_count += 1
                else:
                    print('\033[1A\033[K')
                    print("\033[2A\033[KUnknown Input")
        except ValueError:
            print('Exiting')
    return gamemode

def ai_selection():
    error_count_ai = 0
    gamemode = 'unknown'
    ai_mode = 'unknown'
    while True:
        try:
            ai_mode = input()
            if ai_mode in ('Normal', 'normal', 'n', 'N'):
                gamemode = 'pva'
                return gamemode
            elif ai_mode in ('smart', 'Smart', 's', 'S'):
                gamemode = 'pva_smart'
                return gamemode
            else:
                if error_count_ai <= 0:
                    print("\033[1A\033[KUnknown Input")
                    error_count_ai += 1
                else:
                    print('\033[1A\033[K')
                    print("\033[2A\033[KUnknown Input")
        except ValueError:
            print('Exiting')
    return gamemode

def launchmode(gamemode):
# function that launches the different gamemode
    if gamemode == 'pva':
        player_vs_ai()
    elif gamemode == 'pva_smart':
        player_vs_ai_hard()
    elif gamemode == 'pvp':
        player_vs_player()

def play_again():
# function to play again
    error_count = 0
    play_again = 'unknown'
    print('Would you like to play again (Y/N)?')
    while True:
        try:
            play_again = input()
            if play_again in ('Y', 'y'):
                print('Relaunching game')
                time.sleep(2)
                return main_display()
            elif play_again in ('N', 'n'):
                print("Exiting")
                time.sleep(2)
                return exit()
            else:
                if error_count <= 0:
                    print("\033[1A\033[KUnknown Input")
                    error_count += 1
                else:
                    print('\033[1A\033[K')
                    print("\033[2A\033[KUnknown Input")
        except ValueError:
            print('Exiting')

def drop_piece(board, row, col, piece):
# function that drops player piece into selected column
    board[row][col] = piece

def is_valid_loc(board, col):
# checks to see if column is full or not
    return board[ROW_COUNT-1][col] == 0

def player_one():
# player one turn with validation of input
    while True:
        try:
            col = input('Player 1 Which column would you like to place your piece? (0-6)?')
            val_one = int(col)
            if val_one >= 0 and val_one <= COLUMN_COUNT:
                break
            else:
                print("Invalid input, try again")
        except ValueError:
            print("Amount must be a number, try again")
    col = int(col)
    return col

def player_two():
# player two turn with validation of input
    while True:
        try:
            col = input('Player 2 Which column would you like to place your piece? (0-6)?')
            val_two = int(col)
            if val_two >= 0 and val_two <= COLUMN_COUNT:
                break
            else:
                print("Invalid input, try again")
        except ValueError:
            print("Amount must be a number, try again")
    col = int(col)
    return col

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_board(board):
# function to flip the board as numpy's array is upside down
    # board = pretty_board(board)
    clear()
    print(np.flip(board, 0))
    print('Numbers indicate which column\nC[0 1 2 3 4 5 6]')

# def pretty_board(board):
# # attempt to make board into a more presentable form however did not work well with flip function
#     prt_board = str(board).replace('0', '_').replace('1', 'O').replace('2', 'X')
#     prt_board = str(board).replace('[', ' ').replace(']',' ')
#     board = prt_board
#     return board

def get_next_open_row(board, col):
# part of AI to check all rows
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
# a list of checks to see if a winning move was performed
    # horizontla check
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # vertical check
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # check positively diagonals /
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # check negatively diagonals \
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def score_window(window, piece):
# part of AI's logic to place pieces within certain windows
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2
    elif window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4
    return score

def score_position(board, piece):
# part of AI's logic to check all available positions
    score = 0
    # center scoring
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3
    # horizontal scoring
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += score_window(window, piece)
    # vertical scoring
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += score_window(window, piece)
    # diagonals / scoring
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += score_window(window, piece)
    # diagonls \ scoring
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += score_window(window, piece)

    return score

def get_valid_loc(board):
# Part of AI's logic to see available positions to drop piece
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_loc(board, col):
            valid_locations.append(col)
    return valid_locations

def pick_best_move(board, piece):
# part of AI's logic to find best move for AI
    valid_locations = get_valid_loc(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_loc(board)) == 0

def minimax(board, depth, maximizingPlayer):
# part of AI's logic that looks into depths - Looking several moves ahead
    valid_locations = get_valid_loc(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 10000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000)
            else: #game is over, no valid moves
                return (None, 0)
        else: #depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value
    else: #minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value

def player_vs_ai():
# launches Player vs AI game mode
    board = create_board()
    print_board(board)
    game_over = False
    print('Flipping internal coin for pole position')
    time.sleep(3)
    turn = random.randint(PLAYER_ONE, AI)

    while not game_over:
        # Player 1 turn
        if turn == PLAYER_ONE:
            col = player_one()
            if is_valid_loc(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)
                print(f'Dropping {PLAYER_PIECE} into {col}')
                if winning_move(board, PLAYER_PIECE):
                    print('Player 1 wins')
                    game_over = True
                time.sleep(3)
                turn += 1
                turn = turn % 2
            print_board(board)

    # AI turn
        if turn == AI and not game_over:
            col = pick_best_move(board, AI_PIECE)
            # col, minimax_score = minimax(board, 3, True)
            print('The AI is thinking')
            time.sleep(2)
            if is_valid_loc(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
                print(f'Dropping {AI_PIECE} into {col}')
                if winning_move(board, AI_PIECE):
                    print('The AI wins')
                    game_over = True
                time.sleep(3)
                turn += 1
                turn = turn % 2
            print_board(board)

    play_again()

def player_vs_ai_hard():
# launches Player vs AI game mode - Hard
    board = create_board()
    print_board(board)
    game_over = False
    print('Flipping internal coin for pole position')
    time.sleep(3)
    turn = random.randint(PLAYER_ONE, AI)

    while not game_over:
        # Player 1 turn
        if turn == PLAYER_ONE:
            col = player_one()
            if is_valid_loc(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)
                print(f'Dropping {PLAYER_PIECE} into {col}')
                if winning_move(board, PLAYER_PIECE):
                    print('Player 1 wins')
                    game_over = True
                time.sleep(3)
                turn += 1
                turn = turn % 2
            print_board(board)

    # AI turn
        if turn == AI and not game_over:
            # col = pick_best_move(board, AI_PIECE)
            col, minimax_score = minimax(board, 3, True)
            print('The AI is thinking')
            time.sleep(2)
            if is_valid_loc(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
                print(f'Dropping {AI_PIECE} into {col}')
                if winning_move(board, AI_PIECE):
                    print('The AI wins')
                    game_over = True
                time.sleep(3)
                turn += 1
                turn = turn % 2
            print_board(board)

    play_again()

def player_vs_player():
# launches Player vs Player game mode
    board = create_board()
    print_board(board)
    game_over = False
    print('Flipping internal coin for pole position')
    time.sleep(3)
    turn = random.randint(PLAYER_ONE, PLAYER_TWO)

    while not game_over:
        # Player 1 turn
        if turn == PLAYER_ONE:
            col = player_one()
            if is_valid_loc(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)
                print(f'Dropping {PLAYER_PIECE} into {col}')
                if winning_move(board, PLAYER_PIECE):
                    print('Player 1 wins')
                    game_over = True
                time.sleep(3)
                turn += 1
                turn = turn % 2
            print_board(board)

    # player 2 turn
        if turn == PLAYER_TWO and not game_over:
            col = player_two()
            if is_valid_loc(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
                print(f'Dropping {AI_PIECE} into {col}')
                if winning_move(board, AI_PIECE):
                    print('Player 2 wins')
                    game_over = True
                time.sleep(3)
                turn += 1
                turn = turn % 2
            print_board(board)


    play_again()

gamemode = main_display()
launchmode(gamemode)