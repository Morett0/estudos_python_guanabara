# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*80)
print('10 TERMOS DE UMA PA'.center(80))
print('='*80)

a = int(input('Primeiro termo: '))
b = int(input('Razão: '))

for c in range(10):
 print(a + (b * c), end=' -> ')
print('ACABOU')