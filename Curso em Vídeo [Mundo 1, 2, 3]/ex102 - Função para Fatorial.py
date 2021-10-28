"""
Crie um programa que tenha a função fatorial()
que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial

se usar o help, ensina a usar
ex: show true printa todo o cálculo
"""


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '' )
            else:
                print(' = ', end = '')
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=False))
help(fatorial)
