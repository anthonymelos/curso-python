#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

print('Desafio 26')

frase = str(input('Digite uma frase: ')).strip()

frase = frase.lower()
 
print(f'A frase contém {frase.count('a')} letra(s) A ')

print(f'{frase.find('a') + 1} é a posição da string que ela aparece pela primeira vez')

print(f'{frase.rfind('a') + 1} é a posição da string que ela aparece pela última vez') #rfind significa que se irá procurar a letra 'a' a partir da direita

