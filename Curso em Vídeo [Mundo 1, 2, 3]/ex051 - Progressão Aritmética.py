'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
'''
print('#Meu Programa')

t = int(input('Insira o TERMO da Progressão Aritmética: '))
r = int(input('Insira a RAZÃO da Progressão Aritmética: '))
for pa in range(0,10):
    t += r
    print(t, end=' →')
print('ACABOU')

print('#Professor')#Professor
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='→ ')
print('Acabou')

#Concluído com Sucesso!