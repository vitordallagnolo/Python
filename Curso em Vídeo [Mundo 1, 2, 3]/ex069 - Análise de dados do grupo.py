"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada o programa deverá perguntar se o usuário quer continuar ou não.
No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
print('#Meu Programa')
a = 0
b = 0
c = 0
while True:
    i = int(input('Informe a idade: '))
    s = str(input('Informe o sexo: [M/F]')).strip()
    if s not in 'MmFf':
        print('Opção inválida!')
    elif s in 'MmFf':
        if s in 'Mm':
            b += 1
            if i >= 18:
                a += 1
        elif s in 'Ff':
            if i > 18:
                a += 1
            elif i < 20:
                c += 1
        next = str(input('Deseja continuar? [S/N] '))
        if next in 'Nn':
            break
print(f'{a} pessoa(s) tem mais de 18 anos.')
print(f'{b} homens cadastrados.')
print(f'{c} mulheres tem menos de 20 anos.')

#Concluído com Sucesso!


print('#Programa Professor')
tot18 = totH = 0
while True:
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        tot18 +=1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menso de 20 anos')