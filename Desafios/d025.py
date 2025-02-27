#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

print('Desafio 25')

nome = input('Digite o nome: ').strip()#Remove espaços antes e depois

nome = nome.lower() #Primeira letra do nome é maiúscula

print('silva' in nome)