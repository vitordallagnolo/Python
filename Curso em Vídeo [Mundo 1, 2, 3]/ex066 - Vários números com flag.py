'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condicação de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''
print('#Meu Programa')
count = soma = 0
while True:
    n = int(input('[\033[1m999 para sair]\033[m. Insira um número: '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'Você digitou {count} número(s) e a soma entre eles é {soma}.')
print('Acabou')
"""
print('#Programa Professor com gambiarra')
num = soma = 0
while num != 999:
    num = int(input('Digite um valor (999 para parar): ')
    soma += num
soma -= 999
print(f'A soma dos valores foi {soma}!')
"""
"""
print('#Programa Professor')
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): ')
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
"""

#Finalizado com Sucesso!