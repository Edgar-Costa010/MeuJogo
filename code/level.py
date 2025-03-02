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
from const import BRANCA, EVENTOS_INIMIGOS, ALTURA_TELA, APARICAO_INIMIGOS, VERMELHO_ESCURO, EVENT_TIME_OUT, \
    TIME_OUT_STEP, TIMEOUT_LEVEL

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, pontos: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'bg'))
        jogador = EntityFactory.get_entity('jogador')
        jogador.pontuacao = pontos [0]
        self.entity_list.append(jogador)
        pygame.time.set_timer(EVENTOS_INIMIGOS, APARICAO_INIMIGOS)
        pygame.time.set_timer(EVENT_TIME_OUT, TIME_OUT_STEP)

    def run(self, pontos: list[int]):
        pygame.mixer_music.load('./assets/Soundlevels.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(90)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Jogador, Inimigos)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                if ent.name == 'jogador':
                    self.level_text(14, f'Helath: {ent.health} | Score: {ent.score}', VERMELHO_ESCURO, (10, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENTOS_INIMIGOS:
                    choice = random.choice(('inimigo1', 'inimigo2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIME_OUT:
                    self.timeout -= TIME_OUT_STEP
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

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
