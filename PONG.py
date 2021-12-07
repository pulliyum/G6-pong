import pygame
import sys
from pygame.locals import *
from CONSTANTS import *
from BALL import Ball
from PLAYER import *
from SCORE import *
from INPUT import handle_input
from LEVELS import level_menu, background_index, background_images
from AVATAR import *
from avatarselection2 import *
from avatarselection3 import *
from avatarselection4 import *



# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Create Screen to draw on
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Name that displays in top left of Window bar
pygame.display.set_caption('Group 6: PONG GAME')


# Game Objects
ball = Ball()
player1 = Player_1_2()
player2, player2.rect.x = Player_1_2(), 0
player3 = Player_3_4()
player4, player4.rect.y = Player_3_4(), 0

# Set Score
score1 = Score(screen, '0', SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
score2 = Score(screen, '0', SCREEN_WIDTH - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
score3 = Score(screen, '0', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
score4 = Score(screen, '0', SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT // 4)

X = 1280
Y = 1200
display_surface = pygame.display.set_mode((X, Y))


if num == 1:
    image = pygame.image.load('Avatar1.png')
if num == 2:
    image = pygame.image.load('Avatar2.png')
if num == 3:
    image = pygame.image.load('Avatar3.png')
if num == 4:
    image = pygame.image.load('Avatar4.png')
if num == 5:
    image = pygame.image.load('Avatar5.png')
if num == 6:
    image = pygame.image.load('Avatar6.png')

if num2 == 1:
    image2 = pygame.image.load('Avatar1.png')
if num2 == 2:
    image2 = pygame.image.load('Avatar2.png')
if num2 == 3:
    image2 = pygame.image.load('Avatar3.png')
if num2 == 4:
    image2 = pygame.image.load('Avatar4.png')
if num2 == 5:
    image2 = pygame.image.load('Avatar5.png')
if num2 == 6:
    image2 = pygame.image.load('Avatar6.png')

if num3 == 1:
    image3 = pygame.image.load('Avatar1.png')
if num3 == 2:
    image3 = pygame.image.load('Avatar2.png')
if num3 == 3:
    image3 = pygame.image.load('Avatar3.png')
if num3 == 4:
    image3 = pygame.image.load('Avatar4.png')
if num3 == 5:
    image3 = pygame.image.load('Avatar5.png')
if num3 == 6:
    image3 = pygame.image.load('Avatar6.png')

if num4 == 1:
    image4 = pygame.image.load('Avatar1.png')
if num4 == 2:
    image4 = pygame.image.load('Avatar2.png')
if num4 == 3:
    image4 = pygame.image.load('Avatar3.png')
if num4 == 4:
    image4 = pygame.image.load('Avatar4.png')
if num4 == 5:
    image4 = pygame.image.load('Avatar5.png')
if num4 == 6:
    image4 = pygame.image.load('Avatar6.png')

#menu
menu = False


# Game Loop
#--------------------------------------------------------------------------------------
while True:
    clock.tick(TICK_RATE)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[K_ESCAPE]:
            sys.exit()

    #menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                menu = False
            if event.key == pygame.K_l:
                menu = True
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_1 and menu:
                background_index = 0
                menu = False
            if event.key == pygame.K_2 and menu:
                background_index = 1
                menu = False
            if event.key == pygame.K_3 and menu:
                background_index = 2
                menu = False

    if menu:
        level_menu()
    else:
        handle_input(player1, player2, player3, player4)
        screen.blit(background_images[background_index], [0, 0])

        player1.draw(screen, BLUE)
        player2.draw(screen, RED)
        player3.draw(screen, GREEN)
        player4.draw(screen, PURPLE)
        display_surface.blit(image, (600, 0))
        display_surface.blit(image2, (0, 600))
        display_surface.blit(image3, (1210, 600))
        display_surface.blit(image4, (600, 1200))

        score1.show()
        score2.show()
        score3.show()
        score4.show()

        ball.draw(screen)
        ball.update(player1, player2, player3, player4,)



        if score1.score_player1(ball, player1):
            ball.reset()
        if score2.score_player2(ball, player2):
            ball.reset()
        if score3.score_player3(ball, player3):
            ball.reset()
        if score4.score_player4(ball, player4):
            ball.reset()

    pygame.display.flip()

pygame.quit()