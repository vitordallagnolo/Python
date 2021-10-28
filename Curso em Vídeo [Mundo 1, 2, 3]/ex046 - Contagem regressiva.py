'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artifício, indo de 10 até 0, com uma pause de 1 segundo entre eles.
'''
print('-=-' * 10)
print('CONTAGEM REGRESSIVA')
print('-=-' * 10)
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('\033[0;31;40mPO PO POPOW!!!\033[m')
print('\033[0;31;40mFELIZ ANO NOVO!!!\033[m')

#Concluído com Sucesso!