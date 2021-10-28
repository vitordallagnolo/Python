'''
Escreva um programa que leia dois números inteiro e compare-os,
mostrando na tela uma mensagem:

-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais
'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 < n2:
        print('O PRIMEIRO ({}) é o MENOR'.format(n1))
        print('O SEGUNDO ({}) é o MAIOR'.format(n2))
elif n2 < n1:
        print('O PRIMEIRO ({}) é o MAIOR'.format(n1))
        print('O SEGUNDO ({}) é o MENOR'.format(n2))
else:
        print('Os números são iguais.')


#Concluído com sucesso!