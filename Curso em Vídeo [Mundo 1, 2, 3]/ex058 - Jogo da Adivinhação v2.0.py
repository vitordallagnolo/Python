"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
#Meu programa
import random
import time
ia = int(random.randrange(0,10))
c = 1
print('-=-' * 20) #Mensagem na tela
print('Vou pensar em um número entre 0 e 10. Tente advinhar...') #Gerando número randomico
print('-=-' * 20) #Mensagem na tela
print('Pensando...')
n = int(input('Qual número eu pensei? '))
time.sleep(0.5) #módulo que espera um tempo na tela até a próxima execução
while n != ia:
    c += 1
    if n < ia:
        n = int(input('É maior, tente novamente:  '))
    else:
        n = int(input('É menor, tente novamente:  '))
print('Acertou!')
print('Você precisou de {} tentativa(s) para acertar.'.format(c))

"""
#Professor
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
"""