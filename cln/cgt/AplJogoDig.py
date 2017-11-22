import time
from random import randint

import pygame

from cln.cdp.Obstaculo import Obstaculo
from cln.cdp.Posicao import Posicao
from cln.cgt.AplJogo import AplJogo


class AplJogoDig(AplJogo):
    ACRESCIMO_VELOCIDADE = 0.15 #0.4
    ACRESCIMO_FREQUENCIA = 0.9

    def __init__(self):
        AplJogo.__init__(self)
        self.totalobstaculos = 3
        self.deslocamentoobstaculos = 0.9 #1.8
        self.intervaloobstaculos = 8 #5
        self.valorprogressao = 2
        self.pontosacumulados = 0
        self.mudoupontuacao = False
        self.listacenarios = ["mar", "deserto", "mata", "ceu", "espaco"]
        self.idcenario = 0
        self.novafase = False
        self.voltoufase = False
        self.pontosporfase = 4
        self.pontosacumuladosfase = 0
        self.jogoconcluido = False
        self.letraerrada = False
        self.dicerros = {}


    def incrementa_dicionario_erros(self, letradigitada, letraesperada):
        chave = (letradigitada.upper(), letraesperada.upper())
        if self.dicerros.has_key(chave):
            self.dicerros[chave] += 1
        else:
           self.dicerros[chave] = 1

    def realiza_acao(self, letradigitada):
        if self.palavras.tem_palavra():
            letraesperada = self.palavras.letra_esperada()
            if letraesperada == letradigitada:
                self.palavras.proxima_letra()
            else:
                self.incrementa_dicionario_erros(letradigitada, letraesperada)
                self.letraerrada = True

    def aumenta_dificuldade(self):
        self.deslocamentoobstaculos += self.ACRESCIMO_VELOCIDADE
        self.intervaloobstaculos -= self.ACRESCIMO_FREQUENCIA
        self.atualiza_deslocamento_obstaculos()

    def diminui_dificuldade(self):
        self.deslocamentoobstaculos -= self.ACRESCIMO_VELOCIDADE
        self.intervaloobstaculos += self.ACRESCIMO_FREQUENCIA
        self.atualiza_deslocamento_obstaculos()

    def verifica_troca_fase(self):
        if self.pontosacumuladosfase == self.pontosporfase:
            if self.idcenario < len(self.listacenarios) - 1:
                self.novafase = True
                self.pontosacumuladosfase = 0
                self.idcenario +=1
                self.aumenta_dificuldade()
                #self.pontosporfase += 2

    def regride_fase(self):
        if self.idcenario != 0:
            self.idcenario -=1
            self.pontosacumuladosfase = 0
            self.diminui_dificuldade()
            self.voltoufase = True
            #self.pontosporfase -= 2

    def cria_obstaculos(self):
        if len(self.lobstaculos) < self.totalobstaculos:
            if time.clock() - self.tempoinicial > self.intervaloobstaculos or not self.lobstaculos:
                self.tempoinicial = time.clock()
                palavra = self.palavras.nova_palavra()
                self.palavras.acrescenta_palavra(palavra)
                obstaculo = Obstaculo(palavra,
                                      Posicao(self.limiteinicio, randint(self.limitesuperior, self.limiteinferior)),
                                      self.deslocamentoobstaculos)
                self.lobstaculos.append(obstaculo)

    def remove_obstaculo(self):
        if self.lobstaculos:
            self.lobstaculos.pop(0)
            self.palavras.proxima_palavra()

    def incrementa_pontuacao(self):
        self.pontos += 1
        self.pontosacumuladosfase += 1
        self.mudoupontuacao = True
        if self.pontos > 20:
            self.pontosacumulados += 1
        self.verifica_troca_fase()

    def verifica_colisao_personagem(self, obstaculo):
        return self.personagem.posicao.eixox >= obstaculo.posicao.eixox

    def jogar(self):
        self.cria_obstaculos()
        self.movimenta_obstaculos()
        self.verifica_qtd_de_vidas()
        pygame.display.flip()
        self.clock.tick(60)

        """
        def atualiza_dificuldade(self):
        if self.mudoupontuacao:
            if self.pontos < 20:
                if self.pontos % self.valorprogressao == 0 and self.intervaloobstaculos > 2:
                    self.intervaloobstaculos -= 0.5
            else:
                if self.pontosacumulados < 15 and self.deslocamentoobstaculos < 7:
                    self.deslocamentoobstaculos += 0.4
                    self.atualiza_deslocamento_obstaculos()
                elif self.pontosacumulados < 25:
                    if self.intervaloobstaculos >= 0.3:
                        self.intervaloobstaculos -= 0.2
                elif self.deslocamentoobstaculos < 8:
                    self.deslocamentoobstaculos += 0.1
                    self.atualiza_deslocamento_obstaculos()
            self.mudoupontuacao = False
        """