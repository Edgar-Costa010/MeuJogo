import pygame

LARGURA_TELA = 576
ALTURA_TELA = 324

DALAY_TIRO = {
    'jogador': 20,
    'inimigo1': 50,
    'inimigo2': 50
}

VELOCIDADES = {
    'Level1bg0': 0,
    'Level1bg1': 1,
    'Level1bg2': 2,
    'Level1bg3': 1,
    'Level1bg4': 1,
    'Level1bg5': 2,
    'Level1bg6': 3,
    'jogador': 3,
    'jogadorTiro':1,
    'inimigo1tiro': 2,
    'inimigo2tiro': 2,
    'inimigo1': 1,
    'inimigo2': 1
}

MENU = (
    'INICIAR JOGO',
    'SCORE',
    'EXIT'
)

ALARANJADO = (255, 69, 0)
VERMELHO_ESCURO = (139, 0, 0)
AZUL_CLARO = (0, 0, 205)
PRETO = (0, 0, 0)
BRANCO = (255, 250, 250)
ROXO = (75,0,130)

EVENTOS_INIMIGOS = pygame.USEREVENT + 1

APARICAO_INIMIGOS = 4000

JOGADOR_KEY_UP = {'jogador': pygame.K_UP}

JOGADOR_KEY_DOWN = {'jogador': pygame.K_DOWN}

JOGADOR_KEY_LEFT = {'jogador': pygame.K_LEFT}

JOGADOR_KEY_RIGHT = {'jogador': pygame.K_RIGHT}

TECLA_TIRO = {'jogador': pygame.K_SPACE}

TEMPO_DE_VIDA = {
    'Level1bg0': 999,
    'Level1bg1': 999,
    'Level1bg2': 999,
    'Level1bg3': 999,
    'Level1bg4': 999,
    'Level1bg5': 999,
    'Level1bg6': 999,
    'jogador': 300,
    'inimigo1': 50,
    'inimigo2': 60,
    'jogadorTiro': 1,
    'inimigo1tiro': 3,
    'inimigo2tiro': 3
}

DANOS = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level1bg5': 0,
    'Level1bg6': 0,
    'jogador': 1,
    'inimigo1': 50,
    'inimigo2': 60,
    'jogadorTiro': 25,
    'inimigo1tiro': 15,
    'inimigo2tiro': 15
}

SCORE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level1bg5': 0,
    'Level1bg6': 0,
    'jogador': 0,
    'jogadorTiro': 0,
    'inimigo2tiro': 0,
    'inimigo1tiro': 0,
    'inimigo1': 50,
    'inimigo2': 50
}