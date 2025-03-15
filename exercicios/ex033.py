# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
d = [a, b, c]
d.sort()
print(f'O menor valor digitado foi: {d[0]}')
print(f'O maior valor digitado foi: {d[-1]}')
