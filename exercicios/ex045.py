# Crie um programa que faça o computador jogar Jokenpô com você.

import time
import random

print(f'{"JOKEMPÔ":=^40}')
a = int(input('Suas opções:\n'
              '[ 0 ] PEDRA\n'
              '[ 1 ] PAPEL\n'
              '[ 2 ] TESOURA\n'
              'Qual é sua jogada? '))
if a not in [0, 1, 2]:
    print('Escolha invalida! Tente novamente.')
else:
    print('\nJO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PÔ!!!')
    b = random.randint(0, 2)
    c = ['PEDRA', 'PAPEL', 'TESOURA']
    print('-==-'*10)
    print(f'Você jogou {c[a]}')
    print(f'Computador jogou {c[b]}')
    print('-==-'*10)
    if a == 0 and b == 2 or a == 1 and b == 0 or a == 2 and b == 1:
        print('JOGADOR VENCE!')
    elif a == b:
        print('EMPATE!')
    else:
        print('COMPUTADOR VENCE!')
    