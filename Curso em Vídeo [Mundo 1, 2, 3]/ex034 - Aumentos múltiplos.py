'''
Escreva um program,a que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
'''

s = float(input('Insira seu salário: R$'))
if s > 1250:
    print('Seu salário terá um aumento de 10%, passando de R${:.2f} para R${:.2f}'.format(s, s + (s * 0.10)))
else:
    print('Seu salário terá um aumento de 15%, passando de R${:.2f} para R${:.2f}'.format(s, s + (s * 0.15)))

'''s = float(input('Qual o seu salário? R$'))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)'''
#Concluído com Sucesso!