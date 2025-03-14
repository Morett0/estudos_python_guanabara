# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário vencer ou perdeu.

import random
print('\033[33m-=-\033[0m' * 20)
print('Vou pensar em número de 0 a 5. Tente Adivinhar...')
print('\033[33m-=-\033[0m' * 20)
a = int(input('Em que número eu pensei? '))
b = random.randint(0, 5)
if b == a:
    print('\033[32mParabens! Você ganhou.\033[0m')
else:
    print('\033[31mVocê perdeu.\033[0m')