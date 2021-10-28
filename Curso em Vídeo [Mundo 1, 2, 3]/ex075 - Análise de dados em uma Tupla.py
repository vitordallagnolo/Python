"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A)Quantas vezes apareceou o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C)Quais foram os números pares.
"""
print('#Meu Programa')
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))
d = int(input('Insira o quarto e último número: '))
valores = (a, b, c, d)
print(valores)
print(f'O número 9 aparece {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro número 3 foi digitado no {valores.index(3) + 1}º número.')
else:
    print('O valor 3 não foi digitado.')
print(f'São pares:', end=' ')
for pares in valores:
    if pares % 2 == 0:
        print(pares, end=' ')

print('-=' * 10)
print('#Programa Professor')
núm = (int(input('digite o primeiro número: ')),
       int(input('digite o segundo número: ')),
       int(input('digite o terceiro número: ')),
       int(input('digite o quarto número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
