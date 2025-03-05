from code.entity import Entity
from code.tiroInimigo import TiroInimigo
from code.const import VELOCIDADES, DELAY_TIRO


# Iniciaçação da classe inimigos
class Inimigos(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = DELAY_TIRO[self.name]

    def move(self):
        self.rect.centerx -= VELOCIDADES[self.name]

    # Função de implementação dos tiros inimigos, sendo disparados de forma automática sem necessidade de interação do usuário
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = DELAY_TIRO[self.name]
            return TiroInimigo(name=f'{self.name}tiro', position=(self.rect.centerx, self.rect.centery))
