# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

t1 = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {type(t1)}')
print(f'Só tem espaço? {t1.isspace()}')
print(f'É um número? {t1.isnumeric()}')
print(f'É alfabético? {t1.isalpha()}')
print(f'É alfanumérico? {t1.isalnum()}')
print(f'Está em maiúscula? {t1.isupper()}')
print(f'Está em minúscula? {t1.islower()}')
print(f'Está capitalizada? {t1.istitle()}')
