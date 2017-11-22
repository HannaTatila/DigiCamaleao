import os
import pygame
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from cln.cgt.AplPersistencia import AplPersistencia
from principal.CaminhoRecursos import CaminhoRecursos

__author__ = 'Hanna'

class ControladorRanking:
    TAMFONTETEXTO = 35
    POSICAOXNOME = 110
    POSICAOXPONTUACAO = 448
    ESPACAMENTONOMES = 43
    POSICAOYLINHA_PEGUE_LETRAS = 153
    POSICAOYLINHA_VAMOS_DIGITAR = 333

    def __init__(self):
        self.telamenu = TelaMenu()
        self.aplcadjog = AplPersistencia()

    @staticmethod
    def get_imagem_geral(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_geral(), nomeimagem))

    def exibir_tela_ranking(self):
        imagem = self.get_imagem_geral("telaranking.png")
        self.telamenu.exibe_imagem(imagem, EstiloElementos.posicao_imagem_fundo())

    def imprimir_ranking(self, lrecordes, posicaoy):
        posicaoylinha = posicaoy
        for linha in lrecordes:
            self.telamenu.exibe_texto(str(linha[0][0]), self.TAMFONTETEXTO, Posicao(self.POSICAOXNOME, posicaoylinha))
            self.telamenu.exibe_texto(str(linha[1]), self.TAMFONTETEXTO, Posicao(self.POSICAOXPONTUACAO, posicaoylinha))
            posicaoylinha += self.ESPACAMENTONOMES

    def retorna_ranking(self):
        self.exibir_tela_ranking()
        lrecordepegueletras, lrecordesvamosdigitar = self.aplcadjog.buscar_rankings()
        self.imprimir_ranking(lrecordepegueletras, self.POSICAOYLINHA_PEGUE_LETRAS)
        self.imprimir_ranking(lrecordesvamosdigitar, self.POSICAOYLINHA_VAMOS_DIGITAR)
        pygame.display.flip()



