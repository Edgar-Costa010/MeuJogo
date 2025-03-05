from cx_Freeze import setup, Executable

executaveis = [Executable("main.py")]

setup(
    nome = ' MEU JOGO',
    versao = '2.0',
    descricao = 'Jogo de tiro',
    opcoes = {'build.exe': {'packages': ['pygame']}},
    executaveis = Executable
)