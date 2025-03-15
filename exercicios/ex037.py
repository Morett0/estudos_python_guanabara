# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

a = int(input('Digite um número inteiro: '))
b = int(input('Escolha uma das bases para conversão:\n'
'[ 1 ] Converter para BINÁRIO\n'
'[ 2 ] Converter para OCTAL\n'
'[ 3 ] Converter para HEXADECIMAL\n'
'Sua opção: '))
if b == 1:
    print(f'{a} convertido para BINÁRIO é igual a {bin(a)[2:]}')
elif b == 2:
    print(f'{a} convertido para OCTAL é igual a {oct(a)[2:]}')
elif b == 3:
    print(f'{a} convertido para HEXADECIMAL é igual a {hex(a)[2:]}')
else:
    print('Opção Inválida.')