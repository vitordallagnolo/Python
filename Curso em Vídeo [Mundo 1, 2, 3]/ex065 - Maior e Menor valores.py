"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve pergutnar ao usuário se ele quer ou não continuar a digitar valores.
"""

print('============')
print('Meu Programa')
print('============')
from time import sleep
n = int(input('Insira um número: '))
count = 1
total = n
seguir = 's'
maior = n
menor = n
média = n / count
while seguir not in 'Nn':
    seguir = str(input('Deseja continuar? [S/N] ')).strip()
    if seguir in 'Ss':
        count += 1
        n = int(input('Insira mais um número: '))
        total += n
        média = total / count
        if menor > n:
            menor = n
        elif maior < n:
            maior = n
    elif seguir in 'Nn':
        print('Calculando..')
        sleep(2)
print('Você digitou {} número(s) e a média entre eles é de {:.2f}. O maior foi {} e o menor foi {}.'.format(count, média, maior, menor))
print('PROGRAMA FINALIZADO')

#Concluído com Sucesso!

print('==================')
print('Programa Professor')
print('==================')
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str('Quer continuar? [S/N]').upper().strip()
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
