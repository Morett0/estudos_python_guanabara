# Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a sua porção inteira.
# Exemplo:  Digite um número: 6.127
#           O número 6.127 tem a parte inteira 6.

import math
n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {math.trunc(n)}')
