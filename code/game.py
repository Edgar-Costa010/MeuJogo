import pygame
from code.menu import Menu
from code.level import Level
from code.score import Score
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
            score = Score(self.window)

            if menu_return in [MENU[0]]:

                pontos = [0]

                level = Level(self.window, 'Level1', menu_return, pontos)
                level_return = level.run(pontos)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, pontos)
                    level_return = level.run(pontos)
                    if level_return:
                        score.pontuacao(menu_return, pontos)

            elif menu_return == MENU[1]:
                score.ver_pontos()

            elif menu_return == MENU[2]:
                pygame.quit()
                quit()
            else:
                pass
