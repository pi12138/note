'''显示飞机'''

import pygame
import time

'''1.搭建界面，主要完成窗口和背景图的显示'''

def main():
    # 1. 创建一个窗口
    window = pygame.display.set_mode((480, 852), 0, 32)

    # 2.加载一张和窗口大小一样的图片
    background_image = pygame.image.load('./feiji/background.png')
    # 3.加载一个飞机
    my_plain = pygame.image.load('./feiji/hero1.png')


    while True:
        # 将加载的图片放到打开的窗口
        window.blit(background_image, (0, 0))
        window.blit(my_plain, (190, 700))

        # 更新需要显示的内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()