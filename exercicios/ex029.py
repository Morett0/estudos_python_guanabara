#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

a = float(input('Qual a velocidade atual do carro? '))
if a <= 80:
    print('\033[32mTenha um bom dia! Dirija com segurança.\033[0m')
else:
    print(f'\033[31mMULTADO! Você excedeu o limite de velocidade que é de 80Km/h\n\033[33mVocê deve pagar uma multa de R${(a-80)*7:.2f}\033[0m')