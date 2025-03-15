# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-==-'*20)
print('Analisador de Triângulos')
print('-==-'*20)
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a + b > c and b + c > a and c + a > b:
    print('O segmento acima PODE formar um triãngulo')
else:
    print('O segmento acima NÂO PODE formar um triãngulo')
