"""
    The Space Game: Haven't thought of a name yet!
    This is a project game built using pygame and pymunk.
    The contest held by IIT Bombay, 1st best technical institute of India!
    Bah, praising them ain't going to get me anywhere! 

"""
#Importing modules start here!
#----------------------------
import pygame #pip3 install pygame / pip install pygame
import pymunk #pip3 install pymunk / pip install pymunk
import os 
#Importing modules end here!
#---------------------------

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    while True:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
