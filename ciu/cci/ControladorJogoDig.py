#coding: utf-8
import pygame

from ciu.cci.ControladorJogo import ControladorJogo
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from cln.cgt.AplPersistencia import AplPersistencia
from cln.cgt.AplJogoDig import AplJogoDig



class ControladorJogoDig(ControladorJogo):
    TAM_FONTE_PALAVRA = 30

    def __init__(self):
        ControladorJogo.__init__(self)
        self.listacenarios = ["mar", "deserto", "mata", "ceu", "espaco"]
        self.apljogo = AplJogoDig()
        self.aplcadastrarjogador = AplPersistencia()
        self.aplpersistencia = AplPersistencia()
        self.busca_sons_jogo()
        self.palavrascertas = list()
        self.palavraserradas = list()
        self.corletra = self.COR_BRANCO
        self.continuarjogo = True

    def busca_imagens_tela(self):
        self.imagempersonagem = self.get_imagem("personagem.png", self.listacenarios[self.apljogo.idcenario])
        self.imagemfundo = self.get_imagem("fundojogo.png", self.listacenarios[self.apljogo.idcenario])
        self.imagemvida = self.get_imagem("vida.png", self.listacenarios[self.apljogo.idcenario])
        self.imagemsetaindicadora = self.get_imagem_geral("setaletra.png")

    def busca_sons_jogo(self):
        self.somacerto = self.get_som("moeda.wav")
        self.somcolisao = self.get_som("colisao2.wav")
        self.somteclaerrada = self.get_som("colisao2.wav")
        self.somtrocafase = self.get_som("vitoria.wav")

    def exibir_palavra_digitacao(self, palavra, indice):
        faltam = len(palavra) - indice
        self.telajogo.exibe_texto_personalizado(palavra[:indice] + ("_ " * faltam), self.TAM_FONTE_PALAVRA,
                                  EstiloElementos.posicao_mensagem(), self.corletra)

    def exibir_letra_digitacao(self, letra, posicao):
        self.telajogo.exibe_texto_personalizado(letra, self.TAM_FONTE_PALAVRA, posicao, self.corletra)

    def exibir_pontuacao(self, mensagem):
        self.telajogo.exibe_texto_personalizado(mensagem + str(self.apljogo.pontos), self.TAM_FONTE_PONTUACAO,
                                  EstiloElementos.posicao_pontuacao(), self.corletra)

    def exibir_personagem(self):
        self.telajogo.exibe_imagem(self.imagempersonagem, self.apljogo.personagem.posicao)

    def atualiza_tela(self):
        self.exibir_tela_jogo(self.imagemfundo)
        self.exibir_personagem()
        if self.apljogo.lobstaculos:
            palavra = self.apljogo.palavras.palavra_atual().upper()
            indice = self.apljogo.palavras.indice_atual()
            self.exibir_palavra_digitacao(palavra, indice)
            posicaoletra = Posicao(self.apljogo.lobstaculos[0].posicao.eixox - 10,
                                   self.apljogo.lobstaculos[0].posicao.eixoy - 40)
            self.exibir_letra_digitacao(palavra[indice], posicaoletra)
            if self.apljogo.palavras.idletra == 0:
                posicaoseta = Posicao(self.apljogo.lobstaculos[0].posicao.eixox - 17,
                                       self.apljogo.lobstaculos[0].posicao.eixoy - 100)
                self.telajogo.exibe_imagem(self.imagemsetaindicadora, posicaoseta)
        for obstaculo in self.apljogo.lobstaculos:
            imagemobstaculo = self.get_obstaculo(obstaculo.nome + ".png", self.listacenarios[self.apljogo.idcenario])
            self.telajogo.exibe_imagem(imagemobstaculo, obstaculo.posicao)
        self.exibir_pontuacao("Pontos: ")
        self.exibir_vidas(self.imagemvida)

    # a classe ControlodorJogo (q eh um observador)recebe atualizacao pq a classe Observada ObservableEventosTeclado capturou um evento
    def update(self, observable):
        if observable.space:
            self.paused(observable)
        if observable.teclaletra:
            self.apljogo.realiza_acao(chr(observable.letra))
            if self.apljogo.letraerrada:
                self.telajogo.exibe_som(self.somteclaerrada)
                self.apljogo.letraerrada = False
        if observable.escape:
            self.continuarjogo = False
        #if (observable.enter) and (self.apljogo.fimdejogo):
        #    self.continuarjogo = False

    def atualiza_cor_letras(self):
        self.corletra = self.COR_BRANCO
        if self.listacenarios[self.apljogo.idcenario] == "ceu":
            self.corletra = self.COR_AZUL
        elif self.listacenarios[self.apljogo.idcenario] == "deserto":
            self.corletra = (128, 0, 0)

    def atualiza_dados_fase(self):
        #self.telajogo.exibe_som(self.somtrocafase) # exibir som ao trocar de fase
        self.exibir_musica_partida(self.listacenarios[self.apljogo.idcenario])
        self.atualiza_cor_letras()
        self.apljogo.novafase = False
        self.apljogo.voltoufase = False
        self.busca_imagens_tela()
        self.apljogo.captura_palavras(self.listacenarios[self.apljogo.idcenario])
        self.apljogo.lobstaculos = list()


    def jogo(self, jogador, nomemodulo):
        self.exibir_tela_instrucoes("instrucoesvd.jpg")
        observable = self.inicializa_observable()
        self.apljogo.configuracao()
        self.atualiza_dados_fase()
        while self.continuarjogo:
            observable.verifica_evento()
            self.apljogo.jogar()
            if self.apljogo.palavras.palavra_acabou():
                self.palavrascertas.append(self.apljogo.palavras.palavra_atual())
                self.apljogo.incrementa_pontuacao()
                self.telajogo.exibe_som(self.somacerto)
                self.apljogo.remove_obstaculo()
                if self.apljogo.novafase:
                    self.telajogo.exibe_som(self.somtrocafase)
                    self.exibir_tela_recompensa()
                    self.atualiza_dados_fase()
            self.atualiza_tela()
            for obstaculo in self.apljogo.lobstaculos:
                if self.apljogo.verifica_colisao_personagem(obstaculo):
                    self.telajogo.exibe_som(self.somcolisao)
                    self.palavraserradas.append(self.apljogo.palavras.palavra_atual())
                    self.apljogo.penaliza_jogador()
                    self.apljogo.regride_fase()
                    if self.apljogo.voltoufase:
                        self.atualiza_dados_fase()
                    break
            if self.apljogo.fimdejogo:
                self.aplcadastrarjogador.cadastrar_pontuacao(jogador, nomemodulo, self.apljogo.pontos)
                self.aplpersistencia.registra_erros_partida(self.apljogo.dicerros, jogador.login[0], "LogVamosDigitar.csv")
                self.exibir_fim_de_jogo(self.apljogo.pontos, self.palavrascertas, self.palavraserradas)
                self.continuarjogo = False
        self.exibir_musica("music1.mp3")