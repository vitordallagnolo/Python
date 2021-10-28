#Faça um algoritmo que leia o preço de um produto e mostra seu novo preço, com 5% de desconto.
p = float(input('Insira o valor do produto: R$'))
dp = 0.05
pf = p - (p * dp)
pc = int(dp * 100)
print('O valor do produto é de R${:.2f}, com o desconto de {}% o valor final fica em R${:.2f}'. format(p, pc, pf))

#Concluído com sucesso
#10% de 100 = 100*10/100
