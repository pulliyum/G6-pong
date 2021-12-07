import pygame


# to initalize python
pygame.init()

# to make the window and have its hight and width be 800 and 600
screen = pygame.display.set_mode((1280, 960 ))

# background
background = pygame.image.load('4290766.jpg')

myFont = pygame.font.SysFont("fontselection", 40)
#  font color
color = (0, 0, 0)

# Title and Icon
pygame.display.set_caption("Select an Avatar")


# players
playerImg1 = pygame.image.load('Avatar1.png').convert_alpha()


playerImg2 = pygame.image.load('Avatar2.png').convert_alpha()


playerImg3 = pygame.image.load('Avatar3.png').convert_alpha()


playerImg4 = pygame.image.load('Avatar4.png').convert_alpha()


playerImg5 = pygame.image.load('Avatar5.png').convert_alpha()


playerImg6 = pygame.image.load('Avatar6.png').convert_alpha()


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# create button instances on images
avatar1 = Button(200, 100, playerImg1)
avatar2 = Button(300, 100, playerImg2)
avatar3 = Button(400, 100, playerImg3)
avatar4 = Button(200, 200, playerImg4)
avatar5 = Button(300, 200, playerImg5)
avatar6 = Button(400, 200, playerImg6)

n = 0;
# Game loop  that makes sure the game is always running and window doesnt close down
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB is what the numbers represent for background color
    screen.fill((255, 255, 255))

    # background image
    screen.blit(background, (-130, -130))
    text1 = myFont.render("Select An Avatar Player 2", 1, color)
    screen.blit(text1, (200, 50))
    if avatar1.draw():
        print("avatar1")
        num2 = 1
        exec(open('avatarselection3.py').read())

    if avatar2.draw():
        print("avatar2")
        num2 = 2
        exec(open('avatarselection3.py').read())
    if avatar3.draw():
        print("avatar3")
        num2 = 3
        exec(open('avatarselection3.py').read())
    if avatar4.draw():
        print("avatar4")
        num2 = 4
        exec(open('avatarselection3.py').read())
    if avatar5.draw():
        print("avatar5")
        num2 = 5
        exec(open('avatarselection3.py').read())
    if avatar6.draw():
        print("avatar6")
        num2 = 6
        exec(open('avatarselection3.py').read())
    # to update game window
    pygame.display.update()