from ciu.cci.ControladorCadastro import ControladorCadastro

_author__ = 'Hanna'


class ControladorLogin(ControladorCadastro):

    def __init__(self):
        ControladorCadastro.__init__(self)
        self.login = ""

    def buscar_imagem_tela(self):
        self.imagemtela = self.get_imagem_geral("telalogin.png")

    def enviar_dados_jogador(self, ldadosjogador):
        return self.aplcadastrarjogador.validar_login(ldadosjogador)

    def requisita_jogador(self):
        return self.aplcadastrarjogador.requisitar_jogador()