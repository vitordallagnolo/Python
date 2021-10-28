'''
Faça um programa que leia o número inteiro e diga se ele é ou não um número primo.
Número primo: Somente divisível por 1 e ele mesmo
'''
print('==== MEU PROGRAMA ====')
n = int(input('Informe um número inteiro: '))
d = 1
if n / 1 == n and n / n == 1:
    for p in range(0, 100):
        d += 1
        f = n / d
    if f != 1 or f != n:
        print('Não é um número primo')
    else:
         print('É um número primo')
#minha lógica ficou meio complexa.

print('==== PROGRAMA PROFESSOR ====')

núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(núm, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

#Concluído com Sucesso!