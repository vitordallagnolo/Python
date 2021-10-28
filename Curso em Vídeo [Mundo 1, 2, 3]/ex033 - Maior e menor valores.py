'''
Faça um programa que leia três número e mostre qual é o maior e qual é o menor
'''
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o último número: '))
#Verificar o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    print('O menor número é o {}'.format(menor))
    print('O maior número é o {}'.format(maior))

#Concluído com Sucesso!