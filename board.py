"""
Jericho Adalin and Quang Loc Tran
420-LCU Computer Programming, Section 2
Thursday, May 28
R. Vincent, instructor
Final Project
"""

'''Matrix representation of a Connect Four board.'''

def board_create(rows = 6, cols = 7):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def board_rows(board):
    '''Returns the number of rows in the board.'''
    return len(board)

def board_cols(board):
    '''Returns the number of columns in the board'''
    return len(board[0])

def board_get(board, row, col):
    '''Returns the state of a single board position.'''
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return None
    return board[row][col]

def board_put(board, row, col, code):
    '''Place a piece at row, col.'''
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return
    board[row][col] = code

def board_copy(board):
    '''Construct a copy of the given board.'''
    return [[value for value in row] for row in board]


# def board_count(board, value):
#     '''Return the number of squares on the board that contain the given value.''' 
#     count = 0
#     for row in board:
#         for column in row:
#             if value == column: #checks every square and tests equality
#                 count += 1
#     return count

