import os

_author__ = 'Hanna'


class CaminhoRecursos:
    @staticmethod
    def caminho_imagens_geral():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "imagem"))

    @staticmethod
    def caminho_imagens(cenario):
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "imagem", cenario))

    @staticmethod
    def caminho_imagens_obstaculosedu(cenario):
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "imagem", cenario, "obstaculosedu"))

    @staticmethod
    def caminho_imagens_obstaculos_geral():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "imagem",
                                                                                  "obstaculosgeral"))

    @staticmethod
    def caminho_musica_partida(cenario):
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "imagem", cenario, "musicafundo.mp3"))


    @staticmethod
    def caminho_musicas():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "audio", "musica"))

    @staticmethod
    def caminho_sons():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "audio", "sons"))

    @staticmethod
    def caminho_log():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "log"))

    @staticmethod
    def diretorio():
        if os.path.basename(os.getcwd()) == "principal":
            return "principal"
        else:
            return os.path.join("library.zip", "principal")
