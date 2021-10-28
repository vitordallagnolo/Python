#Um professos que sortear um de seus 4 alunis para papagar o quadro
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
a1 = input('Insira o nome do primeiro aluno: ')
a2 = input('Insira o nome do segundo aluno: ')
a3 = input('Insira o nome do terceiro aluno: ')
a4 = input('Insira o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
