'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
import random
import time
pe = 'pedra'
pa = 'papel'
te = 'tesoura'
lista = [pe, pa, te]
print('{:=^40}'.format(' JOKENPÔ '))
print('Pedra, Papel ou Tesoura?')
ia = random.choice(lista)
j = str(input('O que você escolhe? ')).strip().lower()
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ')
print('O computador escolheu {} e você escolheu {}'.format(ia.upper(),j.upper()))
time.sleep(0.2)
if ia == pe and j == 'tesoura':
    print('Você \033[1;31mPERDEU\033[m :(')
elif ia == te and j == 'papel':
    print('Você \033[1;31mPERDEU\033[m :(')
elif ia == pa and j == 'pedra':
    print('Você \033[1;31mPERDEU\033[m :(')
elif ia == pa and j == 'papel':
    print('\033[1;33mEMPATE\033[m!')
elif ia == pe and j == 'pedra':
    print('\033[1;33mEMPATE\033[m!')
elif ia == te and j == 'tesoura':
    print('\033[1;33mEMPATE\033[m!')
elif j != 'tesoura' or 'pedra' or 'papel':
    print('Opção inválida!')
else:
    print('\033[1;32mVocê venceu!! Parabéns!\033[m')

print('{:=^40}'.format(' SEGUNDO PROGRAMA '))
#Concluído com sucesso!
#OU

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

if computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

if computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

#Concluído com Sucesso!




