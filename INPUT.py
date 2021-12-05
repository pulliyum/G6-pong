import pygame
from pygame.locals import *


def handle_input(player1, player2, player3, player4):
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    # Player 1 Controls
    if keys[K_UP]:
        player1.move_up()
    if keys[K_DOWN]:
        player1.move_down()
    # Player 2 Controls
    if keys[K_w]:
        player2.move_up()
    if keys[K_s]:
        player2.move_down()
    # Player 3 Controls
    if keys[K_LEFT]:
        player3.move_left()
    if keys[K_RIGHT]:
        player3.move_right()
    # Player 4 Controls
    if keys[K_a]:
        player4.move_left()
    if keys[K_d]:
        player4.move_right()