import pygame
import random

# intialize pygame
pygame.init()

# set game screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('SpaceInvaders/raw_data/space_invaders_icon.png')
pygame.display.set_icon(icon)

# Enemy
enemy_image = pygame.image.load('SpaceInvaders/raw_data/enemy.png')
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_xshift, enemy_yshift = 0.3, 40

# Player
player_img = pygame.image.load('SpaceInvaders/raw_data/player.png')
player_x, player_y = 370, 480
player_xshift = 0

def player(x_axis, y_axis):
    screen.blit(player_img, (x_axis, y_axis))

def enemy(x_axis, y_axis):
    screen.blit(enemy_image, (x_axis, y_axis))

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
            # print('a keystroke is pressed ....') # this comment and other similar to for debugging
            if event.key == pygame.K_LEFT:
                # print('left arrow is pressed ....')
                player_xshift = -0.3
            if event.key == pygame.K_RIGHT:
                # print('right arrow is pressed ....')
                player_xshift = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print('keystroke has been released ....')
                player_xshift = 0

    # Checking X axis Boundaries for Spaceship before drawing it.
    player_x += player_xshift
    
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736 
    
    # Enemy Movements
    enemy_x += enemy_xshift

    if enemy_x <= 0:
        enemy_xshift = 0.3
        enemy_y += enemy_yshift
    elif enemy_x >= 736:
        enemy_xshift = -0.3
        enemy_y += enemy_yshift
    
    # drawing player
    player(player_x, player_y)

    # drawing enemy
    enemy(enemy_x, enemy_y)

    # updating screen
    pygame.display.update()
    


