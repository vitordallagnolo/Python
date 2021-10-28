"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex:
5! = 5x4x3x2x1 = 120
"""
#Meu programa
n = int(input('Digite um número: '))
fator = n - 1
fatorial = n
while fator > 0:
    fatorial = fatorial * fator
    fator = fator - 1
print('O FATORIAL de {} é {}.'.format(n, fatorial))

#Professor
"""
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
"""

n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.fornat(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c #f = f * c
    c -= 1 #c = c - 1
print('{}'.format(f))
#Concluído com Sucesso!


