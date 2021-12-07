import pygame
import random
from CONSTANTS import *


class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = 10
        self.SPEED = 7
        self.vx = self.SPEED
        self.vy = self.SPEED
        self.reset = False

    def get_rect(self):
        return pygame.Rect(
            self.x, self.y, self.radius * 2, self.radius * 2
        )

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_GREY, (self.x, self.y), self.radius)

    def update(self, player1, player2, player3, player4):
        self.x += self.vx
        self.y += self.vy
        self.reset = False

        if self.y > SCREEN_HEIGHT - self.radius * 2 or self.y < self.radius * 2:
            self.vy *= -1
            self.reset = True
            self.start()

        if self.x > SCREEN_WIDTH - self.radius * 2 or self.x < self.radius * 2:
            self.vx *= -1
            self.reset = True
            self.start()

        # Collision
        if self.get_rect().colliderect(player2) or self.get_rect().colliderect(player1):
            self.vx *= -1

        if self.get_rect().colliderect(player3) or self.get_rect().colliderect(player4):
            self.vy *= -1

    # Reset ball to center of screen
    def reset(self):
        self.reset = True
        self.start()



    def start(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.vx *= random.choice((1, -1))
        self.vy *= random.choice((1, -1))
        self.reset = False



