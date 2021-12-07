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

    def score_player1(self, ball, player):
        if player.last_hit(ball):
            print("Player 1 Hit Last!")
            # Score in Player 2 Goal
            if ball.x - ball.radius <= 0:
                print("P1 SCORE ON LEFT!")
                self.earn_point()
            # Score in Player 3 Goal
            if ball.y < ball.radius <= 0:
                print("P1 SCORE ON RIGHT!")
                self.earn_point()
            # Score in Player 4 Goal
            if ball.y - ball.radius >= SCREEN_HEIGHT:
                print("P1 SCORE ON TOP!")
                self.earn_point()

    def score_player2(self, ball, player):
        if player.last_hit(ball):
            print(" Player 2 Hit Last!")
            # Score in Player 1 Goal
            if ball.x - ball.radius >= SCREEN_WIDTH:
                self.earn_point()
            # Score in Player 3 Goal
            if ball.y < ball.radius <= 0:
                self.earn_point()
            # Score in Player 4 Goal
            if ball.y - ball.radius >= SCREEN_HEIGHT:
                self.earn_point()

    def score_player3(self, ball, player):
        if player.last_hit(ball):
            print("Player 3 Hit Last!")
            # Score in Player 1 Goal
            if ball.x - ball.radius >= SCREEN_WIDTH:
                self.earn_point()
            # Score in Player 2 Goal
            if ball.x - ball.radius <= 0:
                self.earn_point()
            # Score in Player 4 Goal
            if ball.y - ball.radius >= SCREEN_HEIGHT:
                self.earn_point()

    def score_player4(self, ball, player):
        if player.last_hit(ball):
            print("Player 4 Hit Last!")
            if ball.reset:
                print("point calculating.....")
                self.earn_point()
                print("earn point called")
                self.label = self.font.render(self.points, 0, LIGHT_GREY)
                print("point displayed!")

    def earn_point(self, player):
        if player.score:
            print("player scored!")
            points = int(self.points) + 1
            self.points = str(points)
            self.label = self.font.render(self.points, 0, LIGHT_GREY)
            player.score = False