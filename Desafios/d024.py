#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

print('Desafio 24')

nome = input('Digite o nome da sua cidade: ').strip()

nome = nome.capitalize()

print('Santo' in nome)