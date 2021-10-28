"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores
e dizer qual é o maior.
"""
#Meu Programa
"""
import time
def maior(lst):
    mai = 0
    c = 0
    for n in números:
        if c == 0:
            mai = n
            c += 1
        elif c != 0 and n > mai:
            mai = n
    print(f'Você inseriu {len(lst)} valores.')
    print(f'O maior valor digitado foi: {mai}')





def linha():
    print('-' * 20)

números = []

linha()
print(f'{"Insira os Valores":^20}')
linha()

time.sleep(1)

total = 1
while True:
    n = int(input(f'{total}º Valor: '))
    if n in números:
        print('Você já incluiu este número antes.')
    else:
        total += 1
        números.append(n)
    print(números)
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
time.sleep(1)
linha()
maior(números)
linha()
"""
#Programa Professor

from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end = '')
        sleep(.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#Programa Principal
maior(2, 3, 1, 7, 8, 9, 66, 76, 56, 34, 34, 23, 2)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
