#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex:
#Digite um número: 1834
#Unidade: 4, dezena: 3, centena 8, milhar: 1

print('Desafio 23')

num = (input('Digite um número entre 0 e 9999: '))

if num > 9:
    num[2] = 0

if num > 99:
    num[1] = 0

if num < 999: 
    num[0] = 0

print(f'Milhar: {num[0]} Centena: {num[1]} Dezena: {num[2]} Unidade: {num[3]}')
