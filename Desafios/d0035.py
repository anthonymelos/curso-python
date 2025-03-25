#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Desafio 35')

r1 = int(input('Informe o comprimento da 1° reta: '))

r2 = int(input('Informe o comprimento da 1° reta: '))

r3 = int(input('Informe o comprimento da 1° reta: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Os comprimentos de reta informados não formam um triângulo! ')

else: 
    print('Os comprimentos informados são válidos!')
