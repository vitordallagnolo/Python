'''
Desenvolva um programa que leia o
comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo
'''
print('-=-' * 8)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 8)
a = float(input('Insira uma medida: '))
b = float(input('Insira outra medida: '))
c = float(input('Insira uma última medida: '))
if a < b + c and b < a + c and c < a + b:
    print('Com as medidas informadas, é possível formar um triângulo')
else:
    print('Com as medidas informadas, não é possível formar um triângulo')

#Concluído com sucesso!