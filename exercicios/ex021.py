# Faça um programa em python que abra e reproduza o áudio de um arquiv0 MP3.

import pygame
pygame.init()
pygame.mixer.music.load("C:/Users/nicol/Downloads/music.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()