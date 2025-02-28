import pygame

from code.level import Level
from code.menu import Menu
from const import LARGURA_TELA, ALTURA_TELA, MENU


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(LARGURA_TELA, ALTURA_TELA))

    def run(self):

        print('Loop para manter a janela aberta até que o X seja pressionado')
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU[0]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU[2]:
                pygame.quit()
                quit()

            else:
                pass
