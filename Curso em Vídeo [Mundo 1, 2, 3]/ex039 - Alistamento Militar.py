#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com sua idade:

#-Se ele ainda vai se alistar ao serviço militar.
#-Se é a hora de se alistar
#-Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = atual - ano
print('Sua idade é {}'.format(idade))
if idade < 18:
    print('Ainda faltam {} anos para seu alistamento.'.format(18 - idade))
elif idade == 18:
    print('Você precisa se alistar imediatamente!')
else:
    print('Você perdeu o prazo para alistamento, procure a Junta Militar!')

#Concluído com Sucesso!