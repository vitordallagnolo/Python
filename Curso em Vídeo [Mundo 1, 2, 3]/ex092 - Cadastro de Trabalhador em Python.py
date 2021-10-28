"""
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário se por acaso a CTPS
for diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
trabalhador = {}
# Perguntar o nome
trabalhador['name'] = str(input('Nome: '))
# Perguntar o ano de nascimento
ano = int(input('Ano de nascimento: '))
# Calcular idade
trabalhador['idade'] = date.today().year - ano
# Perguntar a carteira de trabalho(se não tiver é 0)
trabalhador['ctps'] = int(input('Nº da Carteira de Trabalho: (0 se não tiver) '))
# Se tiver carteira
if trabalhador['ctps'] != 0:
    # Perguntar Ano de Contratação
    trabalhador['contr'] = int(input('Ano de contratação: '))
    # Perguntar o Salário
    trabalhador['sal'] = float(input('Salário: R$'))
    # Calcular com quantos anos se aposentará
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contr'] + 35) - date.today().year)

print('-=' * 15)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')