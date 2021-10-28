'''
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
print('Meu Programa')
from time import sleep
print('=-='* 7)
print('TABUADA AUTOMATIZADA')
print('=-='* 7)
while True:
    n = int(input('Insira um número para calcularmos a tabuada: '))
    if n < 0:
        break
    print('CALCULANDO..')
    sleep(1)
    print('=-='* 8)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('=-=' * 8)
print('Programa finalizado')

#Finalizado com Sucesso!