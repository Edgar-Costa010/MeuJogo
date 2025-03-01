from code.entity import Entity
from const import VELOCIDADES


class TiroJogador(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += VELOCIDADES[self.name]