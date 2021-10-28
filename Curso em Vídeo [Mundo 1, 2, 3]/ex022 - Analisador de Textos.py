'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

'''
name = str(input('Insira seu nome completo: '))
nameu = name.upper() #nome em maiúsculo
namel = name.lower() #nome em minúsculo
qtt = len(name) #quantos caractéres com espaço tem
qts = name.count(' ') #quantidade de espaços
qtw = qtt - qts #quantidade de letras ao todo sem considerar espaços
div = name.split() #divide a frase nos espaços
'''

'''nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras, sem contar espaços'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
#macete, colocar .strip no input, assim ele já divide o nome inserido'''

frase = str('BAIXADA ALGUMAS NOTAS DO DIA DE HOJE 03/09 POIS NÃO CONSEGUI MAIS COMPRADOR, POR A VENDA DE VOLTA NA QUINTA-FEIRA VISTO QUE SEG-TER-QUA A CRIS NÃO VAI TRABALHAR. VALOR TOTAL')
print('{}'.format(frase.lower()))