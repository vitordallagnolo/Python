#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#A quantidade de dias pelos quais ele foi alugado
#Calcule o preço a pagar
#Sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram percorridos? '))
d = int(input('Por quantos dias este carro ficou locado? '))
cd = 60
kmr = 0.15
print('Você percorreu {}Km, e ficou com o veículo por {} dias, sendo assim, o valor devido é de R${:.2f}.'.format(km, d, (cd * d) + (kmr * km)))

#Concluído com sucesso!