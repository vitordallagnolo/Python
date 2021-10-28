def aumentar(num=0, taxa=0, formato=False):
    res = num + (num * taxa / 100)
    return res if formato is False else moeda(num)

def diminuir(num=0, taxa=0, formato=False):
    res = num - (num * taxa / 100)
    return res if formato is False else moeda(num)

def dobro(num=0, formato=False):
    res = num * 2
    return res if not formato else moeda(res)


def metade(num=0, formato=False):
    res = num / 2
    return res if not formato else (moeda(res))


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')


