# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:49:25 2020

@author: User
"""

import pygame
from pygame.locals import *
import time
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
    fontCurr = pygame.font.SysFont('ebrima.ttc', 24)
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
    
    start = (height//9) // 2
    for y in range(start, height, height//9):
        row = get_row(y)
        #print("y:", y)
        for x in range(start, width, width//9):
            col = get_col(x)
            if (game[row][col] != 0):
                img = fontCurr.render(str(game[row][col]), True, BLACK)
                #print("x:", x)
                screen.blit(img, (x,y))
        #print()
        
def get_row(y):
    start = (height//9) // 2
    return (y-start) //(height//9)

def get_col(x):
    start = (width//9) // 2
    return (x-start) //(width//9)


width = 540
height = 540
BLACK = (0,0,0)
RED = (255,0,0)
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
while running:
    try:
        all_events = pygame.event.get()
        for event in all_events:
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                row = get_row(pos[1])
                col = get_col(pos[0])
                print(row, col)
                rect.center = pos
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]
                elif event.unicode in nums:
                    text += event.unicode
        textImg = font.render(text, True, RED)
        rect.size = textImg.get_size()
        cursor.topleft= rect.topright
     
        
    
    
    
        screen.fill((255,255,255))
        draw_board()
        insert_nums()
        screen.blit(textImg, rect)
        #blink cursor
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, BLACK, cursor)
    except Exception as e:
        print(e)
        pass
        #insert_nums()
        
    pygame.display.update()
            
pygame.display.quit()           

    
