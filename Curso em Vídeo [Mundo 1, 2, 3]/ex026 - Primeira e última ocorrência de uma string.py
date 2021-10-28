'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''

frase = str(input('Escreva uma frase: ')).upper().strip() #Organizando a frase
print('Vemos a letra "A" em {} vezes'.format(frase.count('A'))) #Encontrando a primeira letra A
print('A Primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #Contanto a posição
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #Encontrando a última letra A