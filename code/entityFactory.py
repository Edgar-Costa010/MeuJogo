import random
from code.inimigos import Inimigos
from code.jogador import Jogador
from code.background import Background
from code.const import LARGURA_TELA, ALTURA_TELA


# Fábrica de entidades, jogadores, inimigos, tiros e outras entidades do jogo
class EntityFactory:

    # Instanciação das entidades e definição dos posicionamentos delas na tela
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (LARGURA_TELA, 0)))
                return list_bg

            case 'Level2bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2bg{i}', (LARGURA_TELA, 0)))
                return list_bg

            case 'jogador':
                return Jogador('jogador', (10, ALTURA_TELA - 60))

            case 'inimigo1':
                return Inimigos('inimigo1', (LARGURA_TELA + 10, random.randint(0, ALTURA_TELA)))

            case 'inimigo2':
                return Inimigos('inimigo2', (LARGURA_TELA + 10, random.randint(0, ALTURA_TELA)))
