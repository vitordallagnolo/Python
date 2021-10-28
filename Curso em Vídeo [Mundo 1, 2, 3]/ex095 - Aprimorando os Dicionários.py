"""
Aprimore o DESAFIO 093 para que ele funcione com
vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""
time = list()
# Definir o dicionário
jogador = {}
# Definir partidas
partidas = []
while True:
    jogador.clear()
    # Perguntar o nome e incluir no dicionário
    jogador['jogador'] = str(input('Jogador: '))
    # Perguntar o número de jogos
    tot = int(input('Jogos: '))
    partidas.clear()
    print('-=' * 15)
    print('Gols Realizados')
    print('-=' * 15)
    # Perguntar os gols feitos em cada partida
    for c in range(0, tot):
        partidas.append(int(input(f'Jogo {c+1}: ')))
    jogador['gols'] = partidas[:]
    # Contador de gols totais
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responsa apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["jogador"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
