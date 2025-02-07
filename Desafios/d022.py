#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.

print('Desafio 22')


nome = input('Digite seu nome completo: ')

print(f'O nome com as letras maiúsculas: {nome.upper()}')
print(f'O nome com todas as letras minúsculas: {nome.lower()}')

print(f'O nome possui {len(nome)} letras')


