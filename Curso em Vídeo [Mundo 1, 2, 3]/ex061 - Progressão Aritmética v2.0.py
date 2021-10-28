"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print('#Meu Programa')
t = int(input('Insira o TERMO da Progressão Aritmética: '))
r = int(input('Insira a RAZÃO da Progressão Aritmética: '))
c = 10
print('Os 10 primeiros termos a partir de {} são:'.format(t))
while c > 0:
    c = c - 1
    t += r
    print('{} '.format(t), end='')

print('#Programa Professor')
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')

#Concluído com Sucesso!