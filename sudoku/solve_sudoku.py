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


startTime = datetime.now()
runTime = 0
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
solve()

Description: this fucntioon uses this function 

"""
def solveHelper(grid):
    global result
    global startTime
    global runTime
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for input in range(1,10):
                    if (checkPossible(i,j,input, grid)):
                        grid[i][j] = input
                        solveHelper(grid)
                        grid[i][j]=0
                return
    #print (np.matrix(grid))
    result = np.copy(grid)
    #print(result)
    #startTime = datetime.now() - startTime
    runTime = datetime.now() - startTime
    
def solve(grid):
    global result
    global runTime
    solveHelper(grid)
    return result, runTime


#grid= np.array(game)
#solve(grid)
#print (np.matrix(result))
#print(startTime)
#print (checkPossible(1,1,8))

  
