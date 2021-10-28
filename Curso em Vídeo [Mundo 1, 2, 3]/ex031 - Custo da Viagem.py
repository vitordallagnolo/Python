'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem do onibus cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.
'''

d = int(input('Insira a distância da viagem que será feita: '))
t1 = 0.50 #taxa para viagens até 200Km
t2 = 0.45 #taxa para viagens maiores que 200Km
if d <= 200:
    print('Sua viagem será de {}Km e a passagem custará R${:.2f}'.format(d, d * t1))
else:
    print('Sua viagem será de {}Km e a passagem custará R${:.2f}'.format(d, d * t2))

'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45
'''

#Concluído com sucesso