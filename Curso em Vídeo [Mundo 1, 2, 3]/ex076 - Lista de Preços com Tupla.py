"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
print('#Meu Programa + Professor')
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

lista = ('Computador', 5000.00,
         'Monitor', 2000.00,
         'Caderno', 15.00,
         'Lápis', 00.50,
         'Mochila', 25.00,
         'Estojo', 25.00,
         'Caneta', 2.50)
for pos in range(0, len(lista)):
    if pos % 2 == 0: #se o número for par, significa que é o nome por causa da posição
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)


