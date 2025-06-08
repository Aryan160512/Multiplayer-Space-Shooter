import os

x= 100
y = 100

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'

import pygame
from pygame.locals import *

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
isRunning = True

keysS1 = [False, False, False, False]
keysS2 = [False, False, False, False]


bg = pygame.image.load('Images/background.jpg')
spaceship1 = pygame.image.load('Images/spaceship.png')
spaceship2 = pygame.image.load('Images/spaceship2.png')

spaceship1_x = 100
spaceship1_y = 200

spaceship2_x = 300
spaceship2_y = 400

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keysS1[0] = True
            elif event.key == pygame.K_a:
                keysS1[1]= True
            elif event.key == pygame.K_s:
                keysS1[2]= True
            elif event.key == pygame.K_d:
                keysS1[3]= True            
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keysS1[0] = False
            elif event.key == pygame.K_a:
                keysS1[1]= False
            elif event.key == pygame.K_s:
                keysS1[2]= False
            elif event.key == pygame.K_d:
                keysS1[3]= False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keysS2[0] = True
            elif event.key == pygame.K_LEFT:
                keysS2[1]= True
            elif event.key == pygame.K_DOWN:
                keysS2[2]= True
            elif event.key == pygame.K_RIGHT:
                keysS2[3]= True            
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keysS2[0] = False
            elif event.key == pygame.K_LEFT:
                keysS2[1]= False
            elif event.key == pygame.K_DOWN:
                keysS2[2]= False
            elif event.key == pygame.K_RIGHT:
                keysS2[3]= False

    if keysS1[0]:
        spaceship1_y -= 1.5
    elif keysS1[1]:
        spaceship1_x -= 1.5
    elif keysS1[2]:
        spaceship1_y += 1.5
    elif keysS1[3]:
        spaceship1_x += 1.5

    if keysS2[0]:
        spaceship2_y -= 1.5
    elif keysS2[1]:
        spaceship2_x -= 1.5
    elif keysS2[2]:
        spaceship2_y += 1.5
    elif keysS2[3]:
        spaceship2_x += 1.5

    screen.blit(bg, (0, 0))

    screen.blit(spaceship1, (spaceship1_x, spaceship1_y))
    screen.blit(spaceship2, (spaceship2_x, spaceship2_y))
    pygame.display.update()


pygame.quit()