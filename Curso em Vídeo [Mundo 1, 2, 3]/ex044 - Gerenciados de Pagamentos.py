'''
Elabore um programa que calcule um valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' LOJAS BIRIBINHA '))
p = float(input('Preços das Compras: R$ '))
print('''Escolha a forma de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
 ''')
forma = int(input('Sua opção: '))
if forma == 1:
    print('O valor de R$ {:.2f} pago à vista em dinheiro ou cartão terá desconto de 10%'.format(p))
    print('O valor a ser pago é de R$ {:.2f}'.format(p - ((p * 10) / 100 )))
elif forma == 2:
    print('O valor de R$ {:.2f} pago à vista no cartão terá 5% de desconto'.format(p))
    print('O valor a ser pago é de {:.2f}'.format(p - ((p * 5) / 100)))
elif forma == 3:
    print('O valor de R$ {:.2f} pago em até 2x no cartão não possuí desconto'.format(p))
    print('O valor para pagamento é de R$ {:.2f}'.format(p))
elif forma == 4:
    print('O valor de R$ {:.2f} pago em 3x ou mais no cartão terá juros de 20.'.format(p))
    print('O valor a ser pago é de R$ {:.2f}'.format(p + ((p * 20) / 100)))
else:
    print('OPÇÃO INVÁLIDA.')

#OU

#Concluído com Sucesso!
