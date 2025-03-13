# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do produto? R$'))
print(f'O produto que custava R${p}, na promoção com desconto de 5% vai custar R${(p*95)/100:.2f}')
