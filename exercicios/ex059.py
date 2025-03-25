# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

c = 0
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

while c != 5:
    c = int(input('[ 1 ] Somar\n'
                '[ 2 ] Multiplicar\n'
                '[ 3 ] Maior\n'
                '[ 4 ] Novos números\n'
                '[ 5 ] Sair do programa\n'
                '>>>>>>> Qual é a sua opção: '))
    if c == 1:
        print(f'A soma entre {a} + {b} é {a+b}')
    elif c == 2:
        print(f'A multiplicação entre {a} * {b} é {a*b}')
    elif c == 3:
        if a > b:
            print(f'Entre {a} e {b} o maior é {a}')
        elif b > a:
            print(f'Entre {a} e {b} o maior é {b}')
        else:
            print('Os valores são iguaia')
    
    elif c == 4:
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
    else:
        print('Adeus!!')