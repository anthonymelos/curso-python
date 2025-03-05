#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas. 

print('Desafio 30')

print('=-' * 20)

distancia = float(input('Qual a distância da viagem que você vai fazer (em km)? '))

if distancia <= 200:
    preco = distancia * 0.5
    print(f'O valor da passagem é R${preco:.2f}')

else:
    preco = distancia * 0.45
    print(f'O valor da passagem é R${preco:.2f}')