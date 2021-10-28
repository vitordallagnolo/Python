#Escreva um programa que leia o valor em metros e mostra ele convertido em centímetros e milimetros.
m1 = float(input('Insira quantos metros quer converter: '))
c = float(m1 * 100)
m = float(c * 100)
print('Você optou por converter {} metros'.format(m1))
print('{} metros é o mesmo que {:.0f} centímetros e o mesmo que {:.0f} milímetros'.format(m1, c, m))