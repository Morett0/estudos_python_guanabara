# Um professor quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
n = [n1, n2, n3, n4]
random.shuffle(n)
print(f'A ordem será: {n}')
