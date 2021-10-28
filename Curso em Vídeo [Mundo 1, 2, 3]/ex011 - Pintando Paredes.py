#Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule a sua área e a quantidade de tinta necessária para pintá-la
#Sabendo que cada litro de tinta pinta uma área de 2m²
alt = float(input('Informe a altura da parede: '))
lar = float(input('Informe a largura da parede:  '))
at = (alt * lar)
lm = 2
ttm = at / (lm)
print('Para pintar a área de {:.2f}m², você precisará de {:.2f} litros de tinta'.format(at, ttm))

#Concluído com sucesso!