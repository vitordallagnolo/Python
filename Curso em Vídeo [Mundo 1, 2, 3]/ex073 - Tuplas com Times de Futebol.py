"""
Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

A)Apenas os 5 primeiros colocados.
B)Os últimos 4 colocados da tabela.
C)Uma lista com os times em ordem alfabética.
D)Em que posição na tabela está o time da Chapecoense.
"""
times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo',
         'Bragantino', 'Corinthians', 'Internacional', 'Fluminense',
         'Athletico-PR', 'Cuiabá', 'Ceará', 'Atlético-GO',
         'São Paulo', 'Juventude', 'América-MG', 'Santos',
         'Bahia', 'Grêmio', 'Sport', 'Chapecoense')

print('-=' * 15)
print(f'Os 5 primeiros colocados são: {times[0:5]}') #A
print('-=' * 15)
print(f'Os 4 últimos colocados são: {times[-4:]}') #B
print('-=' * 15)
print(f'A lista dos times em ordem alfabética: {sorted(times)}') #C
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição.') #D
print('-=' * 15)