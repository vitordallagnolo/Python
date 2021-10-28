"""
Crie um programa que leia o nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos
os dicionários em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.


pessoas = []
cadastro = {}
cadreal = 0
while True:
    cadreal += 1
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    cadastro['idade'] = int(input('Idade: '))
    resp = str(input('Deseja continuar? [S/N] ')).strip()
    pessoas.append(cadastro.copy())
    if resp in 'Nn':
        break
print(f'Lista: {pessoas}')
print(f'Dicionário: {cadastro}')
print(f'A) Foram cadastradas {cadreal} pessoas.')
print(f'B) A média da idade do grupo é {}')


"""
# Lista
galera = list()
# Dicionário
pessoa = dict()
soma = média = 0
while True:
    # Limpa o dicionário
    pessoa.clear()
    # Pergunta o nome e adiciona ao dicionário
    pessoa['nome'] = str(input('Nome: '))
    while True:
        # Pergunta o sexo e adiciona ao dicionário
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        # Se a resposta de sexo ser 'M ou F' = ok
        if pessoa['sexo'] in 'MF':
            break
        # Se a resposta de sexo não for 'M ou F' da erro
        print('ERRO! Por favor, utilize apenas M ou F.')
    # Pergunta a idade e adiciona ao dicionário
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade do grupo é de {soma / len(galera):.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= (soma / len(galera)):
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')