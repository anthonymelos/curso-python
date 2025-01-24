#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sebendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

print('Desario 15')

kmPercorrido = float(input('Quantos km foram percorridos no carro? '))

qtdDias = int(input('Por quantos dias o carro foi locado? '))

total = (qtdDias * 60) + (kmPercorrido * 0.15)

print(f'O total a pagar é R${total:.2f}')