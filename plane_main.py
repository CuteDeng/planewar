import pygame
from plane_sprites import *


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始")


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
