#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('Desafio 20')

alunos = []

alunos.append(input('Informe o nome do 1° aluno: '))
alunos.append(input('Informe o nome do 2° aluno: '))
alunos.append(input('Informe o nome do 3° aluno: '))
alunos.append(input('Informe o nome do 4° aluno: '))

shuffle(alunos)

print(f'A ordem de apresentação será {alunos}')