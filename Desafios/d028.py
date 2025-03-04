#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('Desafio 28')
print('-' * 10)

from random import randint

import time #biblioteca de tempo

numero = int(input('Tente adivinhar um número de 0 a 5: '))

numC = randint(0,5)

print('PROCESSANDO...')
time.sleep(2) #Método sleep que espera por 2 segundos

if numC == numero:
    print(f'Você ganhou! ')

else: 
    print(f'Você perdeu! Pensei no número {numC}')

