# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print(f'{"Lojas Nicolas":=^40}')
p = float(input('Preço da compra: R$'))
f = int(input('FORMA DE PAGAMENTO\n'
              '[ 1 ] à vista dinheiro/cheque.\n'
              '[ 2 ] à vista cartão\n'
              '[ 3 ] 2x no cartão\n'
              '[ 4 ] 3x ou mais no cartão\n'
              'Qual a opção: '))
if f == 1:
    print(f'Sua compra de R${p:.2f} vai custar R${(p*90)/100:.2f} no final.')
elif f == 2:
    print(f'Sua compra de R${p:.2f} vai custar R${(p*95)/100:.2f} no final.')
elif f == 3:
    print(f'Sua compra de R${p:.2f} vai custar o preço normal de R${p:.2f} no final.')
elif f == 4:
    d = int(input('Quantas parcelas: '))
    if d >= 3:
        print(f'Sua compra será parcelada em {d}x de R${((p*120)/100)/d:.2f} COM JUROS.\n'
              f'Sua compra de R${p:.2f} vai custar R${(p*120)/100:.2f} no final.')
    else:
        print('Número de parcelas invalida para esse tipo de compra.')
else:
    print('Opção invalida.')
