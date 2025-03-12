# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira em Reais e mostre quantos Dólares ela pode comprar.

a = float(input('Quanto de dinheiro você tem na carteira R$:'))
print(f'Com R${a} você pode comprar US${(a/5.81):.2f}')
