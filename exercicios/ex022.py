# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

n = str(input('Qual o seu nome completo: '))
print(f'Seu nome com todas as letra maiúculas fica assim: {n.upper()}')
print(f'Seu nome com todas as letra minúsculas fica assim: {n.lower()}')
print(f'Seu nome tem {len(n.replace(" ", ""))} letras')
print(f'O seu primeiro nome é {n.split(" ")[0]} e tem {len(n.split(" ")[0])} letras')
