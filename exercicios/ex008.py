# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

n1 = float(input('Digite o valor em metros: '))
print(f'{n1:.2f} metros convertido em centímetros é {(n1*100):.2f}')
print(f'{n1:.2f} metros convertido em milímetros é {(n1*1000):.2f}')
