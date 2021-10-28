"""
Desenvolva um programa que leia nome e idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.
"""
#Meu Programa
idades = 0
hmv = ''
ihmv = 0
m20 = 0
for c in range(1,5):
    print('---- {}ª pessoa ----'.format(c))
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Masculino [M] ou Feminino [F]?')).upper()
    print('=' * 22)
    idades += idade
    if sexo == 'M' and ihmv == 0:
        hmv = nome
        ihmv = idade
    elif sexo == 'M' and hmv != '' and idade > ihmv:
        ihmv = idade
        hmv = nome
        if sexo == 'M':
            hmv = nome
            ihmv = idade
    elif sexo == 'F' and idade < 20:
        m20 += 1

print('A idade média deste grupo é de {} anos'.format(idades / c))
print('{} é o homem mais velho, tem {} anos'.format(hmv, ihmv))
print('São {} mulheres que tem menos de 20 anos'.format(m20))

#Professor

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1,5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade >maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.fomrat(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))