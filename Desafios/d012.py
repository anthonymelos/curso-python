#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

print('Desafio 12')

preco = float(input('Qual o preço original do produto? '))

preco = preco - (preco * 0.05)

print(f'O preço do produto com desconto de 5% é {preco:.2f}')