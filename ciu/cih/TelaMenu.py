import os

import pygame
from pygame.mixer import music

from ciu.cih.TelaJogo import TelaJogo

_author__ = 'Hanna'


class TelaMenu(TelaJogo):
    COR_CINZA = (80, 80, 80)
    TAMANHO_FONTE_MENSAGEM = 25

    def __init__(self):
        TelaJogo.__init__(self)

    def exibe_texto_menu(self, texto, tam, cor, posicao):
        fonte = pygame.font.SysFont("Arial", tam, False, False)
        t = fonte.render(texto, True, cor)
        self.tela.blit(t, (posicao.eixox, posicao.eixoy))

    def exibe_mensagem_cadastro(self, texto, posicao):
        fonte = pygame.font.SysFont("Arial", self.TAMANHO_FONTE_MENSAGEM, False, False)
        t = fonte.render(texto, True, self.COR_CINZA)
        self.tela.blit(t, (posicao.eixox, (self.tamanhotelay / 2) + posicao.eixoy))

    def exibe_texto_dados(self, texto, tam, posicao):
        fonte = pygame.font.SysFont("Arial", tam, False, False)
        t = fonte.render(texto, True, self.COR_PRETO)
        self.tela.blit(t, (posicao.eixox, posicao.eixoy))


