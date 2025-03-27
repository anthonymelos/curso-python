#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
# 1 Binario
# 2 octal
# 3 hexadecimal


print('Desafio 36')

numero = int(input('Informe um número inteiro: '))
base = int(input('Base de conversão: 1- Binario | 2- Octal | 3- Hexadecimal \n'))

if base == 1:
    print(f'O número convertido é: {bin(numero)}')

elif base == 2:
    print(f'O número convertido é: {oct(numero)}')

else:
    print(f'O número convertido é: {hex(numero)}')


