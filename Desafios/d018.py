#Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

print('Desafio 18')

co = int(input('Qual a medida do cateto oposto? '))

ca = int(input('Qual a medida do cateto adjascente? '))

hip = math.hypot(co, ca)

print(f'A medida da hipotenusa é {hip}')