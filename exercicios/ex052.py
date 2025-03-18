# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

c = 0
a = int(input('Digite um número: '))
for b in range(1, (a+1)):
    if a % b == 0:
        print(f'\033[31m{b}\033[0m', end=" ")
        c += 1
    else:
        print(f'\033[34m{b}\033[0m', end=" " )
if c == 2:
    print(f'\nO número {a} foi divisível {c} vezes.\n'
          'E por isso ele É PRIMO!')
else:
    print(f'\nO número {a} foi divisível {c} vezes.\n'
          'E por isso ele NÃO É PRIMO!')