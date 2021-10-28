"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.

Após aula pediu para colocar a opção "Continuar"
"""
print('#Meu Programa')
números = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito',
           'Dezenove','Vinte')
continuar = 'ss'
while continuar not in 'Nn':
    n = int(input('Informe um número de entre 0 e 20: '))
    while n > 20 or n < 0:
            n = int(input('Valor inválido. Informe um número de entre 0 e 20: '))
    print(f'Você digitou \033[1;31m{números[n]}\033[m.')
    continuar = str(input('Deseja Continuar? [S/N]')).strip()[0]
print('Acabou')

"""
print('#Programa Professor')
cont = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito',
           'Dezenove','Vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {cont[núm]}')
#Concluído com Sucesso!
"""