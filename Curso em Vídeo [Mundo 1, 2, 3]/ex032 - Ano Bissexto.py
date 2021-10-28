'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto
'''
from datetime import date
ano = int(input('Ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano de {} é Bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
print('Data de hoje: {}'.format(date.today()))


#Concluído com sucesso