import os
import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE, K_TAB

from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from cln.cgt.AplPersistencia import AplPersistencia
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna'


class ControladorCadastro:
    TAMANHO_LETRA_DADOS = 24
    POSICAOX_LETRA_DADOS = 228
    POSICAO_INICIAL_DADOS = 292
    INCREMENTA_ESPACAMENTO = 40
    TAMANHO_PALAVRA = 20
    POSICAO_SUBMIT = Posicao(372, 400)
    COR_PRETO = (0, 0, 0)
    COR_BRANCO = (255, 255, 255)
    TAMANHO_LETRA_MENU = 25
    POSICAOX_OPCAO_MENU = 115
    POSICAOY_INICIAL_OPCAO_MENU = 290

    def __init__(self):
        self.telamenu = TelaMenu()
        self.aplcadastrarjogador = AplPersistencia()
        self.lopcoes = ["LOGIN:", "SENHA:"]
        self.nomecorrente = []
        self.nome = ""
        self.posicaoimprimenome = self.POSICAO_INICIAL_DADOS
        self.imagemtela = ""
        self.buscar_imagem_tela()
        self.camposenha = False


    @staticmethod
    def get_imagem_geral(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_geral(), nomeimagem))

    def buscar_imagem_tela(self):
        self.imagemtela = self.get_imagem_geral("telacadastro.png")

    def exibe_tela_informar_dados(self):
        self.telamenu.exibe_imagem(self.imagemtela, EstiloElementos.posicao_imagem_fundo())
        pygame.display.flip()

    def exibe_tela_mensagem_retorno(self, imagemtela):
        imagemtelamensagem = self.get_imagem_geral(imagemtela)
        self.telamenu.exibe_imagem(imagemtelamensagem, EstiloElementos.posicao_imagem_fundo())
        pygame.display.flip()

    @staticmethod
    def get_key():
        while True:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key

    def imprime_nome(self, dado, posicaoy):
        self.nome = ""
        for i in range(len(dado)):
                self.nome = self.nome + dado[i]
        palavraimpressa = self.nome
        if self.camposenha:
            palavraimpressa = "*" * len(self.nome)
        self.telamenu.exibe_texto_dados(palavraimpressa, self.TAMANHO_LETRA_DADOS, Posicao(self.POSICAOX_LETRA_DADOS, posicaoy))
        pygame.display.flip()

    def enviar_dados_jogador(self, ldadosjogador):
        return self.aplcadastrarjogador.cadastrar_jogador(ldadosjogador)

    def atualiza_entrada(self, ldadosjogador):
        self.exibe_tela_informar_dados()
        posicaoy = self.POSICAO_INICIAL_DADOS
        self.camposenha = False
        for dado in ldadosjogador:
            self.imprime_nome(dado, posicaoy)
            posicaoy += self.INCREMENTA_ESPACAMENTO
            if len(ldadosjogador) > 1:
                self.camposenha = True

    def cadastro(self):
        ldadosjogador = []
        while True:
            self.tecla = self.get_key()
            if self.tecla == K_RETURN or self.tecla == K_TAB:
                ldadosjogador.append(self.nome)
                self.nome = ""
                self.nomecorrente = []
                if len(ldadosjogador) == len(self.lopcoes):
                    self.posicaoimprimenome = self.POSICAO_INICIAL_DADOS
                    return self.enviar_dados_jogador(ldadosjogador)
                else:
                    self.posicaoimprimenome = self.posicaoimprimenome + self.INCREMENTA_ESPACAMENTO
                    self.camposenha = True
            elif self.tecla == K_BACKSPACE:
                if len(self.nomecorrente) > 0:
                    self.nomecorrente.pop(-1)
                    ldadosjogador.append(self.nomecorrente)
                    self.atualiza_entrada(ldadosjogador)
                    ldadosjogador.pop(-1)
            elif self.tecla == K_ESCAPE:
                return []
            elif self.tecla <= 127 and len(self.nomecorrente) < self.TAMANHO_PALAVRA:
                self.nomecorrente.append(chr(self.tecla))
                self.imprime_nome(self.nomecorrente, self.posicaoimprimenome)
