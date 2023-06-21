import pygame

from pygame.locals import *

window = pygame.display.set_mode((100, 100), 0, 32)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            print('exit')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
            elif event.key == K_SPACE:
                print("space")