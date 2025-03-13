# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#  quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinha, pinta uma área de 2m².

l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))
print(f'Sua parete tem uma dimensão de {l:.2f}mx{a:.2f}m e sua área é de {(l*a):.2f}m²')
print(f'Para pintar esasa parede, você precisará de {(l*a)/2:.2f}l de tinta')
