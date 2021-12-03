import pygame
import sys
import random

#Initializing pygame
pygame.init()
clock = pygame.time.Clock()

#Screen Dimension
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

#Colors
bg_color = pygame.Color('grey12')
red = (230, 70, 75)
green = (110, 190, 5)
blue = (30, 95, 205)
purple = (120, 65, 170)
grey = (200, 200, 200)


#Game Objects
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
ball_speed_x = 8 * random.choice((1, -1))
ball_speed_y = 8 * random.choice((1, -1))

#Players
#pygame.Rect( *position on screen* x, y, *size of player* x, y)
#--------------------------------------------
#Player ONE
player_one_speed = 0
player_one = pygame.Rect(screen_width - 100, screen_height/2 - 70, 30, 140)

#Player TWO
player_two_speed = 0
player_two = pygame.Rect(100, screen_height/2 - 70, 30, 140)

#Player THREE
player_three_speed = 15
player_three = pygame.Rect(screen_width/2 - 70, 100, 140, 30)

#Player FOUR
player_four_speed = 15
player_four = pygame.Rect(screen_width/2 - 70, screen_height- 100, 140, 30)
#--------------------------------------------







#Game Functions
#--------------------------------------------
def ball_movement():
    #Ball speed
    global ball_speed_x
    global ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_reset()
    if ball.left <= 0 or ball.right >= screen_width:
        ball_reset()

    #Collision
    if ball.colliderect(player_one) or ball.colliderect(player_two):
        ball_speed_x *= -1
    if ball.colliderect(player_three) or ball.colliderect(player_four):
        ball_speed_y *= -1

def ball_reset():
    #Reset ball to center after point scored
    global ball_speed_x
    global ball_speed_y
    ball.center = (screen_width/2 -15, screen_height/2 -15)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))



def player_movement():
    player_one.y += player_one_speed
    if player_one.top <= 0:
        player_one.top = 0
    if player_one.bottom >= screen_height:
        player_one.bottom = screen_height

    player_two.y += player_two_speed
    if player_two.top <= 0:
        player_two.top = 0
    if player_two.bottom >= screen_height:
        player_two.bottom = screen_height

def computer_movement():



    #Player THREE
    if player_three.left <= ball.x:
        player_three.left += player_three_speed
    if player_three.right >= ball.x:
        player_three.right -= player_three_speed

    if player_three.top <= 0:
        player_three.top = 0
    if player_three.bottom >= screen_height:
        player_three.bottom = screen_height

    #Player FOUR
    if player_four.left <= ball.x:

        player_four.left += player_four_speed
    if player_four.right >= ball.x:
        player_four.right -= player_four_speed

    if player_four.top <= 0:
        player_four.top = 0
    if player_four.bottom >= screen_height:
        player_four.bottom = screen_height

#--------------------------------------------



#Main Game Window
#MAIN MENU WILL GO IN THIS BLOCK
#--------------------------------------------
pygame.display.set_caption('Main Menu')


#---------------------------------------------

#Player Avatar Selection Window
#PLEASE PLACE AVATAR SELECTION IN THIS BLOCK
#--------------------------------------------
pygame.display.set_caption('Player Selection')


#---------------------------------------------

#Game Board Selection Window
#PLEASE PLACE GAME BOARD SELECTION IN THIS BLOCK
#--------------------------------------------
pygame.display.set_caption('Level Selection')


#---------------------------------------------


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.set_caption('Group 6: PONG GAME')

        #When key is PRESSED...
        if event.type == pygame.KEYDOWN:
            #Player ONE Controls
            if event.key == pygame.K_DOWN:
                player_one_speed += 15
            if event.key == pygame.K_UP:
                player_one_speed -= 15

            #Player TWO Controls
            if event.key == pygame.K_s:
                player_two_speed += 15
            if event.key == pygame.K_w:
                player_two_speed -= 15

        #When key is RELEASED...
        if event.type == pygame.KEYUP:
            #Player ONE Controls
            if event.key == pygame.K_DOWN:
                player_one_speed -= 15
            if event.key == pygame.K_UP:
                player_one_speed += 15

            #Player TWO Controls
            if event.key == pygame.K_s:
                player_two_speed -= 15
            if event.key == pygame.K_w:
                player_two_speed += 15



    ball_movement()
    player_movement()
    computer_movement()




    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, red, player_one)
    pygame.draw.rect(screen, purple, player_two)
    pygame.draw.rect(screen, blue, player_three)
    pygame.draw.rect(screen, green, player_four)
    pygame.draw.ellipse(screen, grey, ball)
    pygame.draw.aaline(screen, grey, (screen_width / 2, 0), (screen_width / 2, screen_height))


    #Update window
    pygame.display.flip()
    clock.tick(60)
