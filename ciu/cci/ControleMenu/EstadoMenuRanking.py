from ciu.cci.ControladorRanking import ControladorRanking
from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu

__author__ = 'Hanna'


class EstadoMenuRanking(EstadoMenu):

    def __init__(self, menu):
        self.menu = menu

    def proximo_valor(self):
        self.menu.set_estado(self.menu.estadomenusair)

    def valor_anterior(self):
        self.menu.set_estado(self.menu.estadomenucadastrar)

    def selecionar_valor(self):
        controladorranking = ControladorRanking()
        controladorranking.retorna_ranking()
        self.menu.aguarda_confirmacao()
