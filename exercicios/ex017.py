# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e 
# mostre o comprimento da hipotenusa.

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa é {math.hypot(co, ca)}')

