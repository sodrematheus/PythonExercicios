#Tocando uma música
import pygame
pygame.init()
pygame.mixer.music.load('Maresia.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
