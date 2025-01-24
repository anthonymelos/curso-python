#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%

print('Desafio 13')

salario = float(input('Qual o seu salário? '))

salario = salario + (salario * 0.15)

print(f'Com o aumento de 15%, seu salário passou a ser {salario:.2f}')