#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite. 

print('Desafio 29')

vel = int(input('Qual a sua velocidade atual? '))

if vel > 80:
    print('Velocidade acima do permitido na via de 80 km/h')

    excedente = vel - 80
    multa = excedente * 7
    multa = float(multa)
    
    print(f'A multa será de R${multa:.2f}')

else:
    print('Velocidade permitida! ')