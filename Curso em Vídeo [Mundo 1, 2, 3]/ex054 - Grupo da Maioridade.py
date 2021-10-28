"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
Maioridade >= 21
"""
from datetime import date
maior = 0
menor = 0
pessoas = 0
atual = date.today().year
for contador in range (1,8):
    ano = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(contador)))
    pessoas += 1
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Das {} pessoas, {} estão na maioridade e {} não estão.'.format(pessoas, maior, menor))

#Concluído com Sucesso!