# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:49:25 2020

@author: User
"""

import pygame
from pygame.locals import *
import time
import numpy as np
import solve_sudoku as s
import create_sudoku as cr
import traceback
import math
import ctypes  # An included library with Python install.   


timer = [0,0,0,0]
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
EASY = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]

MEDIUM = [[0,0,0,0,0,9,8,0,0], 
        [0,1,8,4,0,0,0,2,0], 
        [0,0,4,0,7,0,0,0,0], 
        [0,0,0,0,0,6,0,0,0], 
        [6,0,0,0,0,0,0,5,0], 
        [0,0,0,1,8,0,7,0,2], 
        [0,5,1,8,0,0,0,9,3], 
        [9,7,0,0,3,0,0,0,4], 
        [0,3,0,0,6,0,0,0,0]]

HARD = [[4,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,9,0,0,0],
        [0,0,0,0,0,0,7,8,5],
        [0,0,7,0,4,8,0,5,0],
        [0,0,1,3,0,0,0,0,0],
        [0,0,6,0,7,0,0,0,0],
        [8,6,0,0,0,0,9,0,3],
        [7,0,0,0,0,5,0,6,2],
        [0,0,3,7,0,0,0,0,0]]
    
game = EASY
game_played = np.copy(game)
class Game:
    """
    __init__(self)
    
    Description: sets the width, height and the space at the bottom for time displayed.
                 This also sets the screen
    """
    def __init__(self):
        pygame.display.set_caption("Sudoku")
        self.width = 540
        self.height = 540
        self.space = 40
        self.screen = pygame.display.set_mode((self.width, self.height+self.space))
        
    def pick_game(self):
        global game
        global game_played
        
        print("Enter your level of difficulty")
        print("1: Easy")
        print("2: Medium")
        print("3: Hard")
        option = int (input("Enter desired option: "))
        if option == 1:
            make = cr.Create(EASY)
            game = make.create()
            
        if option == 2:
            make = cr.Create(MEDIUM)
            game = make.create()
            
        if option == 3:
            make = cr.Create(HARD)
            game = make.create()
            
        game_played = np.copy(game)
    
    
    """
    start_game(self)
    
    Description: this function starts the game and handles all the events that occur during the game
    """
    def start_game(self):
        global RED
        global BLACK
        global game
        global game_played
        pygame.init()
        
        
        text=""
        solvedtimeText = ""
        font = pygame.font.SysFont("ebrima.ttc", 24)
        textImg = font.render(text, True, RED)
        rect = textImg.get_rect()
        rect.topleft = (20,20)
        cursor = pygame.Rect(rect.topright, (3, rect.height))
        valid_nums = "123456789"
        running = True
        pos = (0,0)
        running = True
        solved = False
        
        while running:
            self.screen.fill((255,255,255))

            try:
                all_events = pygame.event.get()
                for event in all_events:
                    if event.type == pygame.QUIT:
                        running = False
                        
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        rect.center = pos
                        
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if len(text) > 0:
                                text = text[:-1]
                        elif event.unicode in valid_nums:
                            text += event.unicode
                        elif event.key == pygame.K_RETURN:
                            row = int (pos[1]/(self.width//9))
                            col = int (pos[0]/(self.height//9))
                            entry = int (text)
                            if entry > 0 and entry < 10:
                                if s.checkPossible(row, col, entry, game_played):
                                    game_played[row][col] = entry
                                    text = ""
                        elif event.key == pygame.K_d:
                            row = int (pos[1]/(self.width//9))
                            col = int (pos[0]/(self.height//9))
                            game_played[row][col] = 0
                            text = ""
                            
                        elif event.key == pygame.K_s:
                            result, runTime = s.solve(np.array(game))
                            if (result == game_played).all():
                                ctypes.windll.user32.MessageBoxW(0, "YOU WON!!", "Game Status", 1)
                            game_played = np.copy(result)
                            print(game_played)
                            solvedtimeText = "Solve Time: " + runTime
                            solved = True
             
                if solved:
                    currentTime = "00:00"
                else:
                    currentTime = self.get_time()
                
                #render the computer solved time
                solvedtimeImg = font.render(solvedtimeText, True, BLACK)
                solvedtime_rect = solvedtimeImg.get_rect()
                solvedtime_rect.bottomright = (self.width-40, self.height+self.space - 5)
                 
                #render the timer
                timerImg = font.render(currentTime, True, BLACK)
                timer_rect = timerImg.get_rect()
                timer_rect.bottomleft = (5, self.height+self.space - 5)
            
                
                #render the entered text
                textImg = font.render(text, True, RED)
                rect.size = textImg.get_size()
                cursor.topleft= rect.topright
             
                
                self.screen.blit(textImg, rect)
                self.screen.blit(timerImg, timer_rect)
                self.screen.blit(solvedtimeImg, solvedtime_rect)
                self.draw_board()
                self.insert_nums()
                
                #blink cursor
                if time.time() % 1 > 0.5:
                    pygame.draw.rect(self.screen, BLACK, cursor)
            except Exception as e:
                print(e)
                traceback.print_stack()
                break
                
            pygame.display.update()
                    
        pygame.display.quit()   
        
    """
    draw_board(self)
    
    Description: draws the board during the course of the execution
    
    """
    def draw_board(self):
        global BLACK
        #horizontal lines
        line_count = 0
        for y in range(0, self.width+1, self.width//9):
            if line_count % 3 == 0 and line_count != 0:
                pygame.draw.line(self.screen, BLACK, (0, y), (self.width, y), 2)
            pygame.draw.line(self.screen, BLACK, (0, y), (self.width, y))
            line_count +=1
            
        #vertical lines
        line_count = 0
        for x in range(0, self.height, self.height//9):
            if line_count %3 == 0 and line_count != 0:
                pygame.draw.line(self.screen, BLACK, (x, 0), (x, self.height), 2)
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, self.height))
            line_count += 1
            
        
    """
    insert_nums(self)
    
    Description: inserts the numbers in the empty space when entered by the user
    
    """    
    def insert_nums(self):
        global game
        global game_played
        global BLUE
        global BLACK
        font = pygame.font.SysFont('ebrima.ttc', 24)
        start = (self.height//9) // 2
        for y in range(start, self.height, self.height//9):
            row = (y-start) //(self.height//9)
            for x in range(start, self.width, self.width//9):
                col = (x-start) //(self.width//9)
                if (game[row][col] != 0):
                    img = font.render(str(game[row][col]), True, BLACK)
                    self.screen.blit(img, (x,y))
                elif game_played[row][col] != 0:
                    img = font.render(str(game_played[row][col]), True, BLUE)
                    self.screen.blit(img, (x,y))


    """
    get_time(self)
    
    Description: updates the clock/timer at the bottom of the window
    
    returns the calculated time
    """
    def get_time(self):
           timer[3] += 1
           timer[0] = math.floor((timer[3] / 100) / 60);
           timer[1] = math.floor((timer[3] / 100) - (timer[0] * 60))
           timer[2] = math.floor(timer[3] - (timer[1] * 100))
           
           return self.leadingZero(timer[0]) + ":" + self.leadingZero(timer[1])
       
    """
    leadingZero(self)
    
    Description: adds a leading zero to the time displayed
    
    """
    def leadingZero(self, num):
        if num < 10:
            return "0" + str(num)
        return str(num)
           

        
#MAIN
start = Game()
start.pick_game()
start.start_game()