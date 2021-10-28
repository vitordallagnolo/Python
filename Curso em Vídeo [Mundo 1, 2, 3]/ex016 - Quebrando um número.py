#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#ex: digitar 6.123456 e mostrar 6

'''import math
n = float(input('Insira um número Real (ex: 1.234): '))
i = math.floor(n)
print('O número real {} que digitou, inteiro é {}'.format(n, i))
print('O número digitado foi {} e a sua porção inteira é {}'.format(n, math.trunc(n)))'''

#Concluído com sucesso

n = float(input('Digite um valor: '))
print('O valor digita foi de {} e sua porção inteira é {}'.format(n, int(n)))