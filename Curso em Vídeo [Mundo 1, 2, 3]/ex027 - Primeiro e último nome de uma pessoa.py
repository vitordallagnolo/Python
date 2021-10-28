'''
Faça um programa que leia o nome completo de uma pessoa
e mostre o primeiro e o último nome separadamente
'''

n = str(input('Qual o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em conhecê-lo {}!'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
