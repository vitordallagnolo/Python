"""
Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e colocar na lista.
A segunda função vai mostrar a soma entre todos os pares sorteados.
"""
from time import sleep
from random import randint
#Meu Programa
"""
numbers = list()


def line():
    print('-=' * 15)


def sorteia():
    line()
    print(f'{"SORTEANDO NÚMEROS:":^30}')
    line()
    sleep(1)
    for c in range(1,6):
        n = randint(1, 10)
        print(f'{c}º número sorteado: {n}')
        numbers.append(n)
        sleep(.5)


def somaPar():
    sompar = 0
    sleep(1)
    line()
    print('Somando pares..')
    line()
    for num in numbers:
        if num % 2 == 0:
            sompar += num
    print(f'A soma dos números pares é: {sompar}.')


line()
print('Irei sortear 5 números para você!')
sleep(1)
line()
sorteia()
line()
print(f'Os números sorteados são: {numbers}.')
line()
somaPar()
line()
"""
#Programa Professor
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end ='')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end = '')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {lista}, temos {soma}.')

números = list()
sorteia(números)
somaPar(números)