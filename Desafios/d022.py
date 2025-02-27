#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.

print('Desafio 22')


nome = input('Digite seu nome completo: ').strip()

print(f'O nome com as letras maiúsculas: {nome.upper()}')
print(f'O nome com todas as letras minúsculas: {nome.lower()}')

print(f'O nome possui {len(nome) - nome.count(' ')} letras')


primNome = nome.split()

print(f'O primeiro nome tem {len(primNome[0])} letras!')

#Outra forma de ver quantas letras tem o primeiro nome:

print(f'Outra forma de ver quantas letras tem o primeiro nome: {nome.find(' ')} letras')

