"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimetno de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

18 é obrigatório
16 Opcional
65+ Opicional
EX: Ano 2000 retorna "com x anos: O voto é TANANAN
"""
#Meu Programa
"""
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        resp = str('NEGADO')
    elif idade > 16 or idade < 18 or idade >= 65:
        resp = str('OPCIONAL')
    elif idade >= 18 < 65:
        resp = str('OBRIGATÓRIO')
    print(f'Cidadão com {idade} anos o voto é: {resp}')
nasc = int(input('Ano de Nascimento: '))
voto(nasc)
"""

#Programa Professor
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO. '

#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

