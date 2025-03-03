import sys
from datetime import datetime

import pygame
from pygame.font import Font
from pygame import Surface, Rect, K_RETURN, K_BACKSPACE, KEYDOWN
from code.BancoDadosProxy import BancoDados
from const import PRETA, LARGURA_TELA, MENU, VERMELHO_ESCURO

class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/Level1bg4.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def pontuacao(self, game_mode: str, pontuacao):
        pygame.mixer_music.load('./assets/SoundMenu.wav')
        pygame.mixer_music.play(-1)
        bancodados = BancoDados('banco')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(30, 'PARABÉNS, JOGADOR!!!', PRETA, (LARGURA_TELA/2, 50))
            self.score_text(30, 'VOCÊ VENCEU!!!', PRETA, (LARGURA_TELA / 2, 90))
            if game_mode == MENU[0]:
                score = pontuacao[0]
                texto = "Digite seu nome: "

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len (name) == 10:
                        bancodados.resultados({'name': name, 'score': score, 'date': get_formatted_date()})
                    elif event.key == K_BACKSPACE:
                        name = name [:-1]
                    else:
                        if len(name) < 10:
                            name += event.unicode
            self.score_text(20, name, VERMELHO_ESCURO, (LARGURA_TELA / 2, 120))
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

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H %M')
    current_date = current_datetime.strftime('%d %m %y')
    return f'{current_time} - {current_date}'