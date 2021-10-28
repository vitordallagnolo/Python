"""
Faça um programa que leia o nome e peso de várias pessoas
guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves
"""
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ) pessoas. }')
print(f'O maior peso foi de {mai}Kg ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men}Kg ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

"""
lista = list()
resp = 'ss'
pesado = list()
leve = list()
count = 0
while resp not in 'Nn':
    count += 1
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    lista.append(nome)
    lista.append(peso)
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()
    if count == 1:
        pesado.append(nome)
        pesado.append(peso)
        leve.append(nome)
        leve.append(peso)
    if peso > pesado[1]:
        pesado.clear()
        pesado.append(nome)
        pesado.append(peso)
    elif peso < leve[1]:
        leve.clear()
        leve.append(nome)
        leve.append(peso)
print(f'A) {count} pessoas foram cadastradas.')
print(f'B) O(s) mais pesado(s): {pesado[0]}')
print(f'C) O(s) mais leve(s): {leve[0]}')
"""

