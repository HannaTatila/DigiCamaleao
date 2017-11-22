from os import listdir
from os.path import isfile, join

from PIL import Image

from principal.CaminhoRecursos import CaminhoRecursos


class ManipulaArquivo:
    def get_nome_obstaculos(self, cenario):
        lpalavras = [arquivo for arquivo in listdir(CaminhoRecursos.caminho_imagens_obstaculosedu(cenario)) if
                     isfile(join(CaminhoRecursos.caminho_imagens_obstaculosedu(cenario), arquivo))]
        for idpalavra in range(0, len(lpalavras)):
            lpalavras[idpalavra] = lpalavras[idpalavra].replace(".png", "")
        return lpalavras

    def resize_imagem(self, nome, altura):
        imagem = Image.open(nome)
        largura = int(altura * imagem.width / imagem.height)
        novaimagem = imagem.resize((largura, altura), Image.ANTIALIAS)
        novaimagem.save(nome)