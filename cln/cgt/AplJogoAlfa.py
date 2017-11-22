import random
import string
import time
from random import randint

import pygame
from pygame.rect import Rect

from cln.cdp.Obstaculo import Obstaculo
from cln.cdp.Posicao import Posicao
from cln.cgt.AplJogo import AplJogo


class AplJogoAlfa(AplJogo):
    def __init__(self):
        AplJogo.__init__(self)
        self.totalobstaculos = 5
        self.intervaloobstaculos = 0
        self.menorintervalo = 1.2#1.6 #1.3
        self.maiorintervalo = 1.5#1.8 #2
        self.deslocamentoobstaculos = 5#3.5
        self.tamanholetra = 40
        self.chanceinicio = 0
        self.chanceextra = 0.15
        self.chanceletraesperada = self.chanceinicio
        self.listacenarios = ["mar", "deserto", "mata", "ceu", "espaco"]
        self.idcenario = 0
        self.novafase = False
        self.pontosporfase = 1
        self.pontosacumuladosfase = 0
        self.dicerros = {}
        self.voltoufase = False


    def nova_palavra(self):
        self.palavras.acrescenta_palavra(self.palavras.nova_palavra())

    def reinicia_chances(self):
        self.chanceletraesperada = self.chanceinicio

    def melhora_chance(self):
        self.chanceletraesperada += self.chanceextra

    def letra_esperada(self, letra):
        return self.palavras.letra_esperada() == letra

    def realiza_acao(self):
        self.palavras.proxima_letra()

    def reinicia_deslocamento(self):
        self.deslocamentoobstaculos = 3
        self.atualiza_deslocamento_obstaculos()

    def reinicia_lista_obstaculos(self):
        self.lobstaculos = []
        #self.cria_obstaculos()

    def gera_novo_intervalo(self):
        self.intervaloobstaculos = random.uniform(self.menorintervalo, self.maiorintervalo)

    def cria_obstaculos(self):
        if len(self.lobstaculos) < self.totalobstaculos:
            if time.clock() - self.tempoinicial > self.intervaloobstaculos or not self.lobstaculos:
                self.tempoinicial = time.clock()
                self.gera_novo_intervalo()
                letra = self.get_letra()
                obstaculo = Obstaculo(letra,
                                      Posicao(self.limiteinicio, randint(self.limitesuperior, self.limiteinferior)),
                                      self.deslocamentoobstaculos)
                self.lobstaculos.append(obstaculo)

    def get_letra(self):
        if random.random() < self.chanceletraesperada:
            letra = self.palavras.letra_esperada()
        else:
            letra = random.choice(string.ascii_letters).lower()
        if letra == self.palavras.letra_esperada():
            self.reinicia_chances()
        else:
            self.melhora_chance()
        return letra

    def incrementa_dicionario_erros(self, letracoletada):
        letraesperada = self.palavras.letra_esperada()
        chave = (letracoletada.upper(), letraesperada.upper())
        if self.dicerros.has_key(chave):
            self.dicerros[chave] += 1
        else:
           self.dicerros[chave] = 1

    def remove_obstaculo(self):
        for id, obstaculo in enumerate(self.lobstaculos):
            if obstaculo.posicao.eixox < -80:
                del self.lobstaculos[id]

    def verifica_limite_da_tela(self):
        self.personagem.atingiu_limite_da_tela()

    def movimenta_personagem(self):
        self.personagem.modifica_posicao(self.personagem.posicao.eixox + self.personagem.deslocamentox,
                                         self.personagem.posicao.eixoy + self.personagem.deslocamentoy)

    def verifica_colisao_personagem(self, imagempersonagem, obstaculo):
        rectpersonagem = self.captura_rect(imagempersonagem, self.personagem.posicao)
        rectobstaculo = self.captura_rect_letra(obstaculo.posicao).inflate(-50, -50)
        colidiu = rectpersonagem.colliderect(rectobstaculo)
        if colidiu and obstaculo.ehtangivel and not self.personagem.imune:
            obstaculo.torna_intangivel()
            return colidiu
        return False

    def captura_rect_letra(self, posicao):
        return Rect((posicao.eixox, posicao.eixoy), (self.tamanholetra, self.tamanholetra))

    def incrementa_pontuacao(self):
        self.pontos += 1
        self.pontosacumuladosfase += 1

    def verifica_troca_fase(self):
        if self.pontosacumuladosfase == self.pontosporfase and self.idcenario < len(self.listacenarios) - 1:
            self.novafase = True
            self.pontosacumuladosfase = 0
            self.idcenario += 1
            self.deslocamentoobstaculos += 0.5
            self.atualiza_deslocamento_obstaculos()
            #self.pontosporfase += 2
            self.maiorintervalo -= 0.1

    def regride_fase(self):
        if self.idcenario != 0:
            self.idcenario -=1
            self.pontosacumuladosfase = 0
            self.deslocamentoobstaculos -= 0.5
            self.atualiza_deslocamento_obstaculos()
            self.voltoufase = True
            #self.pontosporfase -= 2
            self.maiorintervalo += 0.1

    def jogar(self):
        self.movimenta_personagem()
        self.cria_obstaculos()
        self.movimenta_obstaculos()
        self.remove_obstaculo()
        self.verifica_limite_da_tela()
        self.verifica_qtd_de_vidas()
        pygame.display.flip()
        self.clock.tick(60)