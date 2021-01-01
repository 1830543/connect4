"""
Jericho Adalin and Quang Loc Tran
420-LCU Computer Programming, Section 2
Thursday, May 28
R. Vincent, instructor
Final Project
"""

""" Implementation of the graphical user interface
    for the game connect FOUR """

import tkinter as tk
from board import *
from game import *
from tkinter import messagebox


YELLOW="#FFD700"
RED='red'
GAP=20
WIDTH=840
HEIGHT=720
players = [HUMAN, COMPUTER]
DIFFICULTY=0
root=tk.Tk()
root.title("Connect Four")
canvas=tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1E90FF") #creates canvas

xr=(WIDTH//7)  #Creates rectangle borders
for i in range(7):
    x0=xr*i
    x1= x0+xr
    y0=0
    y1=HEIGHT
    canvas.create_rectangle(x0,y0,x1,y1)
    
    
canvas.pack()


    
    
    
def click(event):
    ''' Handles a left click event, '''
    x=canvas.canvasx(event.x)
    col=int(x/120) #Locates click within the rectangles
    game_turn(board,col)
    draw_board(board) #Update the board

    if is_game_over(board, 1):
        message = "Player 1 wins!"
        messagebox.showinfo('Game over', message)
        root.destroy()

    elif is_game_over(board, 2):
        message = "Player 2 wins!"
        messagebox.showinfo('Game over', message)
        root.destroy()

    for a in players: #Checks for a tie
        if not is_game_over(board, a):
            if is_tie(board):
                message = "Game Tie"
                messagebox.showinfo('Game Over')
                root.destroy()


    

canvas.bind('<Button-1>', click)

def draw_board(board): #Creates the board in tkinter
    piece_colors= {HUMAN: RED, COMPUTER: YELLOW}

    for item in canvas.find_withtag('piece'):
        canvas.delete(item)
    for row in range(6):
        for col in range(7):
            player=board_get(board, row, col)
            y= row* 120
            x= col* 120
            if player !=0:
                color = piece_colors[player]
            else:
                color='white'
            canvas.create_oval(x + 100, y + 100,x+25,y+25,fill=color,tag = 'piece')

    

board=game_start()
draw_board(board)
root.mainloop()

