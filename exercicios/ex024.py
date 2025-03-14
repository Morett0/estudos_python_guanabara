# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

a = str(input('Em que cidade você nasceu: '))
print(a.upper().split()[0] == "SANTO")
