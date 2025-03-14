# Faça um programa que leia a fresa pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a ultima vez.

a = str(input('Digite uma frase: ')).lower()
print(f"A letra 'A' aparece {a.count("a")} vezes")
print(f'A primeira letra "A" aparece na posição {a.find("a")}')
print(f'A última letra "A" aparece na posição {a.rfind("a")}')
