# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

d = int(input('Quandos dias alugados: '))
k = int(input('Quantos Km rodados: '))
print(f'O total a pagar é de R${(d*60)+(k*0.15):.2f}')
