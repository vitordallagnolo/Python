"""
Escreva um programa que leia o número n inteiro qualquer e mostre na tela os
n primeiros elementos de uma Sequência de Fibonacci
Ex:
0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print('#Meu Programa')
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Insira um número para a Sequência de Fibonacci: '))
t1 = 0
t2 = 1
count = n - 2
print(t1,'→',t2, end=' → ')
while count != 0:
    t3 = t1 + t2
    print(t3, end=' → ')
    t1 = t2
    t2 = t3
    count -= 1
print('FIM')


print('#Programa Professor')
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos vocês quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → Fim')
print('~'*30)
