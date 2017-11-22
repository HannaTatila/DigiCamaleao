import sqlite3

_author__ = 'Hanna'


class DAOJogador:
    def __init__(self, ldadosjogador):
        self.jogador = ldadosjogador
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

    def inserir_jogador(self):
        try:
            self.cursor.execute("INSERT INTO jogador (id, login, senha) VALUES (?,?,?)",
                                (None, self.jogador[0], self.jogador[1]))
            self.conn.commit()  # salva dados no banco
        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao inserir jogador.")

    def consultar_jogador(self):
        try:
            #self.cursor.execute("SELECT login FROM jogador WHERE login = (?)", (str(self.jogador[0]),))
            self.cursor.execute("SELECT id FROM jogador WHERE login = (?)", (str(self.jogador[0]),))
            return len(self.cursor.fetchall()) != 0
        except sqlite3.Error:
            print("Erro ao consultar o banco!")

    def validar_login(self):
        try:
            self.cursor.execute("SELECT login, senha FROM jogador WHERE login = (?) AND senha = ?",
                                (str(self.jogador[0]), str(self.jogador[1]),))
            return len(self.cursor.fetchall()) == 1
        except sqlite3.Error:
            print("Erro ao consultar o banco para validar login!")


    def atualizar_pontuacao(self, nomemodulo, pontos):
        self.cursor.execute("SELECT id FROM jogador WHERE login = (?)", (str(self.jogador[0]),))
        idjogador = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT recorde FROM " + nomemodulo + " WHERE id_jogador = (?)", (idjogador,))
        recorde = self.cursor.fetchone()

        if recorde == None:
            try:
                self.cursor.execute("INSERT INTO " + nomemodulo + " (id, id_jogador, recorde) VALUES (?,?,?)",
                                    (None, idjogador, pontos))
            except sqlite3.Error:
                print("Erro ao inserir recorde!")

        elif pontos > recorde[0]:
            try:
                self.cursor.execute("UPDATE " + nomemodulo + " SET recorde = ? WHERE id_jogador = ?", (pontos, idjogador,))
            except sqlite3.Error:
                print ("Erro ao atualizar recorde!")

        self.conn.commit()

    def fechar_banco(self):
        self.conn.close()
