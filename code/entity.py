from abc import ABC, abstractmethod
import pygame.image
from code.const import TEMPO_DE_VIDA, DANOS, SCORE


# Classe mãe, Entidade
class Entity(ABC):
    # Instanciação dos métodos em comun necessários nas classes filhas
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = TEMPO_DE_VIDA[self.name]
        self.damage = DANOS[self.name]
        self.score = SCORE[self.name]
        self.last_dmg = None

    @abstractmethod
    def move(self):
        pass