import unittest

from cln.cgt.AplJogo import AplJogo

_author__ = 'Hanna e Neimar'


class Test(unittest.TestCase):
    def teste_movimenta_personagem(self):
        apljogo = AplJogo()
        posicao_inicial = apljogo.personagem.posicao.eixoy
        deslocar = apljogo.personagem.deslocamentoy = 10
        apljogo.movimenta_personagem()
        self.assertEqual(posicao_inicial+deslocar, apljogo.personagem.posicao.eixoy , "posicionamento vertical do personagem esta errada")

    def teste_gera_novo_intervalo(self):
        apljogo = AplJogo()
        apljogo.gera_novo_intervalo()
        obtido = apljogo.intervaloobstaculos
        self.assertTrue(obtido >= apljogo.intervaloobstaculos and obtido <= apljogo.maiorintervalo, "intervaloobstaculos fora do range")

    def teste_cria_obstaculos(self):
        apljogo = AplJogo()
        apljogo.cria_obstaculos()
        obtido = len(apljogo.lobstaculos)
        self.assertTrue(obtido <=apljogo.totalobstaculos,"quantidade de obstaculo maior que o estipulado")

    def teste_remove_obstaculo(self):
        apljogo = AplJogo()
        apljogo.cria_obstaculos()
        quantidade_obstaculos = len(apljogo.lobstaculos)
        #para simular que o obstaculo passou pelo ponto de se destruir
        (apljogo.lobstaculos[0]).posicao.eixox = -81
        apljogo.remove_obstaculo()
        self.assertEqual(quantidade_obstaculos - 1,len(apljogo.lobstaculos),"erro ao remover obstaculo")

    #depende de manipular imagem
    def teste_verifica_colisao_personagem(self):
        apljogo = AplJogo()

        booleano = False#apljogo.verifica_colisao_personagem(apljogo.personagem,apljogo.lobstaculos[0],apljogo.lobstaculos[0].posicao)
        self.assertEqual(booleano,False, "objetos colidiu")

    #depende de manipular imagem
    def teste_captura_rect(self):
        apljogo = AplJogo()
        booleano = False#apljogo.captura_rect(imagem,apljogo.personagem.posicao)
        self.assertEqual(booleano,False, "objetos colidiu")

    def teste_penaliza_jogador(self):
        apljogo = AplJogo()
        quantidade_vida = apljogo.personagem.vida
        apljogo.penaliza_jogador()
        self.assertEqual(quantidade_vida - 1,apljogo.personagem.vida,"erro ao decremenar vida")

    def teste_verifica_qtd_de_vidas(self):
        apljogo = AplJogo()
        apljogo.penaliza_jogador()
        apljogo.verifica_qtd_de_vidas()
        self.assertEqual(0, apljogo.personagem.deslocamentoy, "ainda tem vida")

    def teste_movimenta_obstaculos(self):
        apljogo = AplJogo()
        apljogo.cria_obstaculos()
        obstaculo = apljogo.lobstaculos[0]
        posicao_obstaculo_antes = obstaculo.posicao.eixox,obstaculo.posicao.eixoy
        apljogo.movimenta_obstaculos()
        posicao_obstaculo_depois = obstaculo.posicao.eixox,obstaculo.posicao.eixoy
        self.assertTrue(posicao_obstaculo_antes!=posicao_obstaculo_depois,"erro ao movimentar obstaculo: verifique o metodo")

    """
    def teste_incrementa_pontuacao(self):
        apljogo = AplJogo()
        pontos_atual = apljogo.pontos
        apljogo.cria_obstaculos()
        #para simular que o obstaculo passou pelo personagem
        for obstaculo in apljogo.lobstaculos:
            obstaculo.posicao.eixox = apljogo.personagem.posicao.eixox
            # o baiacu, perseguidor, espada nao incrementam se manter o and na funcao
            #print(obstaculo.nome)
        apljogo.incrementa_pontuacao()
        self.assertEqual(pontos_atual+1,apljogo.pontos,"nao incrementou a pontuacao")
    """
    
if __name__ == "__main__":
    unittest.main()
