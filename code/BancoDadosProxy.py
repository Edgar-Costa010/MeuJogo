import sqlite3


class BancoDados:

    def __init__(self, banco: str):
        self.banco = banco
        self.conexao = sqlite3.connect(banco)
        self.conexao.execute('''
            CREATE TABLE IF NOT EXISTS dados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT NOT NULL)
            ''')


    def resultados(self, score_dict: dict):
        self.conexao.execute('INSERT INTO dados(name,score, date) VALUES (:name, :score, :date)', score_dict)
        self.conexao.commit()

    def melhores(self) -> list:
        return self.conexao.execute('SELECT * FROM dados ORDER BY score DESC limit 3').fetchall()

    def fechar(self):
        self.conexao.close()