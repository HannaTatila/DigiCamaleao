from random import randint

from cln.cdp.Posicao import Posicao

_author__ = 'Hanna'


class EstiloElementos:

    @staticmethod
    def posicao_personagem():
        return Posicao(30, 250)

    @staticmethod
    def posicao_inimigo():
        return Posicao(700, randint(0, 445))

    @staticmethod
    def posicao_imagem_fundo():
        return Posicao(0, 0)

    @staticmethod
    def posicao_pontuacao():
        return Posicao(10, 50)

    @staticmethod
    def posicao_mensagem():
        return Posicao(250, 50)

    @staticmethod
    def posicao_mensagem_fim_jogo():
        return Posicao(200, 30)

    @staticmethod
    def get_posicao_vida(numvida):
        return Posicao((numvida * 36) + 10, 8)

    @staticmethod
    def posicao_titulo_jogo():
        return Posicao(205, 85)

    @staticmethod
    def posicao_mensagem_cadastro():
        return Posicao(150, 50)

    @staticmethod
    def posicao_mensagem_voltar():
        return Posicao(280, 65)