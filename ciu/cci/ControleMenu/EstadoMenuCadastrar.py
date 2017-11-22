from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu
from ciu.cci.ControladorCadastro import ControladorCadastro

__author__ = 'Hanna'

class EstadoMenuCadastrar(EstadoMenu):
    TELAMSGSUCESSO = "telacadsucesso.png"
    TELAMSGERRO = "telacaderro.png"

    def __init__(self, menu):
        self.menu = menu

    def proximo_valor(self):
        self.menu.set_estado(self.menu.estadomenuranking)

    def valor_anterior(self):
        self.menu.set_estado(self.menu.estadomenuvamosdigitar)

    def selecionar_valor(self):
        telacadastro = ControladorCadastro()
        telacadastro.exibe_tela_informar_dados()
        mensagemretorno = self.TELAMSGSUCESSO
        if not telacadastro.cadastro():
            mensagemretorno = self.TELAMSGERRO

        telacadastro.exibe_tela_mensagem_retorno(mensagemretorno)
        self.menu.aguarda_confirmacao()
