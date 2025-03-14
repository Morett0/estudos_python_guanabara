# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Exemplo:
#	Digite um número: 1834
#	Unidade: 4
#	Dezena: 3
#	Centena: 8
#	Milhar: 1

n = int(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {n % 10}')
print(f'Dezena: {n // 10 % 10}')
print(f'Centena: {n // 100 % 10}')
print(f'Milhar: {n // 1000 % 10}')
