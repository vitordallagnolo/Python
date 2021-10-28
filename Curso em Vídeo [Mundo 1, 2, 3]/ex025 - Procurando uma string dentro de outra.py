'''
Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.
'''
name = str(input('Qual seu nome completo? ')).strip() #Strip remove os espaços do nome
print('Seu nome tem Silva? {}'.format('silva' in name.lower()))
