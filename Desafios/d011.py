#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

import math

print('Desafio 11')
largura = float(input('Qual a largura da parede? '))

altura = float(input('Qual a altura da parede? '))

metrosquad = largura * altura
#função que arredonda o valor para cima, para pintar toda a parede sem faltar espaços sem pintar, ou seja, tinta sobrando.
res = math.ceil(metrosquad / 2)

print(f'{res :.0f} latas de tinta são necessárias para pintar a parede \n')
