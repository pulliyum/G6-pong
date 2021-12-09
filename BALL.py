import pygame
import random
from CONSTANTS import *
from PLAYER import *


class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = 10
        self.SPEED = 7
        self.vx = self.SPEED
        self.vy = self.SPEED

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_GREY, (self.x, self.y), self.radius)

    def update(self, player1, player2, player3, player4):
        self.x += self.vx
        self.y += self.vy

# Last Player to Hit the Ball before it goes offscreen Scores
# ---------------------------------------------------------------------------------------------
        if self.y > SCREEN_HEIGHT - self.radius * 2 or self.y < self.radius * 2:
            self.vy *= -1
            if player1.last:
                player1.score()
                player1.last = False
            if player2.last:
                player2.score()
                player2.last = False
            if player3.last:
                player3.score()
                player3.last = False
            if player4.last:
                player4.score()
                player4.last = False
            self.reset()

        if self.x > SCREEN_WIDTH - self.radius * 2 or self.x < self.radius * 2:
            self.vx *= -1
            if player1.last:
                player1.score()
                player1.last = False
            if player2.last:
                player2.score()
                player2.last = False
            if player3.last:
                player3.score()
                player3.last = False
            if player4.last:
                player4.score()
                player4.last = False
            self.reset()
 # ---------------------------------------------------------------------------------------------


# Print in Terminal Last Player to Hit the Ball
# ---------------------------------------------------------------------------------------------
        # Collision
        if self.get_rect().colliderect(player1):
            self.vx *= -1
            print(" Player 1 Hit Last!")
            player1.last = True
            player2.last = False
            player3.last = False
            player4.last = False
        if self.get_rect().colliderect(player2):
            self.vx *= -1
            print("Player 2 Hit Last!")
            player1.last = False
            player2.last = True
            player3.last = False
            player4.last = False
        if self.get_rect().colliderect(player3):
            self.vy *= -1
            print("Player 3 Hit Last!")
            player1.last = False
            player2.last = False
            player3.last = True
            player4.last = False
        if self.get_rect().colliderect(player4):
            self.vy *= -1
            print("Player 4 Hit Last!")
            player1.last = False
            player2.last = False
            player3.last = False
            player4.last = True
# ---------------------------------------------------------------------------------------------

    # Reset ball to center of screen
    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.start()

    # Start the Ball in motion in random direction
    def start(self):
        self.vx *= random.choice((1, -1))
        self.vy *= random.choice((1, -1))
