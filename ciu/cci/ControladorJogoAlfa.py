#coding: utf-8
import os
import sys

import pygame

from ciu.cci.ControladorJogo import ControladorJogo
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from cln.cgt.AplPersistencia import AplPersistencia
from cln.cgt.AplJogoAlfa import AplJogoAlfa
from cln.cgt.AplPersistencia import AplPersistencia
from principal.CaminhoRecursos import CaminhoRecursos

reload(sys)
sys.setdefaultencoding("utf-8")

class ControladorJogoAlfa(ControladorJogo):
    TAM_FONTE_PALAVRA = 30

    def __init__(self):
        ControladorJogo.__init__(self)
        self.listacenarios = ["mar", "deserto", "mata", "ceu", "espaco"]
        self.apljogo = AplJogoAlfa()
        self.aplcadastrarjogador = AplPersistencia()
        self.aplpersistencia = AplPersistencia()
        self.palavrascertas = list()
        self.palavraserradas = list()
        self.busca_sons_jogo()
        self.corletra = self.COR_BRANCO
        self.continuarjogo = True

    def busca_imagens_tela(self):
        self.imagempersonagem = self.get_imagem("personagem.png", self.listacenarios[self.apljogo.idcenario])
        self.imagemfundo = self.get_imagem("fundojogo.png", self.listacenarios[self.apljogo.idcenario])
        self.imagemvida = self.get_imagem("vida.png", self.listacenarios[self.apljogo.idcenario])

    def busca_sons_jogo(self):
        self.somletracerta = self.get_som("moeda.wav")
        self.somletraerrada = self.get_som("colisao2.wav")
        self.sompalavracompleta = self.get_som("vitoria.wav")

    def exibir_palavra_digitacao(self, palavra, indice):
        faltam = len(palavra) - indice
        self.telajogo.exibe_texto_personalizado(palavra[:indice] + ("_ " * faltam), self.TAM_FONTE_PALAVRA,
                                                EstiloElementos.posicao_mensagem(), self.corletra)

    def exibir_letra_digitacao(self, palavra, indice):
        self.telajogo.exibe_texto_personalizado(palavra[indice], self.TAM_FONTE_PALAVRA, Posicao(650, 90), self.corletra)

    # a classe ControlodorJogo (q eh um observador)recebe atualizacao pq a classe Observada ObservableEventosTeclado capturou um evento
    def update(self, observable):
        if observable.space:
            self.paused(observable)
        if observable.escape:
            self.continuarjogo = False
        #if (observable.enter) and (self.apljogo.fimdejogo):
        #    self.continuarjogo = False
        if observable.cima:
            self.apljogo.personagem.diminui_deslocamento_y()
        if observable.baixo:
            self.apljogo.personagem.aumenta_deslocamento_y()
        if observable.soltoubaixo:
            self.apljogo.personagem.deslocamentoy = 0

    def atualiza_tela(self):
        self.exibir_tela_jogo(self.imagemfundo)
        self.telajogo.exibe_imagem(self.imagempersonagem, self.apljogo.personagem.posicao)
        if self.apljogo.lobstaculos:
            palavra = self.apljogo.palavras.palavra_atual().upper()
            indice = self.apljogo.palavras.indice_atual()
            self.exibir_palavra_digitacao(palavra, indice)
            self.exibir_letra_digitacao(palavra, indice)
            imagem = self.get_obstaculo(palavra + ".png", self.listacenarios[self.apljogo.idcenario])
            self.telajogo.exibe_imagem(imagem, Posicao(700 - imagem.get_width() - 20, 15))
            #pygame.draw.rect(self.telajogo.tela, self.COR_BRANCO, (600, 5, 90, 120), 2) #retangulo em volta da img
            #pygame.draw.line(self.telajogo.tela, self.COR_BRANCO, [600, 125], [690, 125], 2)
        for letra in self.apljogo.lobstaculos:
            self.telajogo.exibe_texto_personalizado(letra.nome.upper(), self.apljogo.tamanholetra, letra.posicao, self.corletra)
        self.exibir_pontuacao("Pontos: ")
        self.exibir_vidas(self.imagemvida)

    def atualiza_cor_letras(self):
        self.corletra = self.COR_BRANCO
        if self.listacenarios[self.apljogo.idcenario] == "ceu":
            self.corletra = self.COR_AZUL
        elif self.listacenarios[self.apljogo.idcenario] == "deserto":
            self.corletra = (128, 0, 0)

    def atualiza_dados_fase(self):
        self.exibir_musica_partida(self.listacenarios[self.apljogo.idcenario])
        self.atualiza_cor_letras()
        self.apljogo.novafase = False
        self.apljogo.voltoufase = False
        self.busca_imagens_tela()
        self.apljogo.captura_palavras(self.listacenarios[self.apljogo.idcenario])
        self.apljogo.reinicia_lista_obstaculos()

    def jogo(self, jogador, nomemodulo):
        self.exibir_tela_instrucoes("instrucoespl.png")
        observable = self.inicializa_observable()
        self.apljogo.configuracao()
        self.atualiza_dados_fase()
        self.apljogo.nova_palavra()
        while self.continuarjogo:
            observable.verifica_evento()
            self.apljogo.jogar()
            if self.apljogo.palavras.palavra_acabou():
                self.palavrascertas.append(self.apljogo.palavras.palavra_atual())
                self.apljogo.incrementa_pontuacao()
                self.telajogo.exibe_som(self.sompalavracompleta)
                self.apljogo.nova_palavra()
                self.apljogo.palavras.proxima_palavra()
                self.apljogo.verifica_troca_fase()
                if self.apljogo.novafase:
                    self.telajogo.exibe_som(self.sompalavracompleta)
                    self.exibir_tela_recompensa()
                    self.atualiza_dados_fase()
                    self.apljogo.nova_palavra()
            self.atualiza_tela()
            for obstaculo in self.apljogo.lobstaculos:
                if self.apljogo.verifica_colisao_personagem(self.imagempersonagem, obstaculo):
                    if self.apljogo.letra_esperada(obstaculo.nome):
                        self.telajogo.exibe_som(self.somletracerta)
                        self.apljogo.realiza_acao()
                    else:
                        self.apljogo.incrementa_dicionario_erros(obstaculo.nome)
                        self.apljogo.penaliza_jogador()
                        self.telajogo.exibe_som(self.somletraerrada)
                        self.palavraserradas.append(self.apljogo.palavras.palavra_atual())
                        self.apljogo.regride_fase()
                        if self.apljogo.voltoufase:
                            self.atualiza_dados_fase()
                            self.apljogo.nova_palavra()
                    break
            if self.apljogo.fimdejogo:
                self.aplcadastrarjogador.cadastrar_pontuacao(jogador, nomemodulo, self.apljogo.pontos)
                self.aplpersistencia.registra_erros_partida(self.apljogo.dicerros, jogador.login[0],
                                                            "LogPegueLetras.csv")
                self.exibir_fim_de_jogo(self.apljogo.pontos, self.palavrascertas, self.palavraserradas)
                self.continuarjogo = False
        self.exibir_musica("music1.mp3")