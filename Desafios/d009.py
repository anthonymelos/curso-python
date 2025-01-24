#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

print('Desafio 9')

num = int(input('Informe um número: '))
for i in range(1, 11):
    print(f'{num} * {i} = {num * i}')