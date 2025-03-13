# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
a = float(input('Digite o ãngulo que você deseja: '))
print(f'O ãngulo de {a} tem o SENO de {math.sin(math.radians(a)):.2f}')
print(f'O ãngulo de {a} tem o COSSENO de {math.cos(math.radians(a)):.2f}')
print(f'O ãngulo de {a} tem a TANGENTE de {math.tan(math.radians(a)):.2f}')

