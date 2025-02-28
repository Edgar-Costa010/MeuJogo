from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.player import Player
from code.playerShot import PlayerShot
from const import LARGURA_TELA


class EntityMadiator:


    @staticmethod
    def __give_score__(enemy: Enemy, entity_list: list[Entity]):
        if enemy.lest_dmg == 'tiroJogador':
            for ent in entity_list:
                if ent.name == 'jogador':
                    ent.score += enemy.score

    @staticmethod
    def __verify_colision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

        if isinstance(ent, PlayerShot):
            if ent.rect.left >= LARGURA_TELA:
                ent.health = 0

        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_colision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left
                    and ent1.rect.left <= ent2.rect.right
                    and ent1.rect.bottom >= ent2.rect.top
                    and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.lest_dmg = ent2.name
                ent2.lest_dmg = ent1.name

    @staticmethod
    def verify_colision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMadiator.__verify_colision_window(entity1)

            for j in range(len(entity_list)):
                entity2 = entity_list[j]
                EntityMadiator.__verify_colision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMadiator.__give_score__(ent, entity_list)
                entity_list.remove(ent)