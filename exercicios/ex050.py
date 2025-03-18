# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

a = []
for b in range(6):
    b = int(input(f'Digite o {b+1}° número: '))
    if b % 2 == 0:
        a.append(b)
c = sum(a)
print(f'A soma de todos os números impares é de {c}')


