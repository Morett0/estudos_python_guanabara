# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.


a = str(input('Digite uma frase: '))
b = a.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").upper()
c = b[::-1]
if b == c:
    print(f'O Inverso de {b} é {c}!\n'
          'A frase digitada É um palíndromo!')
else:
    print(f'O Inverso de {b} é {c}!\n'
          'A frase digitada NÃO é um palíndromo!')