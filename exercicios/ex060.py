# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

# Primeira versão, funcional, mas não está otimizado.

import math

n1 = int(input('Digite um número para calcular seu fatorial: '))
a = 0
b = []
c = n1-1

while a != n1:
    a+=1
    b.append(a)
print(b)
print(f'{n1}! = {b[c]}', end=' ')

while c != 0:
    c-=1
    print(f'x {b[c]}', end=' ')
print(f'= {math.factorial(n1)}')
    
'''
# Segunda versão, otimizada, com o menos código possivel

import math

n1 = int(input('Digite um número para calcular seu fatorial: '))
print(f'{n1}! = {n1}', end=' ')

for i in range(n1 - 1, 0, -1):
    print(f'x {i}', end=' ')

print(f'= {math.factorial(n1)}')

