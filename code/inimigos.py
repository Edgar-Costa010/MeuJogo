from code.entity import Entity
from code.tiroInimigo import TiroInimigo
from const import VELOCIDADES, DELAY_TIRO


class Inimigos(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = DELAY_TIRO[self.name]

    def move(self):
        self.rect.centerx -= VELOCIDADES[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = DELAY_TIRO[self.name]
            return TiroInimigo(name=f'{self.name}tiro', position=(self.rect.centerx, self.rect.centery))