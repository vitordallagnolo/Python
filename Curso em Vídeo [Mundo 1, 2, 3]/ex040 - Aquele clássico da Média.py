'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
m = float((n1 + n2) / 2 )
if m < 5.0:
    print('Sua média foi {:.1f}, você está \033[1;31mREPROVADO\033[m!'.format(m))
    print('Estude mais!')
elif m < 7:
    print('Sua média foi de {:.1f}, você está em \033[1;33mRECUPERAÇÃO\033[m!'.format(m))
elif m >= 7:
    print('Sua média foi de {:.1f}. Você foi \033[1;32mAPROVADO\033[m! Parabéns!'.format(m))

#Concluído com Sucesso!
#Colocando as notas 6.9 e 7, ele mostra média 7 e diz que ficou em recuperação, pois arredondou 6.995 para 7