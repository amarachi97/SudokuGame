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
        
    def create(self):
        self.swap()
        self.cipher()
        return self.game
            
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
            
        
    def cipher(self):
        nums = [1,2,3,4,5,6,7,8,9]
        random.shuffle(nums)
        
        for row in range(0,9):
            for col in range(0,9):
                if self.game[row][col] != 0:
                    self.game[row][col] = nums[self.game[row][col]-1]
                



