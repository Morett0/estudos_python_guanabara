# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o
# nome do homem mais velho e quantas mulheres têm menos de 20 anos.

n = []
i = []
s = []

idade_maior = 0
nome_homem_velho = ''
mulher_menos20 = 0
soma_idade = 0

for a in range(1, 5):
    print(f'-'*20, f'{a}ª PESSOA', f'-'*20)

    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())

    soma_idade += idade

    n.append(nome)
    i.append(idade)
    s.append(sexo)

    if sexo == 'M' and idade > idade_maior:
        idade_maior = idade
        nome_homem_velho = nome

    if sexo == 'F' and idade < 20:
        mulher_menos20 += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {soma_idade / 4}')
if nome_homem_velho:
    print(f'O homem mais velho o homem mais velho tem {idade_maior} anos e se chama {nome_homem_velho}.')
else:
    print('Não tem homem no grupo.')
if mulher_menos20:
    print(f'Ao todo, há {mulher_menos20} mulher(es) no grupo com menos de 20 anos.')
else:
    print('Não tem mulher no grupo.')
