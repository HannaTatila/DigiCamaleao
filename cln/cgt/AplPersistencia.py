import csv
import os

from cgd.DAOJogador import DAOJogador
from cgd.DAORanking import DAORanking
from cln.cdp.Jogador import Jogador
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna'


class AplPersistencia():
    @staticmethod
    def cadastrar_jogador(ldadosjogador):
        jog = DAOJogador(ldadosjogador)
        jogadorexiste = jog.consultar_jogador()
        if not jogadorexiste:
            jog.inserir_jogador()
        jog.fechar_banco()
        return not jogadorexiste

    def validar_login(self, ldadosjogador):
        jog = DAOJogador(ldadosjogador)
        validacao = jog.validar_login()
        if validacao:
            jog.fechar_banco()
            self.inicializar_jogador(ldadosjogador)
        return validacao

    def inicializar_jogador(self, ldadosjogador):
        self.jogador = Jogador()
        self.jogador.set_login(ldadosjogador)

    def requisitar_jogador(self):
        return self.jogador

    @staticmethod
    def cadastrar_pontuacao(jogador, nomemodulo, pontos):
        jog = DAOJogador(jogador.login)
        jog.atualizar_pontuacao(nomemodulo, pontos)

    def atribui_nome_ao_id_jogador(self, lrecordes):
        lrecordesfinal = list()
        for idjogador, recorde in lrecordes:
            nome = self.ranking.consultar_nome_jogador(idjogador)
            lrecordesfinal.append((nome, recorde))
        return lrecordesfinal

    def buscar_rankings(self):
        self.ranking = DAORanking()

        lrecordespl = self.ranking.consultar_banco_pegue_letras()
        lrecordesvd = self.ranking.consultar_banco_vamos_digitar()

        if lrecordespl: lrecordespl = self.atribui_nome_ao_id_jogador(lrecordespl)
        if lrecordesvd: lrecordesvd = self.atribui_nome_ao_id_jogador(lrecordesvd)

        self.ranking.fechar_banco()
        return lrecordespl, lrecordesvd

    def mescla_erros_jogo_arquivo(self, errosarquivo):
        for valor in errosarquivo:
            if valor != ['']:
                chave = (valor[0], valor[1])
                quantidade = int(valor[2])
                if self.dicerrosatuais.has_key(chave):
                    self.dicerrosatuais[chave] += quantidade
                else:
                    self.dicerrosatuais[chave] = quantidade

    def converte_dicionario_para_lista(self, loginjogador):
        lista = []
        lista.append(loginjogador)
        for item in self.dicerrosatuais.items():
            a = item[0][0] + ',' + item[0][1] + ',' + str(item[1])
            lista.append(a)
        return lista

    def registra_erros_partida(self, dicerros, loginjogador, nomearquivo):
        self.nomearquivo = nomearquivo
        self.dicerrosatuais = dicerros
        if self.dicerrosatuais:
            errosarquivo, listacompleta = self.busca_dados_arquivo(loginjogador)

            if errosarquivo:
                self.mescla_erros_jogo_arquivo(errosarquivo)

            listaatual = self.converte_dicionario_para_lista(loginjogador)
            listacompleta.append(listaatual)

            self.salva_dados_arquivo(listacompleta)

    def busca_dados_arquivo(self, loginjogador):
        dados = []
        listacompleta = []

        with open(os.path.join(CaminhoRecursos.caminho_log(), self.nomearquivo)) as arquivocsv:
            ler = csv.reader(arquivocsv)
            for linha in ler:
                if linha[0] != loginjogador:
                    listacompleta.append(linha)
                else:
                    for coluna in linha[1:]:
                        dados.append(coluna.split(','))

        arquivocsv.close()
        return dados, listacompleta

    def salva_dados_arquivo(self, conteudo):
        with open(os.path.join(CaminhoRecursos.caminho_log(), self.nomearquivo), "wb") as arq:
            escritor = csv.writer(arq)
            for linha in conteudo:
                escritor.writerow(linha)

    #coisa de s2
    """
    def salva_dados(self, nome, pontuacao, tipojogo):
        arquivo = csv.writer(open(os.path.join(CaminhoRecursos.caminho_log(), "LogJogo.csv"), "a"))
        #now = datetime.now()
        #data = "%d/%d/%d" % (now.day, now.month, now.year)
        #hora = "%d:%d" % (now.hour, now.minute)
        arquivo.writerow([nome,str(pontuacao),tipojogo,hora,data])
    """
