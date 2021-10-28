"""
Crie um programa que tenha uma tupla com várias palavras
(não usar ascentos).
Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.
"""

palavras = ('Bateria', 'Salamandra',
            'Tesoura', 'Laranja', 'Carro',
            'Bicicleta', 'Rinoceronte')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'AaEeIiOoUu':
            print(letra, end=' ')
