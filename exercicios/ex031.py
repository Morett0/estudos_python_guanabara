# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
# de até 200Km e R$0,45 parta viagens mais longas.

k = int(input('Distância da sua viagem: '))
if k <= 200:
    print(f'Você está prestes a começar uma viagem de {k}Km.')
    print(f'E o preço da sua paragem será de R${k*0.50:.2f}')
else:
    print(f'Você está prestes a começar uma viagem de {k}Km.')
    print(f'E o preço da sua paragem será de R${k*0.45:.2f}')

