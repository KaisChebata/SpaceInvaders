import pygame

# intialize pygame
pygame.init()

# set game screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('SpaceInvaders/raw_data/space_invaders_icon.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('SpaceInvaders/raw_data/player.png')
player_x, player_y = 370, 480
x_shift, y_shift = 0, 0

def player(x_axis, y_axis):
    screen.blit(player_img, (x_axis, y_axis))

# Game loop
running = True

while running:
    
    # drawing screen
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # Checking Keystrokes directions
        if event.type == pygame.KEYDOWN:
            # print('a keystroke is pressed ....')
            if event.key == pygame.K_LEFT:
                # print('left arrow is pressed ....')
                x_shift = -0.3
            if event.key == pygame.K_RIGHT:
                # print('right arrow is pressed ....')
                x_shift = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print('keystroke has been released ....')
                x_shift = 0

    # changing player X axis before drawing it.
    player_x += x_shift

    # drawing player
    player(player_x, player_y)

    # updating screen
    pygame.display.update()
    


