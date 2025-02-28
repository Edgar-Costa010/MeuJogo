
import pygame.image
from pygame import Surface, Rect, KEYDOWN
from pygame.font import Font
from const import LARGURA_TELA, ALARANJADO, VERMELHO_ESCURO, AZUL_CLARO, PRETO, ROXO
from const import MENU


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Level1bg4.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/SoundMenu.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Meu Jogo", ROXO, ((LARGURA_TELA / 2), 70))

            for i in range(len(MENU)):
                if i == menu_option:
                    self.menu_text(20, MENU[i], AZUL_CLARO, ((LARGURA_TELA / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU[i], PRETO, ((LARGURA_TELA / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < (len(MENU)) -1:
                            menu_option +=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -=1
                        else:
                            menu_option = len(MENU) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
