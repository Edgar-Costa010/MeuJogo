# Classe para fazer disparar os tiros inimigos contra o jogador

# Importação das classes pertinentes
from code.entity import Entity
from code.const import VELOCIDADES


# Classe filha herdando os métodos da classe mãe Entity
class TiroInimigo(Entity):

    # Função para inicialização da classe
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Função para movimento do tiro no eixo x do gráfico, no sentido negativo do eixo para ir contra ao joogador
    def move(self):
        self.rect.centerx -= VELOCIDADES[self.name]