# Importação das classes e métodos necessários para a execução do level

import sys
import random
import pygame
from pygame.font import Font
from code.entity import Entity
from code.jogador import Jogador
from pygame import Surface, Rect
from code.inimigos import Inimigos
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.const import BRANCA, EVENTOS_INIMIGOS, ALTURA_TELA, APARICAO_INIMIGOS, VERMELHO_ESCURO, VERIFICACAO, \
    FIM_DE_FASE, \
    TEMPO_RESTANTE


# Classe level para indicação de tempo de jogo e , score, mudança de fase e textos na tela
class Level:

    # Função para inicialização da classe e instanciação dos atributos necessários
    def __init__(self, window: Surface, name: str, game_mode: str, pontos: list[int]):
        self.timeout = TEMPO_RESTANTE
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'bg'))
        # Atribuição de pontos (score) ao jogador
        jogador = EntityFactory.get_entity('jogador')
        jogador.pontuacao = pontos[0]
        self.entity_list.append(jogador)
        pygame.time.set_timer(EVENTOS_INIMIGOS, APARICAO_INIMIGOS)
        pygame.time.set_timer(FIM_DE_FASE, VERIFICACAO)

    # Função do metodo run para aparição das entidades e midias e movimento das imagens na tela durante o jogo
    def run(self, pontos: list[int]):
        pygame.mixer_music.load('./assets/Soundlevels.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        # Laço de repetição para os eventos e verificação se a entidade jogador continua na tela para determinar se continua ou para o jogo
        while True:
            clock.tick(90)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Jogador, Inimigos)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                # Visibilidade da vida e pontuação do jogador
                if ent.name == 'jogador':
                    self.level_text(14, f'Helath: {ent.health} | Score: {ent.score}', VERMELHO_ESCURO, (10, 30))

            # Evento para fechar o jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENTOS_INIMIGOS:
                    choice = random.choice(('inimigo1', 'inimigo2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                # Evento para mudança de fase
                if event.type == FIM_DE_FASE:
                    self.timeout -= VERIFICACAO
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Jogador) and ent.name == 'Jogador':
                                pontos[0] = ent.score
                        return True
                verifica_jogador = False
                for ent in self.entity_list:
                    if isinstance(ent, Jogador):
                        verifica_jogador = True
                if not verifica_jogador:
                    return False

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', BRANCA, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', BRANCA, (10, ALTURA_TELA - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', BRANCA, (10, ALTURA_TELA - 20))
            pygame.display.flip()

            EntityMediator.verifica_colisao_tela(entity_list=self.entity_list)
            EntityMediator.verifica_vida(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
