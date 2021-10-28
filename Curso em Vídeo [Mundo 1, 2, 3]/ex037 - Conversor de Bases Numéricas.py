'''
Escreva um programa que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 hexadecimal
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Para Binário
[ 2 ] Para Octal
[ 3 ] Para Hexadecimal ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('O número escolhido é inválido, tente novamente.')

#Concluído com sucesso!
