from random import randint

from cln.cdp.Posicao import Posicao

_author__ = 'Hanna e Neimar'


class EstiloElementos:
    @staticmethod
    def posicao_personagem():
        return Posicao(150, 250)

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
        return Posicao(200, 250)

    @staticmethod
    def get_posicao_vida(numvida):
        return Posicao(numvida * 40, 0)

    @staticmethod
    def posicao_titulo_jogo():
        return Posicao(150, 140)

    @staticmethod
    def posicao_mensagem_cadastro():
        return Posicao(160, 22)

    @staticmethod
    def posicao_mensagem_voltar():
        return Posicao(300, 70)
