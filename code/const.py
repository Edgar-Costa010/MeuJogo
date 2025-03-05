import pygame

# Ajustes do tamanho da janela do jogo
LARGURA_TELA = 576
ALTURA_TELA = 324

APARICAO_INIMIGOS = 4000

# Cores
ALARANJADA = (255, 69, 0)
VERMELHO_ESCURO = (139, 0, 0)
AZUL_CLARO = (0, 0, 205)
PRETA = (0, 0, 0)
BRANCA = (255, 250, 250)
ROXA = (75, 0, 130)

# D
DELAY_TIRO = {
    'jogador': 20,
    'inimigo1': 50,
    'inimigo2': 50
}

DANOS = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level1bg5': 0,
    'Level1bg6': 0,
    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Level2bg4': 0,
    'Level2bg5': 0,
    'Level2bg6': 0,
    'jogador': 1,
    'inimigo1': 20,
    'inimigo2': 30,
    'jogadorTiro': 25,
    'inimigo1tiro': 15,
    'inimigo2tiro': 30
}

# E
EVENTOS_INIMIGOS = pygame.USEREVENT + 1

#Eventos para passar a fase
FIM_DE_FASE = pygame.USEREVENT + 2
VERIFICACAO = 1
TEMPO_RESTANTE = 15000 #30 segundos de duração de cada fase

# M
MENU = (
    'INICIAR JOGO',
    'SCORE',
    'EXIT'
)

# S
SCORE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level1bg5': 0,
    'Level1bg6': 0,
    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Level2bg4': 0,
    'Level2bg5': 0,
    'Level2bg6': 0,
    'jogador': 0,
    'jogadorTiro': 0,
    'inimigo2tiro': 0,
    'inimigo1tiro': 0,
    'inimigo1': 25,
    'inimigo2': 50
}

# T
# Teclas para movimentação e tiro do jogador
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
    'Level2bg0': 999,
    'Level2bg1': 999,
    'Level2bg2': 999,
    'Level2bg3': 999,
    'Level2bg4': 999,
    'Level2bg5': 999,
    'Level2bg6': 999,
    'jogador': 300,
    'inimigo1': 50,
    'inimigo2': 100,
    'jogadorTiro': 1,
    'inimigo1tiro': 1,
    'inimigo2tiro': 1
}

# V
VELOCIDADES = {
    'Level1bg0': 0,
    'Level1bg1': 1,
    'Level1bg2': 2,
    'Level1bg3': 1,
    'Level1bg4': 1,
    'Level1bg5': 2,
    'Level1bg6': 3,
    'Level2bg0': 0,
    'Level2bg1': 1,
    'Level2bg2': 2,
    'Level2bg3': 1,
    'Level2bg4': 1,
    'Level2bg5': 2,
    'Level2bg6': 3,
    'jogador': 3,
    'jogadorTiro':1,
    'inimigo1tiro': 3,
    'inimigo2tiro': 5,
    'inimigo1': 1,
    'inimigo2': 1
}