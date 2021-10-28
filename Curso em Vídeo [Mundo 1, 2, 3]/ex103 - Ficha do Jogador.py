"""
Faça um programa que tenha uma função chamada
ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
ex:
nome:
gols:
o jogador tal fez tantos gols.
"""


def ficha(jog = '<desconhecido>' , gols = 0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')


#Programa Principal
jogador = str(input('Qual o jogador? '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)

