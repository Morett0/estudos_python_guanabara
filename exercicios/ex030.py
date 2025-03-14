# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

a = int(input('Digite um número: '))
if a % 2 == 0:
    print(f'O número {a} é PAR')
else:
    print(f'O número {a} é IMPAR')
