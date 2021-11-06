import pygame
import sys

#   Initializing pygame
pygame.init()
clock = pygame.time.Clock()

#   Main Game Window
#   MAIN MENU WILL GO IN THIS BLOCK
#--------------------------------------------
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Main Menu')


#---------------------------------------------

#   Player Avatar Selection Window
#   PLEASE PLACE AVATAR SELECTION IN THIS BLOCK
#--------------------------------------------
pygame.display.set_caption('Player Selection')


#---------------------------------------------

#   Game Board Selection Window
#   PLEASE PLACE GAME BOARD SELECTION IN THIS BLOCK
#--------------------------------------------
pygame.display.set_caption('Level Selection')


#---------------------------------------------



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
