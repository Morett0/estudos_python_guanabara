# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


a = int(input('Digite um número para ver a tabuada: '))
for b in range(1, 11):
    print(f'{a} x {b:2} = {a*b}')
    
