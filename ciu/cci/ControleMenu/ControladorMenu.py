import os

import pygame

from ciu.cci.ControladorJogo import ControladorJogo
from ciu.cci.ControleMenu.Menu import Menu
from ciu.cih.EventosTeclado import ObservableEventosTeclado
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna'


class ControladorMenu():
    POSICAOX_SETA = 165
    POSICAOY_SETA = 268
    POSICAOX_OPCAO_MENU = 222
    POSICAOY_OPCAO_MENU = 280
    DISTANCIA_OPCAO_MENU = 40
    TAMANHO_OPCAO_MENU_PADRAO = 25
    TAMANHO_OPCAO_MENU_SELECAO = 28
    COR_PRETO = (0, 0, 0)
    COR_CINZA = (80, 80, 80)

    def __init__(self):
        pygame.init()
        self.telamenu = TelaMenu()
        self.controladorjogo = ControladorJogo()
        self.lopcoes = ["PEGUE AS LETRAS", "VAMOS DIGITAR", "CADASTRAR", "RANKING", "SAIR"]
        self.menu = Menu()
        self.buscar_imagens_menu()

    @staticmethod
    def get_imagem_geral(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_geral(), nomeimagem))

    def exibir_musica(self):
        self.telamenu.exibe_musica(os.path.join(CaminhoRecursos.caminho_musicas(), "music1.mp3"))

    def buscar_imagens_menu(self):
        self.imagemfundomenu = self.get_imagem_geral("fundomenu.jpg")
        self.imagemtitulojogo = self.get_imagem_geral("titulojogo.png")
        self.imagemseta = self.get_imagem_geral("seta.png")

    def exibir_tela_menu(self):
        self.telamenu.exibe_imagem(self.imagemfundomenu, EstiloElementos.posicao_imagem_fundo())
        self.telamenu.exibe_imagem(self.imagemtitulojogo, EstiloElementos.posicao_titulo_jogo())

    def exibe_opcoes_menu(self):
        alteraposicao = 0
        for id, opcao in enumerate(self.lopcoes):
            tam = self.TAMANHO_OPCAO_MENU_PADRAO
            cor = self.COR_CINZA
            if id + 1 == self.menuselecao:
                tam = self.TAMANHO_OPCAO_MENU_SELECAO
                cor = self.COR_PRETO
            self.telamenu.exibe_texto_menu(opcao, tam, cor,
                                           Posicao(self.POSICAOX_OPCAO_MENU, self.POSICAOY_OPCAO_MENU + alteraposicao))
            alteraposicao += self.DISTANCIA_OPCAO_MENU


    def manipula_seta(self):
        self.telamenu.exibe_imagem(self.imagemseta, Posicao(self.POSICAOX_SETA, self.POSICAOY_SETA + 40 * (self.menuselecao - 1)))

    def update(self, observable):
        if observable.baixo:
            self.menu.alterar_opcao_menu_baixo()
            if (self.menuselecao >= 1) & (self.menuselecao < len(self.lopcoes)):
                self.menuselecao += 1
        elif observable.cima:
            self.menu.alterar_opcao_menu_cima()
            if (self.menuselecao > 1) & (self.menuselecao <= len(self.lopcoes)):
                self.menuselecao -= 1
        elif observable.enter:
            self.menu.selecionar_opcao_menu()

    def inicializa_menu(self):
        self.exibir_musica()
        pygame.mouse.set_visible(False)
        observable = ObservableEventosTeclado()
        observable.add_observer(self)
        self.menuselecao = 1
        while True:
            self.exibir_tela_menu()
            self.manipula_seta()
            self.exibe_opcoes_menu()
            observable.verifica_evento()
            pygame.display.update()
            pygame.display.flip()

        #self.controladorjogo.jogo(self.menu.estadomenuiniciar.jogador)

