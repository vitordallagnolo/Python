"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('#Meu Programa')
print('=======')
print('RobBank')
print('=======')
v = int(input('Qual valor deseja sacar? R$'))
cinq = v // 50
vinte = dez = um = 0
restante = v - (cinq * 50)
print(f'Saque de R${v:.2f}')
print(f'{cinq} notas de R$50.00')
while True:
    if restante != 0:
        vinte = restante // 20
        restante -= (vinte * 20)
        print(f'{vinte} notas de R$20.00')
        if restante != 0:
            dez = restante // 10
            restante -= (dez * 10)
            print(f'{dez} notas de R$10.00')
            if restante != 0:
                um = restante // 1
                restante -= (um * 1)
                print(f'{um} notas de R$1.00')
    else:
        break

#print(f'O restante é {restante}')

#Concluído com Sucesso!

print('#Programa Professor')
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


