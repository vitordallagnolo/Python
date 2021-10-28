# Ordem de Precedência
# 1 ()
# 2 **
# 3 * / // %
# 4 + -

# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Insira um número: '))
ant = n1 - 1
suc = n1 + 1
print('Seu número é o {}, onde seu antecessor é o {} e seu sucessor é o {}'.format(n1, ant, suc))

#Pode removar as varíaveis e colocar direto na máscara do .format como .format(n1, (n-1), (n+1))

#Concluído com sucesso!