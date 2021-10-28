"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""
print('#Meu Programa')
print('Para encerrar, digite 999')
print('=========================')
n = int(input('Insira um valor: '))
count = 0
total = n
if total != 999:
    total = n
    while n != 999:
        count += 1
        n = int(input('Insira um valor: '))
        if n != 999:
            total += n
    print('Você digitou {} números, a soma deles foi {}.'.format(count, total))
else:
    print('Você desistiu do programa.'.format(count, total))
print('PROGRAMA FINALIZADO')

#Finalizado com Sucesso!

print('Programa Professor')
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))