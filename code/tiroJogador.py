# Classe para inserir os tiros do jogador contra os inimigos

# Importação das classes pertinentes para fazer a classe funcionar corretamente
from code.entity import Entity
from code.const import VELOCIDADES

# Classe filha herdando métodos da classe mãe Entity
class TiroJogador(Entity):

    # Função de inicialização
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Função para movimento dos tiros no eixo X do gráfico
    def move(self):
        self.rect.centerx += VELOCIDADES[self.name]