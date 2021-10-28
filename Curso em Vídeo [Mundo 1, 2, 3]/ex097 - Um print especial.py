"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer com o parâmetro e mostre uma mensagem com o tamanho adaptável.
"""
def  escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


escreva(str(input('Insira a frase: ')))