import pygame
from pygame import Surface, Rect
from pygame.font import Font

from const import PRETA, LARGURA_TELA


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/Level1bg4.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def pontuacao(self, menu_return, pontuacao):
        pygame.mixer_music.load('./assets/SoundMenu.wav')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.score_text(30, 'PARABÉNS PELA VITÓRIA!!', PRETA, (LARGURA_TELA/2, 50))
            pygame.display.flip()
            pass

    def ver_pontos(self):
        pygame.mixer_music.load('./assets/SoundMenu.wav')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)