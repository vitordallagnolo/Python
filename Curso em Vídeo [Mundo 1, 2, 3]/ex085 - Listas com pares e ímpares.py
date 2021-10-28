"""
Fazer uma lista com lsitas internas.
Crie um programa onde o usuário pode digitar 7 valores númericos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""

núm = [[], []]
valor = 0
for c in range (1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 ==0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {núm[0]}.')
print(f'Os valores ímpares digitados foram: {núm[1]}.')