# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
# até ter um valor correto.

x = str(input('Informe seu sexo: [M/F] ').upper().strip())

while x not in 'MmFf':
    x = str(input('Dado inválido. Por favor, informe o seu sexo: [M/F] ').upper().strip())

print(f'Sexo {x} registrado com sucesso.')
