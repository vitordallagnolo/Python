'''
Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram no intervalo de 1 e 500
'''
s = 0
for count in range(1, 501):
    if count % 2 != 0: #Verifica os números ímpares (não divisíveis por 2).
        if count % 3 == 0: #Verifica se é múltiplo de 3 (resto da divisão por 3 é igual a 0).
            s += count
print('A soma dos números ímpares e divisíveis por 3 entre 1 e 500 é de {}'.format(s))

'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores é {}',format(cont, soma)
'''

#Concluído com Sucesso!

