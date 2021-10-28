#Desenvolva um programa que leia as duas notas de um aluno , calcule e mostre a sua média.

n1 = float(input('Insira a nota 1 de 2: '))
n2 = float(input('Insira a nota 2 de 2: '))
med = (n1 + n2) / 2
print('Suas notas foram {} e {}, sua média ficou em {}'.format(n1, n2, med))
