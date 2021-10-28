'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Qual o valor da casa que deseja comprar? R$ '))
sal = float(input('Qual o seu salário? R$ '))
ano = int(input('Em quantos anos deseja pagar? ' ))
margem = float(sal * 30 / 100)
nparcelas = int(ano * 12)
mensal = float(casa / nparcelas)
if mensal >= margem:
    print('Seu empréstimo foi \033[1;31mNEGADO\033[m! A parcela comprometeria mais de 30% do seu salário.')
else:
    print('Seu empréstimo está \033[1;32mPRÉ-APROVADO\033[m! As parcelas não comprometem mais que 30% do seu salário.')

print('-=-'*10)
print('\033[1mDETALHAMENTO DA PROPOSTA\033[m')
print('-=-'*10)
print('O valor da casa é de R$ {:.2f}'.format(casa))
print('Seu salário é de R$ {:.2f}'.format(sal))
print('Você optou por parcelar em {} anos'.format(ano))
print('Você terá {} parcelas'.format(nparcelas))
print('O valor da parcela ficou em R$ {:.2f}'.format(mensal))
print('O valor da parcela não pode ultrapassar R$ {:.2f}'.format(margem))

#Concluído com Sucesso!!