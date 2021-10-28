"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, rescpectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
listapar = []
listaimpar = []
print('Digite 0000 para finalizar.')
while True:
    n = int(input('Insira um número: '))
    if n != 0000:
        if n % 2 == 0:
            lista.append(n)
            print('Número par registrado.')
            listapar.append(n)
        elif n % 2 != 0:
            lista.append(n)
            print('Número ímpar registrado.')
            listaimpar.append(n)
    else:
        break
print(f'A lista completa é: {lista}')
print(f'A lista dos números pares é: {listapar}')
print(f'A lista dos números ímpares é: {listaimpar}')

print('-=' * 30)
print('Programa Professor')
print('-=' * 30)

num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')