#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3

print('Desafio 21')

import pygame

#Comando para instalar a biblioteca: pip install pygame 

pygame.init() #Essa biblioteca deve ser iniciada

pygame.mixer.music.load('d021.mp3')
pygame.mixer.music.play()
pygame.event.wait()