"""
Faça um mini-sistema que utilize o
Interactive Help do Python.
O usuário vai digitar o comando e o manual
vai aparecer.
Quando o usuário digitar a palavra 'FIM',
o programa se encerrará.

OBS: use cores.
"""
def menu():
    print('\033[31;40m=\033[m' * 30)
    print(f'\033[1;30;41m{"SISTEMA DE AJUDA PyHELP":^30}\033[m')
    print('\033[31;40m=\033[m' * 30)


def ajuda(com):
    help(com)


# Programa Principal
comando = ''
while True:
    menu()
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print('\033[7;30;41mATÉ LOGO!\033[m')



