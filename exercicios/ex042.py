# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('-' * 20)
print('Analisador de Triângulos')
print('-' * 20)
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a + b > c and b + c > a and c + a > b:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a == b or b == c or c == a:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
