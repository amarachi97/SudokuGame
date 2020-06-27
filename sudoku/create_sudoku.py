# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:41:50 2020

@author: User
"""
import numpy as np
import random
import solve_sudoku as s

class Create:
    game = np.zeros(shape=(9,9), dtype=int)
    
    def __init__(self, g):
        g = np.array(g)
        self.game = np.copy(g)
        print(self.game)
        
    def create(self):
        #print("here")
        self.swap()
       # print(self.game)
        self.blank_out()
        print(self.game)
        return self.game
        #solved_game, time = s.solve(self.game)
        #print("Solved game")
        #print(solved_game)
        
        #print("Time: ", time)
            
    def swap(self):
        for i in range(5):  #half of the grid    
            #get opposite column
            opp = len(self.game) - i - 1
            
            #swap columns
            temp = np.copy(self.game[:,opp])
            self.game[:,opp] = self.game[:,i]
            self.game[:,i] = temp

            
            #swap rows
            temp = np.copy(self.game[i])
            self.game[i] = self.game[opp]
            self.game[opp] = temp
            
    def blank_out(self):
        for i in range(60):
            row= random.randint(0,8)
            col = random.randint(0,8)
            
            opp_row = len(self.game) - row - 1
            opp_col = len(self.game) - col - 1
            
#            print(row)
#            print(col)
#            print(opp_row)
#            print(opp_col)
            self.game[row,col] = 0
            self.game[opp_row, opp_col] = 0
            
        
solved_game_easy = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]]

solved_game_hard = [
        [4,5,2,6,8,7,3,1,9],
        [3,7,8,1,5,9,4,2,6],
        [6,1,9,4,2,3,7,8,5],
        [2,3,7,9,4,8,6,5,1],
        [5,4,1,3,6,2,8,9,7],
        [9,8,6,5,7,1,2,3,4],
        [8,6,5,2,1,4,9,7,3],
        [7,9,4,8,3,5,1,6,2],
        [1,2,3,7,9,6,5,4,8]]


#a = Create(solved_game_hard)
#a.create()


