#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.


print('Desafio 35')

valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Informe o seu salario: '))
tempo = int(input('Pretende pagar em quantos anos? '))

numeroParcelas = tempo * 12 #de anos para meses
valorParcela = valorCasa / numeroParcelas


verificaSalario = salario + (salario * 0.3)

if valorParcela > verificaSalario:
    print('Empréstimo negado! Seu salario é menor que o valor permitido de 30%')

else:
    print(f'Você optou por {numeroParcelas} parcelas no valor de R${valorParcela:.2f} cada.')
    print('Empréstimo concedido!')