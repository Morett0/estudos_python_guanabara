# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao
# serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o
# tempo que falta ou que passou do prazo.

from datetime import datetime

a = int(input('Ano de nascimento: '))
b = datetime.now().year
if b - a < 18:
    print(f'Quem nasceu em {a} tem {b-a} em {b}.\n'
          f'Ainda faltam {(a+18)-b} anos para o alstamento.\n'
          f'Seu alistamento será em {a+18}.')
elif b - a > 18:
    print(f'Quem nasceu em {a} tem {b-a} em {b}.\n'
          f'Você já deveria ter se alistado há {b-(a+18)} anos.\n'
          f'Seu alistamento foi em {a+18}.')
else:
    print(f'Quem nasceu em {a} tem {b-a} em {b}.\n'
          f'Você deve se alistar IMEDIATAMENTE!')
    