from code.enemyShot import EnemyShot
from code.entity import Entity
from const import VELOCIDADES, DALAY_TIRO


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = DALAY_TIRO[self.name]

    def move(self):
        self.rect.centerx -= VELOCIDADES[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = DALAY_TIRO[self.name]
            return EnemyShot(name=f'{self.name}tiro', position=(self.rect.centerx, self.rect.centery))