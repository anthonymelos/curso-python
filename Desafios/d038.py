#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor e maior
# O segundo valor e maior 
# Os valores são iguais

print('Desafio 38')

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

if n1 > n2:
    print('O primeiro valor é maior')

elif n2 > n1:
    print('O segundo valor é maior')

else: 
    print('Os valores são iguais')
 