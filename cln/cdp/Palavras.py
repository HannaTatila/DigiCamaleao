import random

class Palavras:
    def __init__(self, ltodaspalavras):
        self.ltodaspalavras = ltodaspalavras
        self.lpalavras = list()
        self.idletra = 0

    def tem_palavra(self):
        return len(self.lpalavras) > 0

    def indice_atual(self):
        return self.idletra

    def letra_esperada(self):
        if self.tem_palavra() and self.idletra < len(self.lpalavras[0]):
            return self.lpalavras[0][self.idletra]
        else:
            return ""

    def proxima_letra(self):
        self.idletra += 1

    def palavra_atual(self):
        if self.tem_palavra():
            return self.lpalavras[0]
        else:
            return ""

    def proxima_palavra(self):
        self.lpalavras.pop(0)
        self.idletra = 0

    def palavra_acabou(self):
        if self.tem_palavra():
            return len(self.lpalavras[0]) == self.idletra
        else:
            return False

    def acrescenta_palavra(self, palavra):
        self.lpalavras.append(palavra)

    def nova_palavra(self):
        return random.choice(self.ltodaspalavras)
