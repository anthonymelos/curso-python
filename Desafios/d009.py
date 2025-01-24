#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

print('Desafio 9')

num = int(input('Informe um número: '))

print('_' * 12) #Isso replica as strings o números de vezes que se quiser
for i in range(1, 11):
    print(f'{num} * {i} = {num * i}')

print('_' * 12)