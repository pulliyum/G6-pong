import pygame
import sys
from pygame.locals import *
from CONSTANTS import *
from BALL import Ball
from PLAYER import *
from SCORE import *
from INPUT import handle_input
#from LEVELS import *
from AVATAR import *



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


# Game Loop
#--------------------------------------------------------------------------------------
while True:
    clock.tick(TICK_RATE)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[K_ESCAPE]:
            sys.exit()

    handle_input(player1, player2, player3, player4)
    screen.fill(GREY)

    player1.draw(screen, BLUE)
    player2.draw(screen, RED)
    player3.draw(screen, GREEN)
    player4.draw(screen, PURPLE)


    score1.show()
    score2.show()
    score3.show()
    score4.show()

    ball.draw(screen)
    ball.update(player1, player2, player3, player4)



    if score1.score_player1(ball):
        score1.earn_point()
        ball.reset()

    pygame.display.flip()

pygame.quit()