# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
x = input('Digite Algo: ')
print('o tipo de x é:', type(x))
print('É número?', x.isnumeric())
print('É alfabeto?', x.isalpha())
print('É decimal?', x.isdecimal())
print('É título?', x.istitle())
print('É ascii?', x.isascii())
print('Está em maiúsculo?', x.isupper())