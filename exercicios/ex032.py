# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# %%

from datetime import datetime

a = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if a == 0:
    a = datetime.now().year
    if a % 100 == 0:
        print(f'O ano de {a} NÃO é BISSEXTO!')
    elif a % 400 == 0:
        print(f'O ano de {a} é BISSEXTO!')
    elif a % 4 == 0:
        print(f'O ano de {a} é BISSEXTO!')
    else:
        print(f'O ano de {a} NÃO é BISSEXTO!')
else:
    if a % 100 == 0:
        print(f'O ano de {a} NÃO é BISSEXTO!')
    elif a % 400 == 0:
        print(f'O ano de {a} é BISSEXTO!')
    elif a % 4 == 0:
        print(f'O ano de {a} é BISSEXTO!')
    else:
        print(f'O ano de {a} NÃO é BISSEXTO!')

# %%

from datetime import datetime

a = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
    a == datetime.now().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
     print(f'O ano de {a} é BISSEXTO!')
else:
    print(f'O ano de {a} NÃO é BISSEXTO!')