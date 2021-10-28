#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Insira um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('Seu número é o {}, onde seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n1, d, t, r))