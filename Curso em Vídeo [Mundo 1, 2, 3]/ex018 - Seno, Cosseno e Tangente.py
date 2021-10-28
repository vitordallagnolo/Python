#Faça um programa que leia um ângulo qualquer
#E mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

an = float(input('Informe o angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
a = math.radians(an)
print('O angulo que informou é {}º, o qual seu seno é {:.2f}, cosseno {:.2f} e sua tangente {:.2f}'.format(an, sen, cos, tan))

#Concluído com sucesso