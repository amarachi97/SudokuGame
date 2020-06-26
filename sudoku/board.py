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
pygame.init()

def draw_board():
    #horizontal lines
    line_count = 0
    for i in range(0, width, width//9):
        #++line_count
        if line_count % 3 == 0 :
            pygame.draw.line(screen, BLACK, (0, i), (width, i), 2)
        pygame.draw.line(screen, BLACK, (0, i), (width, i))
        line_count +=1
        
    #vertical lines
    line_count = 0
    for j in range(0, height, height//9):
        if line_count %3 == 0:
            pygame.draw.line(screen, BLACK, (j, 0), (j, height), 2)
        pygame.draw.line(screen, BLACK, (j, 0), (j, height))
        line_count += 1
        
    
    
def insert_nums():
    global game
    fontCurr = pygame.font.SysFont('ebrima.ttc', 24)
    start = (height//9) // 2
    for y in range(start, height, height//9):
        row = (y-start) //(height//9)
        for x in range(start, width, width//9):
            col = (x-start) //(width//9)
            if (game[row][col] != 0):
                img = fontCurr.render(str(game[row][col]), True, BLACK)
                screen.blit(img, (x,y))
            elif game_played[row][col] != 0:
                img = fontCurr.render(str(game_played[row][col]), True, BLUE)
                screen.blit(img, (x,y))

    

game = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]
game_played = np.array(game)
width = 540
height = 540
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")

text=""
font = pygame.font.SysFont("ebrima.ttc", 24)
textImg = font.render(text, True, RED)
rect = textImg.get_rect()
rect.topleft = (20,20)
cursor = pygame.Rect(rect.topright, (3, rect.height))
nums = "123456789"
running = True
pos = (0,0)
while running:
    screen.fill((255,255,255))
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
                elif event.unicode in nums:
                    text += event.unicode
                elif event.key == pygame.K_RETURN:
                    print(pos)
                    row = int (pos[1]/(width//9))
                    col = int (pos[0]/(height//9))
                    print(row, col)
                    if s.checkPossible(row, col, int(text), game_played):
                        game_played[row][col] = int (text)
                        text = ""
                        print(game_played)
                elif event.key == pygame.K_d:
                    row = int (pos[1]/(width//9))
                    col = int (pos[0]/(height//9))
                    game_played[row][col] = 0
                    text = ""
                    
        textImg = font.render(text, True, RED)
        rect.size = textImg.get_size()
        cursor.topleft= rect.topright
     
        
        screen.blit(textImg, rect)
        draw_board()
        insert_nums()
        
        #blink cursor
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, BLACK, cursor)
    except Exception as e:
        print(e)
        pass
        
    pygame.display.update()
            
pygame.display.quit()           

    
