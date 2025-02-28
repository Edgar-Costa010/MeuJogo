import random
from code.background import Background
from code.enemy import Enemy
from code.player import Player
from const import LARGURA_TELA, ALTURA_TELA

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (LARGURA_TELA, 0)))
                return list_bg

            case 'jogador':
                return Player('jogador', (10, ALTURA_TELA / 2 - 30))

            case 'inimigo1':
                return Enemy('inimigo1', (LARGURA_TELA + 10, random.randint(0, ALTURA_TELA)))

            case 'inimigo2':
                return Enemy('inimigo2', (LARGURA_TELA + 10, random.randint(0, ALTURA_TELA)))