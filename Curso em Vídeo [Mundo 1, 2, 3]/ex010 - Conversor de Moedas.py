#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1.00 = R$3.27

w = float(input('Informe o valor em sua carteira: R$'))
cd = 3.27
n1 = (w / cd)
print('Com o valor de R${:.2f} que tem na carteira, você pode comprar US${:.2f}'.format(w, n1))