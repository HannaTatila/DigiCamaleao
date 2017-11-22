import pygame
from pygame.mixer import music, Sound

_author__ = 'Hanna'


class TelaJogo:
    COR_BRANCO = (255, 255, 255)
    COR_PRETO = (0, 0, 0)
    COR_DARKBLUE = (0,0,139)
    COR_VERMELHO = (255, 0, 0)
    COR_CEU = (192, 217, 217)

    def __init__(self):
        #pygame.init()
        self.tamanhotelax = 700
        self.tamanhotelay = 500
        self.tela = pygame.display.set_mode((self.tamanhotelax, self.tamanhotelay))
        pygame.display.set_caption("DigiCamaleao")

    def exibe_imagem(self, imagem, posicao):
        self.tela.blit(imagem, (posicao.eixox, posicao.eixoy))

    def exibe_imagem_congelada(self, imagem, posicao):
        self.tela.blit(imagem, (posicao.eixox, posicao.eixoy))
        pygame.display.flip()
        pygame.time.delay(3500)

    def exibe_texto(self, texto, tamanhofonte, posicao):
        fonte = pygame.font.SysFont("Arial", tamanhofonte, False, False)
        text = fonte.render(texto, True, self.COR_BRANCO)
        self.tela.blit(text, (posicao.eixox, posicao.eixoy))

    def exibe_texto_personalizado(self, texto, tamanhofonte, posicao, cor):
        fonte = pygame.font.SysFont("Arial", tamanhofonte, False, False)
        text = fonte.render(texto, True, cor)
        self.tela.blit(text, (posicao.eixox, posicao.eixoy))

    @staticmethod
    def exibe_musica(musica):
        music.load(musica)
        music.play()

    @staticmethod
    def exibe_som(som):
        som = Sound(som)
        som.play()
