"""
Crie um programa que lei o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato.
"""
print('#Meu Programa')
a = b = c = 0
nmb = ''
print('==========================')
print('Mercado LevaTudo DeixaNada')
print('==========================')
while True:
    nome = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o valor do produto? R$'))
    a += preço
    if c == 0 or c > preço:
        c = preço
        nmb = nome
    elif preço > 1000:
        b += 1
    siga = str(input('Deseja Continuar? [S/N]')).strip()
    if siga in 'Nn':
        break
    while siga not in 'NnSs':
        print('Opção Inválida!')
        siga = str(input('Deseja Continuar? [S/N]')).strip()

print(f'O valor total da compra é R${a}')
print(f'{b} produtos custam mais que R$1.000,00')
print(f'O produto mais barato é o {nmb}, que custa R${c:.2f}')

#Concluído com sucesso

print('Programa Professor')

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')