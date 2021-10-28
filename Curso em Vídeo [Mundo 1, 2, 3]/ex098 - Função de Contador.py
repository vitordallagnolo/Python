"""
Faça um programa que tenha uma função chamada contador(),
que receba 3 parâmetros: inicio, fim e passo e realiza a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada.
"""
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    sleep(1.5)
    if i < f:
        cont = i
        while cont <=f:
            print(f'{cont} ', end ='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end ='')
            sleep(0.5)
            cont -= p
        print('FIM!')



def linha():
    print('-=' * 20)


# Programa Principal
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')),int(input('Passo: ')))
# Pode ser também por:
"""
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
"""
linha()
