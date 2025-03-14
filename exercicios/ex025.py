# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

a = str(input('Digite seu nome completo: ')).upper().split()
print("SILVA" in a)