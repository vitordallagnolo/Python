"""
Crie um programa que vai gerar 5 números aleatórios e colocar
em uma tupla.

Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""
from random import randint
numeros = (randint(1, 10),randint(1, 10),randint(1, 10),
     randint(1, 10),randint(1, 10))
print(f'Os valores sorteados foram: {numeros}')
#ou
"""print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
"""
print(f'O menor valor é o {sorted(numeros)[0]}')
#print(f'O mario valor é o {reversed(numeros)}')
print(f'O maior valor é {max(numeros)}.')
print(f'O menor valor é {min(numeros)}.')