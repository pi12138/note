import pygame
from sys import exit


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BG_COLOR = (255, 255, 255)      # 白色
FONT_COLOR = (0, 0, 0)          # 黑色

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("event")

position = 0

# fonts = pygame.font.get_fonts()
font = pygame.font.SysFont('consolas', 18)
line_height = font.get_linesize()
# print(font)
# print(line_height)

screen.fill(BG_COLOR)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        font_file = font.render(str(event), True, FONT_COLOR)
        screen.blit(font_file, (0, position))

        position += line_height

        # 当屏幕内容满了之后，进行清屏操作
        if position > SCREEN_HEIGHT:
            position = 0
            screen.fill(BG_COLOR)
    
    pygame.display.flip()