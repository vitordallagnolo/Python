"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
#Meu programa
s = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while s not in 'FM':
    print('Incorreto, você utilizou "{}", utilize apenas M ou F'.format(s))
    s = str(input('Informe seu sexo: [M/F] ')).upper().strip()
print('Finalizado')
#Concluído com Sucesso!

"""
#Professor
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, inform seu sexo: [m/f]'))
print('Sexo {} registrado com sucesso.'.format(sexo))
"""