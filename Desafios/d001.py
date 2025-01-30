#Crie um script que python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de
#acordo com o valor digitado

nome = input('Olá, informe seu nome: ')
print('Seja bem vindo ', nome, '!')

#Também pode ser feito de outro jeito, uma formatação (string format):

print(f'Olá, {nome}! Seja bem vindo(a)')

#Outro exemplo:

x = 5
y = 3
print(f'A soma de {x} e {y} é {x + y}')

print(type(x))
print(type(nome))

print(nome.isupper())

