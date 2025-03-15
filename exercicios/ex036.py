# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador 
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

a = float(input('Valor da casa: '))
b = float(input('Salário do comprador: '))
c = int(input('Quantos anos de financiamento: '))
print(f'Para pagar uma casa de R${a:.2f} em {c} anos a prestação será de R${a / (c*12):.2f}')
if a / (c*12) <= b*30/100:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
