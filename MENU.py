import pygame
import sys
import pygame_menu
from pygame.locals import *
from CONSTANTS import *
from BALL import Ball
from PLAYER import *
from SCORE import *
from INPUT import handle_input
import json



# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Create Screen to draw on
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Name that displays in top left of Window bar
pygame.display.set_caption('Group 6: PONG GAME')


# Start NEW game
def start_game():

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

    while True:

        clock.tick(TICK_RATE)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[K_ESCAPE]:

		# Save game data on Quit/Exit
                data = {
                    'player1': score1.points,
                    'player2': score2.points,
                    'player3': score3.points,
                    'player4': score4.points
                }
                with open('save_data.JSON', 'w') as save_file:
                    json.dump(data, save_file)
                pygame.quit()
                sys.exit()

            if keys[K_TAB]:
		# Save game data when accessing Menu
                data = {
                    'player1': score1.points,
                    'player2': score2.points,
                    'player3': score3.points,
                    'player4': score4.points
                }
                with open('save_data.JSON', 'w') as save_file:
                    json.dump(data, save_file)
                main_menu(screen)


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

# Continue with a saved game
def load_game():

# Open save file and import scores to data dictionary
    with open('save_data.JSON') as save_file:
        data = json.load(save_file)

        # Game Objects
        ball = Ball()
        player1 = Player_1_2()
        player2, player2.rect.x = Player_1_2(), 0
        player3 = Player_3_4()
        player4, player4.rect.y = Player_3_4(), 0

        # Set Scores to values corresponding to player key in the data dictionary from the save file
        score1 = Score(screen, data['player1'], SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        score2 = Score(screen, data['player2'], SCREEN_WIDTH - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        score3 = Score(screen, data['player3'], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        score4 = Score(screen, data['player4'], SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT // 4)

    while True:

        clock.tick(TICK_RATE)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[K_ESCAPE]:
		# Saves scores on quit/exit
                data = {
                    'player1': score1.points,
                    'player2': score2.points,
                    'player3': score3.points,
                    'player4': score4.points
                }
                with open('save_data.JSON', 'w') as save_file:
                    json.dump(data, save_file)
                pygame.quit()
                sys.exit()

            if keys[K_TAB]:
		# Saves scores on opening Menu
                data = {
                    'player1': score1.points,
                    'player2': score2.points,
                    'player3': score3.points,
                    'player4': score4.points
                }
                with open('save_data.JSON', 'w') as save_file:
                    json.dump(data, save_file)
                main_menu(screen)

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

def main_menu(screen):

    menu = pygame_menu.Menu('Menu', 400, 300, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Start Game', start_game)
    menu.add.button('Continue', load_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

main_menu(screen)
