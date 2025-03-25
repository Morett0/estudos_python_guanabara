# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('='*80)
print('10 TERMOS DE UMA PA'.center(80))
print('='*80)

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
n3 = 0
n4 = n1

while n3 != 10:
    print(f'{n1}', end=' -> ')
    n1 += n2
    n3 += 1
print('FIM')