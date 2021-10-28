'''
Refaça o Desafio 009,
mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
'''
'''from time import sleep
print('=-='* 8)
print('TABUADA AUTOMATIZADA')
print('=-='* 8)
n = int(input('Insira um número para calcularmos a tabuada: '))
x = 0
print('CALCULANDO..')
sleep(1.5)
print('=-='* 8)
for t in range (0,10):
    x += 1
    print('{} x {} = {}'.format(n,x, n * x))
print('=-='* 8)
'''
from time import sleep
print('=-='* 8)
print('TABUADA AUTOMATIZADA')
print('=-='* 8)
n = int(input('Insira um número para calcularmos a tabuada: '))
print('CALCULANDO..')
sleep(1.5)
print('=-='* 8)
for c in range(1,11):
    print('{} x {:2} = {}'.format(n, c, n * c))

#Concluído com Sucesso!