"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
menor = 0
maior = 0
for c in range(1,6):
    peso = float(input('Informe o peso da {}ª pessoa: Kg '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso foi {}Kg e o maior {}Kg'.format(menor, maior))
