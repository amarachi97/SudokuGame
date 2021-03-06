# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:32:51 2020

@author: User
"""

"""
checkPossible (r, c, num)

r (type: int) --> row
c (type: int) --> column
num (type: int) --> number you wish check if possible in (r,c) of the grid

Description: To check if a number is possible, you see if they are present
in that row, column and square (3x3)

returns True if possible
return False otherwise
"""
import numpy as np
from datetime import datetime

#startTime = 0
runTime = ""
result = np.zeros(shape=(9,9), dtype=int) 
def checkPossible(r, c, num, grid):
    #ROW
    if (num in grid[r]):
        #print("row")
        return False
    
    #COLUMN
    if (num in grid[:,[c]]):
        #print("col")
        return False
    
    #SQUARE
    #to see which square they are in
    x = r // 3
    y = c // 3

    x*=3
    y*=3
    
    #add three steps right and three steps down
    for i in range(x, x+3):
        for j in range (y, y+3):
            if grid[i][j] == num:
                #print("box")
                return False

    return True

"""
solveHelper()

Description: solves the sudoku 

"""
def solveHelper(grid, startTime):
    global result
    #global startTime
    global runTime
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for input in range(1,10):
                    if (checkPossible(i,j,input, grid)):
                        grid[i][j] = input
                        solveHelper(grid, startTime)
                        grid[i][j]=0
                        
                return
    result = np.copy(grid)
    endTime = datetime.now()
    runTime = leadingZero(endTime.hour - startTime.hour) + ":" + leadingZero(endTime.minute - startTime.minute) + ":" + leadingZero(endTime.second - startTime.second) + "." + str(endTime.microsecond - startTime.microsecond)

"""
solve()

Description: sets the start time and sends the grid to the solveHelper function

"""
def solve(grid):
    global result
    global runTime
    startTime = datetime.now()
    solveHelper(grid, startTime)
    return result, runTime

def leadingZero(num):
    if num < 10:
        return "0" + str(num)
    return str(num)



  
