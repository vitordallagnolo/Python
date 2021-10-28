"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato
"""
# Definir o dicionário
jogadores = {}
# Definir partidas
partidas = []
# Perguntar o nome e incluir no dicionário
jogadores['jogador'] = str(input('Jogador: '))
# Perguntar o número de jogos
tot = int(input('Jogos: '))
print('-=' * 15)
print('Gols Realizados')
print('-=' * 15)
# Perguntar os gols feitos em cada partida
for c in range(0, tot):
    partidas.append(int(input(f'Jogo {c+1}: ')))
jogadores['gols'] = partidas[:]
# Contador de gols totais
jogadores['total'] = sum(partidas)
print('-=' * 30)
print(jogadores)
print('-=' * 30)
for k, v in jogadores.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogadores["jogador"]} jogou {len(jogadores["gols"])} partidas.')
for i, v in enumerate(jogadores['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogadores["total"]} gols.')

