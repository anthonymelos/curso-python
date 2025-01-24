#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

print('Desafio 14')

temperaturaC = int(input('Qual a temperatura em °C? '))

temperaturaF = temperaturaC * 1.8 + 32

temperaturaK = temperaturaC + 273

print(f'A temperatura: {temperaturaC}°C para {temperaturaF}°F e {temperaturaK}K')