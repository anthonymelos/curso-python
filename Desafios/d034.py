#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.

print('Desafio 34')

salario = float(input('Qual o valor de seu salário? R$'))

if salario > 1250:
    nSalario = (salario * 0.1) + salario
    print(f'Seu novo salário é R${nSalario:.2f}')
else:
    nSalario = (salario * 0.15) + salario
    print(f'Seu novo salário é R${nSalario:.2f}')
