import time

import pygame

from cln.cdp.ManipulaArquivo import ManipulaArquivo
from cln.cdp.Palavras import Palavras
from cln.cdp.Personagem import Personagem

_author__ = 'Hanna'

class AplJogo:
    def __init__(self):
        self.personagem = Personagem()
        #self.personagem.modifica_posicao(50, self.personagem.posicao.eixoy)
        self.palavras = Palavras([])
        self.lobstaculos = list()
        self.limiteinicio = 700
        self.limitesuperior = 120
        self.limiteinferior = 400
        self.tempoinicial = time.clock()
        self.pontos = 0
        self.fimdejogo = False
        self.menorintervalo = 2.5
        self.maiorintervalo = 3.5


    def configuracao(self):
        self.clock = pygame.time.Clock()

    def captura_palavras(self, cenario):
        manipulaArquivo = ManipulaArquivo()
        nomeobstaculos = manipulaArquivo.get_nome_obstaculos(cenario)
        self.palavras = Palavras(nomeobstaculos)

    def atualiza_deslocamento_obstaculos(self):
        for obstaculo in self.lobstaculos:
            obstaculo.deslocamentox = self.deslocamentoobstaculos

    def movimenta_obstaculos(self):
        for obstaculo in self.lobstaculos:
            obstaculo.movimenta(self.limitesuperior, self.limiteinferior)

    def verifica_qtd_de_vidas(self):
        if self.personagem.acabou_vida():
            self.fimdejogo = True
            self.personagem.deslocamentoy = 0
            for obstaculo in self.lobstaculos:
                obstaculo.deslocamentox = 0


    def penaliza_jogador(self):
        self.personagem.vida -= 1
        self.remove_obstaculo()

    @staticmethod
    def captura_rect(imagem, posicao):
        return imagem.get_rect().move(posicao.eixox, posicao.eixoy)
