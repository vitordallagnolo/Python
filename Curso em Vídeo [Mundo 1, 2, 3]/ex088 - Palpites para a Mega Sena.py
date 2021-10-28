"""
Faça um programa que ajude um jogador da MEGASENA a criar palpites.
O programa vai pergutnar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando em uma lista composta.
"""
from random import randint
from time import sleep
lista = []
jogos = []
print('-=' * 30)
print('     JOGA NA MEGA SENA    ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

"""
from random import randint
gerados = []
randomizado = []
jogos = int(input('Quantos jogos deseja gerar? '))
for palpites in range(0, jogos):
    for sorteado in range(0,6):
        n = randint(1,60)
        randomizado.append(n)
    gerados.append(randomizado[:])
    randomizado.clear()
print(f'{gerados}')
print(f'{randomizado}')
print(f'{jogos}')
print(f'{palpites}')
print(f'{sorteado}')
"""