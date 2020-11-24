import pygame
import random
from math import sqrt, pow


# intialize pygame
pygame.init()

# set game screen
screen = pygame.display.set_mode((800, 600))

# Set Background
background = pygame.image.load('SpaceInvaders/raw_data/background.png')

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('SpaceInvaders/raw_data/space_invaders_icon.png')
pygame.display.set_icon(icon)

# Enemy
enemy_image = pygame.image.load('SpaceInvaders/raw_data/enemy.png')
enemy_x = random.randint(0, 735)
enemy_y = random.randint(50, 150)
enemy_xshift, enemy_yshift = 4.5, 40

# Bullet
# Bullet states:
# ready: can't see bullet on screen
# fire: the bullet is currently moving.
bullet_img = pygame.image.load('SpaceInvaders/raw_data/bullet.png')
bullet_x, bullet_y = 0, 480
bullet_xshift, bullet_yshift = 0, 10
bullet_state = 'ready'

# Player
player_img = pygame.image.load('SpaceInvaders/raw_data/player.png')
player_x, player_y = 370, 480
player_xshift = 0

# Score:
score = 0

def player(x_axis, y_axis):
    screen.blit(player_img, (x_axis, y_axis))

def enemy(x_axis, y_axis):
    screen.blit(enemy_image, (x_axis, y_axis))

def fire_bullet(x_axis, y_axis):
    global bullet_state
    bullet_state = 'fire'

    screen.blit(bullet_img, (x_axis + 16, y_axis + 10))

def is_collision(enemy_x_axis, enemy_y_axis, bullet_x_axis, bullet_y_axis):
    distance = sqrt(
        (pow(enemy_x_axis - bullet_x_axis,2)) + (pow(enemy_y_axis - bullet_y_axis, 2))
        )
    return True if distance < 27 else False

# Game loop
running = True

while running:
    
    # drawing screen
    screen.fill((0, 0, 0))

    # drawing Background Image
    screen.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # Checking Keystrokes directions
        if event.type == pygame.KEYDOWN:
            # print('a keystroke is pressed ....') # this comment and other similar to for debugging
            if event.key == pygame.K_LEFT:
                # print('left arrow is pressed ....')
                player_xshift = -5
            if event.key == pygame.K_RIGHT:
                # print('right arrow is pressed ....')
                player_xshift = 5
            if event.key == pygame.K_SPACE:
                # stoping bullet from movement with spaceship after first shout
                if bullet_state == 'ready':
                    # get the currenct x cordinate of the spaceship
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
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

    # Checking X axis, Y axis Boundaries for Enemy
    if enemy_x <= 0:
        enemy_xshift = 4.5
        enemy_y += enemy_yshift
    elif enemy_x >= 736:
        enemy_xshift = -4.5
        enemy_y += enemy_yshift
    
    # Bullet Movement
    if bullet_y <= 0:
        bullet_y = 485
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_yshift
    
    # collision
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = 'ready'
        score += 1
        print(score)
        enemy_x = random.randint(0, 735)
        enemy_y = random.randint(50, 150)
    
    # drawing player
    player(player_x, player_y)

    # drawing enemy
    enemy(enemy_x, enemy_y)

    # updating screen
    pygame.display.update()
    


