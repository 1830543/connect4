"""
Jericho Adalin and Quang Loc Tran
420-LCU Computer Programming, Section 2
Thursday, May 28
R. Vincent, instructor
Final Project
"""

'''Implements the logic for the game Connect Four.'''

from board import *
from random import choice

HUMAN = 1
COMPUTER = 2
DIFFICULTY=1


def game_start():
    '''Create, initialize, and return a board object.'''
    board = board_create()
    return board

def game_turn(board,col):
    '''Implements the back forth mechanic of Connect Four. When called it first
    places the piece of the Human Player, than it performs the appriopriate computer move.
    If it the winning move is the player move, it exits.
    '''
    if is_legal_move(board, col):
        move(board,HUMAN,col)
        if is_game_over(board,HUMAN):
            return
        else:
           moves=legal_moves(board)
           if len(moves)>0: #Check if over
            move(board, COMPUTER, computer_move(board, DIFFICULTY))


def board_score(board, player):
    '''Returns the state of the board.'''
    score = 0
    if is_win(board, player):
        score = 4
    elif is_connect3(board, player):
        score = 3
    elif is_connect2(board, player):
        score = 2
    return score
    
def legal_moves(board):
    ''' Returns a list of all legal moves for a given board state'''
    legal_cols = []
    for x in range(board_cols(board)):
        cols = []
        col_number = 0
        for y in range(board_rows(board)):
            cols.append(board[y][x])
            col_number = x
        if not all(cols):
            legal_cols.append(col_number)
    return legal_cols

def is_legal_move(board,col):
    ''' Checks if the given move is legal, uses legal_moves as a reference'''
    if col in legal_moves(board):
        return True
    else:
        return False

def move(board, player, col):
    '''Performs the move for a given player at a given column
        while simultaneously checking if the game is over '''
    for y in range(board_rows(board)):
        if board[y][col]:
            board[y - 1][col] = player
            is_game_over(board, player)
            break
        elif y==(board_rows(board)-1): #if no pieces are present place the piece on the bottom row
            board[y][col]=player
            is_game_over(board, player)

def computer_move(board, DIFFICULTY):
    ''' Dependent on difficulty, it picks a move for the computer to play. It returns
    the move to be played'''
    if DIFFICULTY == 1:
        return choice(legal_moves(board)) #random move
        
    if DIFFICULTY == 2: #Greedy algorithm
        best_moves = []
        test_board=board_copy(board)
        score=0
        for x in legal_moves(board):
            move(test_board, COMPUTER, x)
            new_score=board_score(test_board,COMPUTER)
            if new_score>score:
                score=new_score
                best_moves.clear()
                best_moves.append(x)
            elif new_score==score:
                best_moves.append(x)
            test_board=board_copy(board)
        if len(best_moves)>1:
            return choice(best_moves)
        else:
            return best_moves[0]
        
    if DIFFICULTY== 3: #minmax algorithm
        best_moves=[]
        test_moves=[]
        test_board1=board_copy(board)
        player=COMPUTER
        scores={COMPUTER:0, HUMAN:0}
        Total_P=0
        for x in legal_moves(board):
            player=COMPUTER
            move(test_board1, player, x)
            test_board2=board_copy(test_board1)
            
            for y in legal_moves(test_board2): #checks countermoves
                player=HUMAN
                move(test_board2, player, y)
                P_score=board_score(test_board2,player)
                if P_score <=3:
                    if scores[player]==0: #picks move with worst countermove
                        scores[player]=P_score
                        test_moves.append(x)
                    elif P_score<scores[player]:
                        scores[player]=P_score
                        test_moves.clear()
                        test_moves.append(x)
                    elif P_score==scores[player]:
                        test_moves.append(x)

                test_board2=board_copy(test_board1)
                
            test_board1=board_copy(board)
        print(test_moves)

        for x in test_moves: #picks move with worst countermove and best personal gain
            test_board3=board_copy(board)
            player=COMPUTER
            move(test_board3, player, x)
            C_score=board_score(test_board3,player)

            if C_score==4:
                return x
            elif C_score>scores[player]:
                scores[player]=C_score
                best_moves.clear()
                best_moves.append(x)
            elif C_score==scores[player]:
                best_moves.append(x)
              
        if len(best_moves)>1: #random move from move resevoir
            return choice(best_moves)
        else:
            return best_moves[0]
            

