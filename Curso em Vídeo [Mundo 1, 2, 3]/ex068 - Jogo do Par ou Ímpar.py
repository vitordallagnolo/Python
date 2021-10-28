'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivos que ele conquistou no fim do jogo.
'''
from random import randint
win = 0
print('Vamos jogar PAR ou ÍMPAR')
while True:
    c = randint(0,10)
    n = int(input('Informe um número: '))
    choice = str(input('Você escolhe PAR ou ÍMPAR? [P/I]')).strip().upper()[0]
    if choice in 'pP':
        if (c + n) % 2 == 0:
            win += 1
            print(f'IA escolhe {c} e você escolhe {n}.')
            print(f'{c+n} é PAR!')
            print('Você Venceu!')
        else:
            print(f'IA escolhe {c} e você escolhe {n}.')
            print(f'{c+n} é ÍMPAR!')
            break
    elif choice in 'iI':
        if (c + n) % 2 != 0:
            win += 1
            print(f'IA escolhe {c} e você escolhe {n}.')
            print(f'{c+n} é ÍMPAR!')
            print('Você Venceu!')
        else:
            print(f'IA escolhe {c} e você escolhe {n}.')
            print(f'{c+n} é PAR!')
            break
    elif choice not in 'IipP':
        print('Opção Inválida')
print('Game Over')
print(f'Você ganhou {win} vezes.')

#Concluído com Sucesso!

