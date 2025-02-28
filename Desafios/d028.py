#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('Desafio 28')

import random 

numero = int(input('Tente adivinhar um número de 1 a 5: '))

numC = random.randint(1,5)

if numC == numero:
    print(f'Você ganhou! ')

else: 
    print('Você perdeu! ')

