import sqlite3

_author__ = 'Hanna'


class DAORanking:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("Digicamaleao.db")  # conexao banco
            self.cursor = self.conn.cursor()
            self.criar_tabela()
        except sqlite3.Error:
            print("Erro ao abrir o banco.")

    def criar_tabela(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS jogador (id INTEGER PRIMARY KEY AUTOINCREMENT, login varchar(15), senha varchar(8))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pegueletras (id INTEGER PRIMARY KEY AUTOINCREMENT, id_jogador INTEGER, recorde INTEGER, FOREIGN KEY (id_jogador) REFERENCES jogador(id))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS vamosdigitar (id INTEGER PRIMARY KEY AUTOINCREMENT, id_jogador INTEGER, recorde INTEGER, FOREIGN KEY (id_jogador) REFERENCES jogador(id))")

    def consultar_banco_pegue_letras(self):
        try:
            self.cursor.execute("SELECT id_jogador, recorde FROM pegueletras WHERE recorde <> 0 ORDER BY recorde DESC LIMIT 3")
            return self.cursor.fetchall()
        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao consultar o banco pegue as letras!")

    def consultar_banco_vamos_digitar(self):
        try:
            self.cursor.execute(
                "SELECT id_jogador, recorde FROM vamosdigitar WHERE recorde <> 0 ORDER BY recorde DESC LIMIT 3")
            return self.cursor.fetchall()
        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao consultar o banco vamos digitar!")

    def consultar_nome_jogador(self, id):
        try:
            self.cursor.execute("SELECT login FROM jogador WHERE id = (?)", (id,))
            return self.cursor.fetchone()
        except sqlite3.Error:
            print("Erro ao consultar o nome do jogador!")


    def fechar_banco(self):
        self.conn.close()
