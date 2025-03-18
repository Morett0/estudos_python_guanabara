# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
# até acertar, mostrando no final quantos palpites foram necessários para vencer

import random

a = int(input('Sou seu computador...\n'
      'Acabei de pensar em um número enre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?\n'
      'Qual o seu palpite? '))
b = random.randint(0, 10)
c = 1

while a != b:
    if a < b:
        a = int(input('Mais... Tente mais uma vez!\n'
                      'Qual o seu palpite? '))
    elif a > b:
        a = int(input('Menos... Tente mais uma vez!\n'
                      'Qual o seu palpite? '))
    else:
        break
    c += 1
print(f'ACERTOU! Em {c} tentativa(s).')
