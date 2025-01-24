#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar considerando o dolár R$1,00 = US$5,93.

print('Desafio 10')
dinheiro = float(input('Quantos reais você tem em sua carteira? R$'))
print(f'R${dinheiro:.2f} vale US${dinheiro / 5.93:.2f}')
