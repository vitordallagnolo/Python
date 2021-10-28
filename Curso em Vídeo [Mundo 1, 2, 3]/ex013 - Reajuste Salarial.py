#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Informe seu salário: R$'))
percentual = float(input('Insira o percentual para aumentar: '))
aumento = salário + (salário * (percentual/100))

print('Com um aumento de R${:.2f}, seu novo salário é R${:.2f}'.format(aumento - salário,aumento))

#Concluído com sucesso