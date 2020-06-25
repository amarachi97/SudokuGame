# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:22:50 2020

@author: User
"""
import pygame
import time
from pygame.locals import *
def get_system_fonts():
    fonts = pygame.font.get_fonts()
    print(len(fonts))
    for f in fonts:
        print(f)
      


#MAIN
pygame.init()

screen = pygame.display.set_mode((600,600))
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
#system fonts
#get_system_fonts()
running = True
text = ''

font = pygame.font.SysFont(None, 48)
img = font.render(text, True, white)

#define bounding rectangle
rect = img.get_rect() #the rectangle with be the dimensions of the text
rect.topleft = (20,20) #defining the topleft

#the cursor is essentially a very slim rectangle
cursor = pygame.Rect(rect.topright, (3, rect.height))

while running:
    try:
        all_events = pygame.event.get()
        for event in all_events:
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        if len(text) > 0:
                            text = text[:-1]
                            
                    else:
                        text += event.unicode 
                        print(type(event.unicode))
                
                    print(text)
                    #render again to uodate
        img = font.render(text, True, white)
        
        #resize rectangle
        rect.size = img.get_size()
        
        #update position of cursor
        cursor.topleft = rect.topright
            
            #else:
                
#                #create a font object
#                font = pygame.font.SysFont(None, 24) #args: font, size
#                
#                #render the object to an image
#                img = font.render('hello', True, blue)
#                
#                
#                rect = img.get_rect()
#                pygame.draw.rect(img, white, rect, 1)
#                
#                #blit the image
#                screen.blit(img, (20,20))
        #we ahve to fill background again before writing updated text
        screen.fill((0,0,0))
        screen.blit(img,rect)
        
        #blink cursor
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, blue, cursor)
        pygame.display.update()
    except Exception as e:
        print(e)
        pygame.quit()
        running = False
        
pygame.quit() 

