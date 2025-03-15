# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import datetime

a = datetime.now().year
b = int(input('Ano de Nascimento: '))
print(f'O atleta tem {a-b} anos.')
if b <= 9:
    print('Calissificação: MIRIM')
elif b > 9 and b <= 14:
    print('Classificação: INFANTIL')
elif b > 14 and b <= 19:
    print('Classificação: JUNIOR')
elif b > 19 and b <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
