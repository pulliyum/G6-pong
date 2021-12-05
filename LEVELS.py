
#Background

biOne = pygame.image.load('../../../PycharmProjects/G6-pong/default.png').convert()
biOne = pygame.transform.scale(biOne, (screen_width, screen_height))

biTwo = pygame.image.load('../../../PycharmProjects/G6-pong/space.jpg').convert()
biTwo = pygame.transform.scale(biTwo, (screen_width, screen_height))

biThree = pygame.image.load('../../../PycharmProjects/G6-pong/underground.jpg').convert()
biThree = pygame.transform.scale(biThree, (screen_width, screen_height))

background_index = 0
background_images = [ biOne, biTwo, biThree ]




#--------------------------------------------
menu_font = pygame.font.Font('freesansbold.ttf', 65)
submenu_font = pygame.font.Font('freesansbold.ttf', 25)
menu = False

def level_menu():
    # Menu Text
    global background_index
    pygame.display.set_caption('Level Selection')
    menu_text = menu_font.render("***Levels***", True, (255, 255, 255))
    screen.blit(menu_text, (100 , 50))
    menu_text = submenu_font.render("1. Default", True, (255, 255, 255))
    screen.blit(menu_text, (150 , 150))
    menu_text = submenu_font.render("2. Space", True, (255, 255, 255))
    screen.blit(menu_text, (150 , 250))
    menu_text = submenu_font.render("3. Underground", True, (255, 255, 255))
    screen.blit(menu_text, (150 , 350))



#-------------------------------------------------------
    # inside of game loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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

    # Visuals
    # set background
    screen.blit(background_images[background_index], [0, 0])