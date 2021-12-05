from BALL import *
from PLAYER import *


class Score:
    def __init__(self, screen, points, x, y):
        self.screen = screen
        self.points = points
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("freesansbold.ttf", 60, bold=True)
        self.label = self.font.render(self.points, 0, LIGHT_GREY)
        self.show()

    def show(self):
        self.screen.blit(self.label, (self.x - self.label.get_rect().width // 2, self.y))

    def score_player1(self, ball):
        return ball.x - ball.radius >= SCREEN_WIDTH

    def score_player2(self, ball):
        return ball.x - ball.radius <= 0

    def earn_point(self):
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.render(self.points, 0, LIGHT_GREY)

