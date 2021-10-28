"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
#Meu programa
from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
op = ''
while op != 5:
    op = int(input('''
Escolha a operação:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
    '''))
    if op == 1:
        print('SOMAR: {} + {} = {}.'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('MULTIPLICAR: {} x {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('MAIOR: {} é o MAIOR.'.format(n1))
        elif n2 > n1:
            print('MAIOR: {} é o MAIOR'.fomart(n2))
        elif n1 == n2:
            print('MAIOR: Os números informados são iguais.')
    elif op == 4:
        print('Insira novos valores')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando')
    else:
        print('Opção inválida!')
    sleep(1.5)

#Concluído com sucesso!

#Professor
