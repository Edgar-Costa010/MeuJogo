import random
import sys
import pygame
from pygame.font import Font

from code.enemy import Enemy
from code.entity import Entity
from pygame import Surface, Rect
from code.entityFactory import EntityFactory
from code.entityMadiator import EntityMadiator
from code.player import Player
from const import BRANCO, EVENTOS_INIMIGOS, ALTURA_TELA, APARICAO_INIMIGOS, VERMELHO_ESCURO


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode # Modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))
        self.entity_list.append(EntityFactory.get_entity('jogador'))
        pygame.time.set_timer(EVENTOS_INIMIGOS, APARICAO_INIMIGOS)

    def run(self):
        pygame.mixer_music.load('./assets/Soundlevels.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(90)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                if ent.name == Player:
                    self.level_text(14, f'jogador - Helath: {ent.health} | Score: {ent.score}', VERMELHO_ESCURO, (10, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENTOS_INIMIGOS:
                    choice = random.choice(('inimigo1', 'inimigo2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', BRANCO, (10, 5))
                self.level_text(14, f'fps: {clock.get_fps():.0f}', BRANCO, (10, ALTURA_TELA - 35))
                self.level_text(14, f'entidades: {len(self.entity_list)}', BRANCO, (10, ALTURA_TELA - 20))

                pygame.display.flip()

                EntityMadiator.verify_colision(entity_list=self.entity_list)
                EntityMadiator.verify_health(entity_list=self.entity_list)
                pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)