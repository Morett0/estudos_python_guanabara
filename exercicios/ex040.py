#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
c = (a+b)/2
print(f'Tirando {a:.1f} e {b:.1f}, a média do aluno é {c:.1f}')
if c < 5:
    print('O aluno está REPROVADO!')
elif c >= 5 and c <= 6.9:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')
