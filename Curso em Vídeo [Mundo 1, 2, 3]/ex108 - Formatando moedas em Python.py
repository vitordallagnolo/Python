import moeda1

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda1.moeda(p)} é {moeda1.moeda(moeda1.metade(p))}')
print(f'O dobro de {moeda1.moeda(p)} é {moeda1.moeda(moeda1.dobro(p))}')
print(f'Aumentando 10%, temos {moeda1.moeda(moeda1.aumentar(p, 10))}')

"""Adapte o código do desafio 107,
criando uma função adicional chamada moeda() que
consiga mostrar os valores como um valor monetário formatado

formatar os valores.
"""