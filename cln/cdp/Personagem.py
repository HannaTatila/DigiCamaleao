from cln.cdp.EstiloElementos import EstiloElementos

_author__ = 'Hanna'


class Personagem:
    def __init__(self):
        self.vida = 3
        self.posicao = EstiloElementos.posicao_personagem()
        self.deslocamentoy = 0
        self.deslocamentox = 0
        self.imune = False

    def modifica_posicao(self, eixox, eixoy):
        self.posicao.eixox = eixox
        self.posicao.eixoy = eixoy

    def incrementa_vida(self):
        self.vida += 1

    def decrementa_vida(self):
        self.vida -= 1

    def acabou_vida(self):
        return self.vida <= 0

    def aumenta_deslocamento_y(self):
        self.deslocamentoy = 10

    def diminui_deslocamento_y(self):
        self.deslocamentoy = -10

    def aumenta_deslocamento_x(self):
        self.deslocamentox = 7

    def diminui_deslocamento_x(self):
        self.deslocamentox = -7

    def atingiu_limite_da_tela(self):
        chao = 390
        teto = 90
        cantoesquerdo = 630
        cantodireito = 0
        # if peixe encostar no chao ou no teto, ele nao ultrapassa a tela
        if self.posicao.eixoy > chao:
            self.posicao.eixoy = chao
        elif self.posicao.eixoy < teto:
            self.posicao.eixoy = teto
        if self.posicao.eixox > cantoesquerdo:
            self.posicao.eixox = cantoesquerdo
        elif self.posicao.eixox < cantodireito:
            self.posicao.eixox = cantodireito


    def torna_imune(self):
        self.imune = True

    def torna_desprotegido(self):
        self.imune = False