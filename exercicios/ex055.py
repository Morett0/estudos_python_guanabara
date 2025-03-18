# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

c = []
for b in range(1, 6):
    a = float(input(f'Peso da {b}° pessoa: '))
    c.append(a)
print(f'A pessoa mais pesada pesa {max(c)}kg\n'
      f'E a mais leve é {min(c)}kg')
