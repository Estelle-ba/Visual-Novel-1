# Encodage : UTF8
# Python 3.9
# Auteur : Estelle Bandhavong
import pygame
from pygame.locals import *

pygame.init()
import time
font = pygame.font.Font('freesansbold.ttf', 32)
largeur_ecran = 1300
hauteur_ecran = 655
blanc=(255,255,255)
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

def au_revoir_jeu(evenement):
    if evenement.type == pygame.QUIT:
        return True
    elif evenement.type == KEYDOWN:
        touche = evenement.key
        if touche == K_ESCAPE:
            return True





