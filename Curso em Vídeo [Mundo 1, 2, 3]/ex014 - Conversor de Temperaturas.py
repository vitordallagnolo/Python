#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Insira a temperatura de ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de ºC {:.1f} em ºF é {:.1f}'.format(c, f))
