from code.entity import Entity
from code.const import LARGURA_TELA, VELOCIDADES


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= VELOCIDADES[self.name]
        if self.rect.right <= 0:
            self.rect.left = LARGURA_TELA