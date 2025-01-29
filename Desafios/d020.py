#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

print('Desafio 20')

alunos = []

alunos.append(input('Informe o nome do 1° aluno: ')) #Função append acresenta os valores no final do vetor 
alunos.append(input('Informe o nome do 2° aluno: '))
alunos.append(input('Informe o nome do 3° aluno: '))
alunos.append(input('Informe o nome do 4° aluno: '))


print(f'O aluno escolhido foi {random.choice(alunos)}')




