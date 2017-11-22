from ciu.cci.ControladorJogo import ControladorJogo
from ciu.cci.ControladorJogoAlfa import ControladorJogoAlfa
from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu
from ciu.cci.ControladorLogin import ControladorLogin

__author__ = 'Hanna'


class EstadoMenuPegueLetras(EstadoMenu):
    TELADADOINVALIDO = "telaloginerro.png"

    def __init__(self, menu):
        self.menu = menu
        self.jogador = ""
        self.nomemodulo = "pegueletras"

    def proximo_valor(self):
        self.menu.set_estado(self.menu.estadomenuvamosdigitar)

    def valor_anterior(self):
        pass

    def selecionar_valor(self):
        telalogin = ControladorLogin()

        telalogin.exibe_tela_informar_dados()
        if telalogin.cadastro():
            self.jogador = telalogin.requisita_jogador()
            controladorjogoalfa = ControladorJogoAlfa()
            controladorjogoalfa.jogo(self.jogador, self.nomemodulo)
        else:
            telalogin.exibe_tela_mensagem_retorno(self.TELADADOINVALIDO)
            self.menu.aguarda_confirmacao()