def is_win(board, player):
    '''Returns true if a player has achieved a Connect 4'''
    tile = player

    # Horizontal check
    for x in range(board_cols(board) - 3):
        for y in range(board_rows(board)):
            if board[y][x] == tile and board[y][x + 1] == tile and board[y][x + 2] == tile and board[y][x + 3] == tile:
                return True

    # Vertical check
    for x in range(board_cols(board)):
        for y in range(board_rows(board) - 3):
            if board[y][x] == tile and board[y + 1][x] == tile and board[y + 2][x] == tile and board[y + 3][x] == tile:
                return True

    # Descending diagonal check
    for x in range(board_cols(board) - 3):
        for y in range(board_rows(board) - 3):
            if board[y][x] == tile and board[y + 1][x + 1] == tile and board[y + 2][x + 2] == tile and board[y + 3][x + 3] == tile:
                return True

    # Ascending diagonal check
    for x in range(3, board_cols(board)):
        for y in range(board_rows(board) - 3):
            if board[y][x] == tile and board[y + 1][x - 1] == tile and board[y + 2][x - 2] == tile and board[y + 3][x - 3] == tile:
                return True

def is_connect3(board, player):
    '''Returns true if a player has achieved a Connect 3'''
    tile = player

    # Vertical check
    for x in range(board_cols(board)):
        for y in range(board_rows(board) - 2):
            if board[y][x] == tile and board[y + 1][x] == tile and board[y + 2][x] == tile:
                return True

    # Horizontal check
    for x in range(board_cols(board) - 2):
        for y in range(board_rows(board)):
            if board[y][x] == tile and board[y][x + 1] == tile and board[y][x + 2] == tile:
                return True

    # Descending diagonal check
    for x in range(board_cols(board) - 2):
        for y in range(board_rows(board) - 2):
            if board[y][x] == tile and board[y + 1][x - 1] == tile and board[y + 2][x - 2] == tile:
                return True

    # Ascending diagonal check
    for x in range(board_cols(board)-2):
        for y in range(2,board_rows(board)-2):
            if board[y][x] == tile and board[y + 1][x + 1] == tile and board[y + 2][x + 2] == tile:
                return True

    #change x and y

def is_connect2(board, player):

    '''Returns true if a player has achieved a Connect 2'''
    tile = player

    # Vertical check
    for x in range(board_cols(board)):
        for y in range(board_rows(board) - 1):
            if board[y][x] == tile and board[y + 1][x] == tile:
                return True

    # Horizontal check
    for x in range(board_cols(board) - 1):
        for y in range(board_rows(board)):
            if board[y][x] == tile and board[y][x + 1] == tile:
                return True

    # Descending diagonal check
    for x in range(board_cols(board) - 1):
        for y in range(board_rows(board) - 1):
            if board[y][x] == tile and board[y + 1][x - 1] == tile:
                return True

    # Ascending diagonal check
    for x in range(1, board_cols(board)-1):
        for y in range(board_rows(board) - 1):
            if board[y][x] == tile and board[y + 1][x + 1] == tile:
                return True
            

def is_game_over(board, player):
    '''Returns True if the game is over'''
    
    if is_win(board, player):
        return True

  
def is_tie(board):
    ''' Returns true if the board is full'''
    # Checks if the board is full
    for y in range(board_cols(board)): 
        for x in range(board_rows(board)):
            if board[x][y] == 0:
                return False
    return True
