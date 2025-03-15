# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

a = float(input('Digite o salário do funcionário: '))
if a > 1250:
    print(f'Quem ganhava R${a:.2f}, passa a ganhar R${(a*110)/100:.2f}')
else:
    print(f'Quem ganhava R${a:.2f}, passa a ganhar R${(a*115)/100:.2f}')
