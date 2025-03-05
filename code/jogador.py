# Importaçã dos métodos e classes necessários

import pygame.key
from code.entity import Entity
from code.tiroJogador import TiroJogador
from code.const import VELOCIDADES, ALTURA_TELA, LARGURA_TELA, JOGADOR_KEY_RIGHT, JOGADOR_KEY_LEFT, JOGADOR_KEY_DOWN, \
    JOGADOR_KEY_UP, TECLA_TIRO, DELAY_TIRO


# Inicialização da classe
class Jogador(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = DELAY_TIRO[self.name]

    # Criação da função e destinação das teclas de movimento do jogador
    def move(self):
        tecla_movimento = pygame.key.get_pressed()
        if tecla_movimento[JOGADOR_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= VELOCIDADES[self.name]

        if tecla_movimento[JOGADOR_KEY_DOWN[self.name]] and self.rect.bottom < ALTURA_TELA:
            self.rect.centery += VELOCIDADES[self.name]

        if tecla_movimento[JOGADOR_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= VELOCIDADES[self.name]

        if tecla_movimento[JOGADOR_KEY_RIGHT[self.name]] and self.rect.right < LARGURA_TELA:
            self.rect.centerx += VELOCIDADES[self.name]
            pass

    # Implementação da função de atirar, tecla ESPAÇO é a responsável pelos disparos
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = DELAY_TIRO[self.name]
            tecla_movimento = pygame.key.get_pressed()
            if tecla_movimento[TECLA_TIRO[self.name]]:
                return TiroJogador(name=f'{self.name}Tiro', position=(self.rect.centerx, self.rect.centery))
