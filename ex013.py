# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

s = float(input('Qual é o salário do funcionário? R$'))
print(f'Um funcionário que ganhava R${s}, com 15% de aumento, passa a receber R${(s*115)/100:.2f}')
