"""
Faça um programa que leia o nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
< 7 reprovado
>= 7 aprovado
"""
alunos = {}
alunos['name'] = str(input('Nome do Aluno: '))
alunos['avg'] = float(input(f'Média do {alunos["name"]}: '))
if alunos['avg'] < 5:
    alunos['situation'] = 'REPROVADO'
elif 5 <= alunos['avg'] < 7:
    alunos['situation'] = 'RECUPERAÇÃO'
else:
    alunos['situation'] = 'APROVADO'
print('-=' * 15)
print(alunos)
print(f'O aluno {alunos["name"]} teve a média {alunos["avg"]}')
print(f'{alunos["name"]} está {alunos["situation"]}!')

for k, v in alunos.items():
    print(f'{k} é igual a {v}')