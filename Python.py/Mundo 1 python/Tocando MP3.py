import pygame
pygame.mixer.init()
pygame.mixer.music.load('uruguay.mp3')
pygame.mixer.music.play()
input('Pressione enter para reprodução')
pygame.mixer.stop