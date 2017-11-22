import os

import pygame
import sys

from ciu.cih.EventosTeclado import ObservableEventosTeclado
from ciu.cih.TelaJogo import TelaJogo
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna'

class ControladorJogo:
    TAM_FONTE_PONTUACAO = 30
    TAM_FONTE_RESULTADO = 20
    DESLOCAMENTO_TELA = 2
    POSICAO_TROCA_TELA = -700
    COR_BRANCO = (255, 255, 255)
    COR_AZUL = (0, 0, 139)

    def __init__(self):
        pygame.init()
        self.telajogo = TelaJogo()
        self.posicaotela = EstiloElementos.posicao_imagem_fundo()
        self.buscar_imagem_pause()

    @staticmethod
    def get_obstaculo(nomeobstaculo, cenario):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_obstaculosedu(cenario), nomeobstaculo))

    @staticmethod
    def get_imagem_obstaculo_geral(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_obstaculos_geral(), nomeimagem))

    @staticmethod
    def get_imagem(nomeimagem, cenario):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens(cenario), nomeimagem))

    @staticmethod
    def get_imagem_geral(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_geral(), nomeimagem))

    @staticmethod
    def get_musica_partida(cenario):
        return os.path.join(CaminhoRecursos.caminho_musica_partida(cenario))

    @staticmethod
    def get_musica(nomemusica):
        return os.path.join(CaminhoRecursos.caminho_musicas(), nomemusica)

    @staticmethod
    def get_som(nomesom):
        return os.path.join(CaminhoRecursos.caminho_sons(), nomesom)

    def exibir_musica(self, nomemusica):
        self.telajogo.exibe_musica(self.get_musica(nomemusica))

    def exibir_musica_partida(self, cenario):
        self.telajogo.exibe_musica(self.get_musica_partida(cenario))

    def buscar_imagem_pause(self):
        self.imagempause = self.get_imagem_geral("pause.png")

    def exibir_tela_jogo(self, imagemfundo):
        self.telajogo.exibe_imagem(imagemfundo, self.posicaotela)
        self.anda_tela()

    def anda_tela(self):
        self.posicaotela.eixox -= self.DESLOCAMENTO_TELA
        if self.posicaotela.eixox == self.POSICAO_TROCA_TELA:
            self.posicaotela.eixox = 0

    def exibir_vidas(self, imagemvida):
        for numvida in range(self.apljogo.personagem.vida):
            self.telajogo.exibe_imagem(imagemvida, EstiloElementos.get_posicao_vida(numvida))

    def exibir_pontuacao(self, mensagem):
        self.telajogo.exibe_texto_personalizado(mensagem + str(self.apljogo.pontos), self.TAM_FONTE_PONTUACAO,
                                                EstiloElementos.posicao_pontuacao(), self.corletra)

    def redimensionar_imagem_obstaculo(self, imagem):
        imagem = pygame.transform.scale(imagem, (30, 30))
        return imagem

    def exibir_tela_instrucoes(self, nomeimagem):
        self.imageminstrucoes = self.get_imagem_geral(nomeimagem)
        self.telajogo.exibe_imagem(self.imageminstrucoes, EstiloElementos.posicao_imagem_fundo())
        pygame.display.flip()
        self.aguarda_confirmacao()

    @staticmethod
    def aguarda_confirmacao():
        espera = True
        while espera:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (e.type == pygame.KEYDOWN) and (e.key == pygame.K_RETURN):
                    espera = False

    def exibir_palavras_erradas(self, palavraserradas):
        if palavraserradas:
            self.telajogo.exibe_texto("Erros: ", self.TAM_FONTE_PONTUACAO, Posicao(25, 440))
            x = 120
            y = 440
            listapalavrasunicas = list(set(palavraserradas))
            for palavra in listapalavrasunicas:
                imagem = self.get_imagem_obstaculo_geral(palavra + ".png")
                self.telajogo.exibe_imagem(self.redimensionar_imagem_obstaculo(imagem), Posicao(x, y))
                self.telajogo.exibe_texto(palavra.upper(), self.TAM_FONTE_RESULTADO, Posicao(x + 45, y))
                x += 190

    def exibir_palavras_certas(self, palavrascertas):
        x = 25
        y = 100
        listapalavrasunicas = list()
        for palavra in palavrascertas:
            if palavra not in listapalavrasunicas:
                listapalavrasunicas.append(palavra)
                qtdacertos = palavrascertas.count(palavra)
                self.telajogo.exibe_texto(str(qtdacertos) + " X", self.TAM_FONTE_RESULTADO, Posicao(x, y))
                imagem = self.get_imagem_obstaculo_geral(palavra + ".png")
                self.telajogo.exibe_imagem(self.redimensionar_imagem_obstaculo(imagem), Posicao(x + 40, y))
                self.telajogo.exibe_texto(palavra.upper(), self.TAM_FONTE_RESULTADO, Posicao(x + 85, y))
                y += 60
                if y > 350:
                    x += 225
                    y = 100


    def exibir_fim_de_jogo(self, totalpontos, palavrascertas, palavraserradas):
        self.exibir_fundo_resultados()
        self.telajogo.exibe_texto(str(totalpontos) + " pontos", self.TAM_FONTE_PALAVRA, Posicao(350, 30)) #EstiloElementos.posicao_mensagem_fim_jogo())
        self.posicaotela.eixox = 0
        self.exibir_palavras_certas(palavrascertas)
        self.exibir_palavras_erradas(palavraserradas)
        pygame.display.flip()
        self.aguarda_confirmacao()

    def exibir_fundo_resultados(self):
        imagem = self.get_imagem_geral("telaresultado.png")
        self.telajogo.exibe_imagem(imagem, EstiloElementos.posicao_imagem_fundo())

    def exibir_mensagem(self, mensagem):
        self.telajogo.exibe_texto(mensagem, self.TAM_FONTE_PONTUACAO, EstiloElementos.posicao_mensagem())

    def atualiza_cor_letras(self):
        self.corletra = self.COR_BRANCO
        if self.listacenarios[self.apljogo.idcenario] == "ceu":
            self.corletra = self.COR_AZUL

    def atualiza_dados_fase(self):
        #self.telajogo.exibe_som(self.somtrocafase) # exibir som ao trocar de fase
        self.atualiza_cor_letras()
        self.apljogo.novafase = False
        self.busca_imagens_tela()
        self.apljogo.captura_palavras(self.listacenarios[self.apljogo.idcenario])

    def exibir_tela_recompensa(self):
        pygame.mixer.music.stop()
        telarecompensa = self.get_imagem("novafase.png", self.listacenarios[self.apljogo.idcenario])
        self.telajogo.exibe_imagem_congelada(telarecompensa, EstiloElementos.posicao_imagem_fundo())

    def paused(self, observable):
        self.telajogo.exibe_imagem(self.imagempause, EstiloElementos.posicao_imagem_fundo())
        pygame.display.update()
        while observable.space:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        observable.space = False

    def inicializa_observable(self):
        observable = ObservableEventosTeclado()
        observable.add_observer(self)
        return observable


