'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

v = int(input('Insira sua velocidade: '))
if v > 80:
    print('Você ultrapassou 80Km/h e foi multado, o valor da multa será de R${:.2f}, que se refere aos {}Km/h que passou do limite.'.format((v-80)*7, v - 80))
else:
    print('Você está dentro do limite de velocidade. Siga bem caminhoneiro!')

#Concluído com Sucesso!