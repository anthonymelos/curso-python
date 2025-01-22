#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.

print('Desafio 04')

dado = input('Entre com a informação: ')

print(type(dado),'\n\n')

print(f'{dado} é alfabético?', dado.isalpha())
print(f'{dado} é númerico?', dado.isnumeric())
print(f'{dado} está em caixa alta?', dado.isupper())
print(f'{dado} está em caixa baixa?', dado.islower())
print(f'{dado} é alfanumerico?', dado.isalnum())