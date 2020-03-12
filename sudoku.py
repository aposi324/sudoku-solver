# Author: Alexander Posipanko
# Description: Recursive sudoku solver. No GUI or input for now.
# Creation Date: 2/5/2020
# Last Edited: 2/5/2020

from array import *
from graphics import *
from Board import *
import pprint
import math

def main():

    win = GraphWin("Sudoku Solver", 400, 400)
   
    board = Board()
    draw(win, board)
    input()
    board = [   [6,0,7,4,1,0,0,9,0],
                [0,1,0,3,9,0,6,0,0],
                [0,9,0,6,2,0,0,0,5],
                [2,0,0,7,5,1,0,8,3],
                [7,0,0,8,3,9,0,6,4],
                [0,8,3,2,0,0,0,5,1],
                [1,7,0,5,4,2,0,3,9],
                [0,4,0,9,8,0,1,7,0],
                [8,3,9,0,7,6,5,4,0]
            ]
    pos = [0,0]
    print("Original Board: ")
    print("====================================")
    print_board(board)
    sol = solve(board,pos)

    print("Solved Board: ")
    print("====================================")
    print_board(board)



def solve(board, pos):
    #If we already have a number here, it stays
    if board[pos[0]][pos[1]] != 0:
        return solve(board, next_position(pos))
    

    options = get_options(board, pos)

    # Try all legal options
    while len(options) > 0:
        val = options.pop() #Take first option off of list
        board = place_num(board, pos, val) 
        if pos[0]*9+pos[1] >= (9*9-1) or solve(board, next_position(pos)): # Escape if the board is solved
            return 1

    
    #We're out of options; not the right path to go down
    place_num(board, pos, 0) #Return the board to the state it was in before entering the function and return to go down another path

    return 0

# Find the next board position
def next_position(pos):
    tPos = pos[0]*9 + pos[1] +1;
    newpos = [0,0]
    newpos[0] = int(tPos / 9)
    newpos[1] = tPos % 9
    return newpos

# Display the board to the terminal
def print_board(board):
    #print("----------------------")
    pp = pprint.PrettyPrinter()
    pp.pprint(board)
    print("")


# Function to get the legal numbers for a spot
def get_options(board, pos):
    options = list(range(1,10))
    #strike out any options already present in the row
    for i in range(0,9):
        val = board[pos[0]] [i]

        #If the value in the current index exists in our option list, remove it
        if val in options:
            options.remove(val)



    #strike out any options already present in the column
    for i in range(0,9):
        val = board [ i ][ pos[1] ]

        # If the value in the current index exists in our option list, remove it
        if val in options:
            options.remove(val)


    #strike out any options already present in the local box
    box_start_x = math.floor(pos[1]/3)*3
    box_start_y = math.floor(pos[0]/3)*3

    for i in range(box_start_y, box_start_y+3):
        for j in range(box_start_x, box_start_x+3):
            val = board[i][j]

            # If the value in the current index exists in our option list, remove it
            if val in options: 
                options.remove(val)
                
    return options

def place_num(board, pos, val):
    board[pos[0]][pos[1]] = val
    return board

def draw(window, board):
    print("hiyo")

  
    margin = 50
    for i in range(0, 3):
        for j in range(0, 3):
            currX = i*100
            currY = j *100
            #rect = Rectangle(Point(currX+margin, currY+margin), Point(currX+100+margin, currY+100+margin))
            #rect.draw(window)
            draw_bold_box(window,currX+margin, currY+margin)

def draw_bold_box(window, x, y):
    thickness = 3
    for i in range(0, thickness):
        rect = Rectangle(Point(x+i,y+i), Point(x+(100+i), y+(100+i)))
        rect.draw(window)


if __name__ == '__main__':
    main()