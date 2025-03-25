# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser
# que quer mostrar 0 termos.

# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('='*80)
print('10 TERMOS DE UMA PA'.center(80))
print('='*80)

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
n3 = 0
n4 = n1
n5 =  10
n6 = 10

while n5 != 0:
    while n3 != n5:
        print(f'{n1}', end=' -> ')
        n1 += n2
        n3 += 1
    print('PAUSA')
    n3 = 0
    n5 = int(input('Quantos termos você quer mostrar mais? '))
    n6 += n5
print(f'Progressão finalizada com {n6} termos encontrados.')