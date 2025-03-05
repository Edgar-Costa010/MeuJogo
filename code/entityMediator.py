from code.entity import Entity
from code.jogador import Jogador
from code.inimigos import Inimigos
from code.const import LARGURA_TELA
from code.tiroInimigo import TiroInimigo
from code.tiroJogador import TiroJogador


# Classe da entidade mediadora que intermedia os movimentos das entidades e fim do jogo em caso de derrota
class EntityMediator:

    # Verificação se as entidades (jogador, inimigo e tiros) sairam da tela para serem destruídas e não ocupar memória
    @staticmethod
    def saida_de_tela(ent: Entity):
        if isinstance(ent, Inimigos):
            if ent.rect.right < 0:
                ent.health = 0

        if isinstance(ent, TiroJogador):
            if ent.rect.left >= LARGURA_TELA:
                ent.health = 0

        if isinstance(ent, TiroInimigo):
            if ent.rect.right <= 0:
                ent.health = 0

    # Verifica colisao dos tiros inimigos com o jogador, dos tiros do jogador com o inimigo e jogador com inimigo
    @staticmethod
    def verifica_colisao_entidades(ent1, ent2):
        valid_interaction = False

        # Se os tiros colidirem com o jogador ou inimigo, quem receber o tiro perde pontos de vida e em caso de jogador e inimigo colidirem, o jogador perde o jogo
        if isinstance(ent1, Inimigos) and isinstance(ent2, TiroJogador):
            valid_interaction = True
        elif isinstance(ent1, TiroJogador) and isinstance(ent2, Inimigos):
            valid_interaction = True
        elif isinstance(ent1, TiroInimigo) and isinstance(ent2, Jogador):
            valid_interaction = True
        elif isinstance(ent1, Jogador) and isinstance(ent2, TiroInimigo):
            valid_interaction = True
        elif isinstance(ent1, Inimigos) and isinstance(ent2, Jogador):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left
                    and ent1.rect.left <= ent2.rect.right
                    and ent1.rect.bottom >= ent2.rect.top
                    and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    # Passar os pontos do inimigo para o jogador caso sejam acertados pelo tiro do jogador
    @staticmethod
    def ganhar_pontos(i: Inimigos, entity_list: list[Entity]):
        if i.last_dmg == 'jogadorTiro':
            for ent in entity_list:
                if ent.name == 'jogador':
                    ent.score += i.score

    @staticmethod
    def verifica_colisao_tela(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.saida_de_tela(entity1)

            for j in range(len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.verifica_colisao_entidades(entity1, entity2)

    @staticmethod
    def verifica_vida(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Inimigos):
                    EntityMediator.ganhar_pontos(ent, entity_list)
                entity_list.remove(ent)