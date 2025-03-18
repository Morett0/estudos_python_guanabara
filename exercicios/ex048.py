# Faça um programa que calculse a soma entre todo os números que são múltiplos de três e que seo encontram n intervalo de 1 até 500

b = 0
c = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        b += a
        c += 1
print(f'A soma de todos os {c} valores solicitados é {b}.')


        