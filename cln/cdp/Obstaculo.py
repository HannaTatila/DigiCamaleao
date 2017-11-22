
_author__ = 'Hanna'


class Obstaculo:
    def __init__(self, nome, posicao, deslocamentox):
        self.nome = nome
        self.posicao = posicao
        self.deslocamentox = deslocamentox
        self.ehtangivel = True

    def movimenta(self, limitesuperior, limiteinferior):
        self.movimenta_horizontalmente()

    def movimenta_horizontalmente(self):
        self.posicao.eixox -= self.deslocamentox

    def torna_intangivel(self):
        self.ehtangivel = False

