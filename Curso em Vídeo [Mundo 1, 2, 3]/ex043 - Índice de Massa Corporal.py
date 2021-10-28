'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida
'''

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura) #ou altura² que é altura ** 2
if imc < 18.5:
    print('Seu IMC é de {:.1f}, você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.1f}, você está no peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é de {:.1f}, você está com sobrepeso.'.format(imc))
elif imc < 40:
    print('Seu IMC é de {:.1f}, você está em obesidade.')
else:
    print('Seu IMC é de {:.1f}, você está em obesidade mórbida, cuide mais de sua saúde!'.format(imc))
#print('Seu peso é de {:.1f} e sua altura {:.2f}.'.format(peso, altura))
#print('Seu IMC é {:.1f}'.format(imc))

#Concluído com Sucesso!
