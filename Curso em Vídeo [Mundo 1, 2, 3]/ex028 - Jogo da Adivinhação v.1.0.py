'''
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
e peça para o usuário tentar advinhar.

O programa escreverá na tela se o usuário venceu ou perdeu.
'''

import random
import time
ia = int(random.randrange(0,5))
print('-=-' * 20) #Mensagem na tela
print('Vou pensar em um número entre 0 e 5. Tente advinhar...') #Gerando número randomico
print('-=-' * 20) #Mensagem na tela
n = int(input('De 0 à 5, qual número eu pensei? '))
print('Processando...')
time.sleep(3) #módulo que espera um tempo na tela até a próxima execução
print('Você escolheu {} e eu {}'.format(n, ia))
if n == ia:
    print('Hmmmmm espertinho, acertou!')
else:
    print('Não foi dessa vez, tente de novo!')

#Concluído com Sucesso!
