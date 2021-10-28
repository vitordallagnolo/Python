"""
Crie um programa onde o usuário posas digitar vários valores númericos
e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final serão exibidos todos os números em ordem crescente.
"""
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    if r in 'N':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')

"""    
    c += 1
    listanum.append(int(input('Insira um valor: ')))
    print(listanum)
    if listanum[c] in (listanum):
        print('Valor duplicado, não registrado!')
    else:
        print('Valor registrado!')
    seguir = str(input('Deseja continuar? [S/N]')).strip().upper()
    if seguir[0] in 'N':
        break
print(listanum)
"""