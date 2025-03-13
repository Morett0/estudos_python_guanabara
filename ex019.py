# Um professor quer sortear um dos seu quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles 
# e escrevendo o nome escolhido.

import random
a = str(input('Nome do primeiro aluno: '))
b = str(input('Nome do segundo aluno: '))
c = str(input('Nome do terceiro aluno: '))
d = str(input('Nome do quarto aluno: '))
e = [a, b, c, d]
print(f'O aluno escolhido foi {random.choice(e)}')
