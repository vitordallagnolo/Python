'''
Refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:

-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes

Desafio 035:
Desenvolva um programa que leia o
comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo
'''

print('-=-' * 8)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 8)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Com os segmentos informados, é possível formar um triângulo ', end = '')
    if a == b == c: #ou pode ser if a == b and b == c
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Com os segmentos informados, não é possível formar um triângulo')


#Concluído com Sucesso!