#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

from math import trunc

#import math

print('Desafio 17')

num = float(input('Informe um número real: '))
print(f'O número sem casas decimais é: {trunc(num)}')

#O método trunc remove a parte inteira do número

#Outro jeito de ser feito:

print(f'Outro jeito de ser feito: {int(num)}')
