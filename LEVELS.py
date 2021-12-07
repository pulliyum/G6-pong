import pygame
from CONSTANTS import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()
#Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Background

bgOne = pygame.image.load('default.png').convert()
bgOne = pygame.transform.scale(bgOne, (SCREEN_WIDTH, SCREEN_HEIGHT))

bgTwo = pygame.image.load('space.jpg').convert()
bgTwo = pygame.transform.scale(bgTwo, (SCREEN_WIDTH, SCREEN_HEIGHT))

bgThree = pygame.image.load('underground.jpg').convert()
bgThree = pygame.transform.scale(bgThree, (SCREEN_WIDTH, SCREEN_HEIGHT))

background_index = 0
background_images = [ bgOne, bgTwo, bgThree ]

#fonts
menu_font = pygame.font.Font('freesansbold.ttf', 65)
submenu_font = pygame.font.Font('freesansbold.ttf', 25)



def level_menu():
    # Menu Text
    global background_index
    s = pygame.Surface((560, 500))
    b = pygame.Surface((600, 520))
    s.fill((0,0,0))
    b.fill((255,255,255))
    screen.blit(b, (380, 0))
    screen.blit(s, (400, 0))
    pygame.display.set_caption('Level Selection')
    menu_text = menu_font.render("***Levels***", True, (255, 255, 255))
    screen.blit(menu_text, (450 , 50))
    menu_text = submenu_font.render("1. Default", True, (255, 255, 255))
    screen.blit(menu_text, (500 , 150))
    menu_text = submenu_font.render("2. Space", True, (255, 255, 255))
    screen.blit(menu_text, (500 , 200))
    menu_text = submenu_font.render("3. Underground", True, (255, 255, 255))
    screen.blit(menu_text, (500 , 250))