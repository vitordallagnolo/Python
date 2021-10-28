"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma descresente.
C) Se o valor 5 foi digitado e está ou não na lista.

"""

lista = []
print('Digite 0000 para encerrar')
while True:
    n = int(input('Insira um número: '))
    if n != 0000:
        lista.append(n)
        print('Registrado.')
    else:
        break
print(f'A) Foram digitados {len(lista)} números.') #ou {len(lista)}
lista.sort(reverse=True)
print(f'B) Lista ordenada decresente: {lista}')
if 5 in lista:
    print(f'C) O número 5 está na lista.')
else:
    print(f'C) O número 5 não foi digitado.')