#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#from math import radians, sin, cos, tan
import math
print('Desafio 19')

angulo = float(input('Informe um ângulo a ser mostrado seus valores: '))

anguloG = math.radians(angulo)

print(f'O seno é {math.sin(anguloG):.2f}\nO cosseno é {math.cos(anguloG):.2f}\nE a tangente é {math.tan(anguloG):.2f}')


