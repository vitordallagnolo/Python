'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 Anos: SÊNIOR
-Acima de 20: MASTER
'''

from datetime import date
nasc = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
idade = int(atual - nasc)
if idade <= 9:
    print('Para {} anos a categoria é a MIRIM'.format(idade))
elif idade <= 14:
    print('Para {} anos a categoria é a INFANTIL'.format(idade))
elif idade <= 19:
    print('Para {} anos a categoria é a JUNIOR'.format(idade))
elif idade <= 25:
    print('Para {} anos a categoria é a SÊNIOR'.format(idade))
elif idade > 25:
    print('Para {} anos a categoria é a MASTER'.format(idade))

#Concluído com sucesso!

