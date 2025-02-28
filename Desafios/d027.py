#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro: Ana 
#último: Souza

print('Desafio 27')

nome = str(input('Informe seu nome completo: ')).strip()

print(f'{nome} é seu nome completo ')

nome = nome.split()

print(f'Primeiro nome: {nome[0]}')

print(f'O último nome: {nome[-1]}')#outra solução seria usar o nome[len(nome)]


