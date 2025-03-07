#Números maior e menor 

print('Desafio 33')

num1 = int(input('Informe um número: '))
num2 = int(input('Informe um número: '))
num3 = int(input('Informe um número: '))

if num1 > num2 and num1 > num3:
    print(f'O número {num1} é maior!')
    if num2 > num3:
        print(f'O número {num3} é menor!')
    else:
        print(f'O número {num2} é menor!')

if num2 > num3 and num2 > num1:
    print(f'O número {num2} é maior!')
    if num3 > num1:
        print(f'O número {num1} é menor!')
    else:
        print(f'O número {num3} é menor!')

if num3 > num2 and num3 > num1:
    print(f'O número {num3} é maior!')
    if num1 > num2:
        print(f'O número {num2} é menor!')
    else:
        print(f'O número {num1} é menor!')