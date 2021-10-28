'''
Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com "SANTO"
'''

city = str(input('Em qual cidade você nasceu?')).strip()
print(city[:5].upper() == 'SANTO')