#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex:
#Digite um número: 1834
#Unidade: 4, dezena: 3, centena 8, milhar: 1

print('Desafio 23')

num = int(input('Digite um número entre 0 e 9999: '))

#n = str(num) #Transforma o número em string

print(f'Analisando o número {num}')

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d} ')
print(f'Unidade: {u}')
