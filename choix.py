import pygame
from pygame.locals import *
from image import image, el_boutton
from fonction import au_revoir_jeu

largeur_ecran = 1300
hauteur_ecran = 655
blanc = (255, 255, 255)
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
ecran.fill(blanc)
pygame.display.flip()
choix_1 = pygame.image.load("brouillard_question.png")
choix_2 = pygame.image.load("brouillard_question.png")
image_choix_1 = el_boutton((largeur_ecran-1100)/2, (hauteur_ecran-(28*2))/3, 28, 1100)
image_choix_2 = el_boutton((largeur_ecran-1100)/2, ((hauteur_ecran-(28*2))/3)*2+28, 28, 1100)
font = pygame.font.Font('freesansbold.ttf', 32)

choix = True



# {joueur.prenom{ => prénom
# {joueur.genremini{ => le genre du joueur en miniscule
# {joueur.genremasc{ => le genre du joueur en majuscule
# {joueur.cible.genremini{ => le genre de la cible en miniscule
# {joueur.cible.genremasc{ => le genre de la cible en majuscule
# {joueur.ennemi.genremini{ => le genre de la ennemi en miniscule
# {joueur.ennemi.genremasc{ => le genre de la ennemi en majuscule
while A:
    for evenement in pygame.event.get():
        ecran.fill(blanc)
        pygame.display.set_caption("Faut faire un choix")
        ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
        histoire_1 = f""
        texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
        ecran.blit(texte_truc_1, (0, 477))
        pygame.display.update()
        if au_revoir_jeu(evenement) == True:
            A = False

        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_RETURN:
                A = False
                choix = True
while choix:
    for evenement in pygame.event.get():
        pygame.display.set_caption("Faut faire un choix")
        souris = pygame.mouse.get_pos()
        ecran.blit(choix_1, image_choix_1.coordonnees)
        ecran.blit(choix_2, image_choix_2.coordonnees)
        choix_1_ecrit = f""
        choix_2_ecrit = f""
        texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
        texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
        ecran.blit(texte_choix_1, image_choix_1.coordonnees)
        ecran.blit(texte_choix_2, image_choix_2.coordonnees)
        pygame.display.flip()
        if au_revoir_jeu(evenement) == True:
            choix = False
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[1] <= \
                    image_choix_1.carre[3]:
                choix = False
                AA = True
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                    image_choix_2.carre[3]:
                choix = False
                AB = True

