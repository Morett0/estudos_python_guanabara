# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

a = []
e = 0
for b in range(1, 8):
    c = int(input(f'Em que ano a {b}° pessoa nasceu? '))
    a.append(c)
for d in range(7):
    t = 2025 - a[d]
    if t < 19: 
        e += 1
print(f'Ao todo tivemos {e} pessoa(s) menor(es) de idade.')
print(f'E também tivemos {7-e} pessoa(s) maior(es) de idade.')