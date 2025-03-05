import pygame
from code.menu import Menu
from code.level import Level
from code.score import Score
from code.const import LARGURA_TELA, ALTURA_TELA, MENU


# Classe game, onde o jogo inicia e são instanciadas as fases
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

            # Seleção do menu, opções de iniciar o jogo, ver o score ou fechar a tela
            # Indice zero (Iniciar jogo) inicia a fase 1
            if menu_return in [MENU[0]]:

                pontos = [0]
                # Fases do jogo. Implementadas apenas duas fases inicialmente
                level = Level(self.window, 'Level1', menu_return, pontos)
                level_return = level.run(pontos)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, pontos)
                    level_return = level.run(pontos)
                    if level_return:
                        score.pontuacao(menu_return, pontos)

            # Indice 1 (Score) ver o histórico de score
            elif menu_return == MENU[1]:
                score.ver_pontos()

            # Indice 2 (exit) aciona o evento sair e fecha a janela e o jogo encerra
            elif menu_return == MENU[2]:
                pygame.quit()
                quit()
            else:
                pass