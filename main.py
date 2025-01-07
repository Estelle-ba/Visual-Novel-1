# import du module pygame
import pygame
from fonction import au_revoir_jeu
from image import image, el_boutton
from Joueur_type import Bandit, Aventurier, Sorcier, Snow, Sylas, Dora, Roudolf, Hazel, Merlin
clock = pygame.time.Clock()
from random import randint

# définition de la fonction principale de jeu


def jeu():

# Initialisation de pygame
    pygame.init()

# Création d'un écran
    largeur_ecran = 1300
    hauteur_ecran = 655
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))


#Création des boutons
    image_start = pygame.image.load("assets/ceut.png")
    image_start_donnees = el_boutton(50, 327, 84, 342)
    image_choix_bandit = pygame.image.load("assets/choix_1.png")
    image_choix_bandit_donnees = el_boutton(50, 112, 59, 69)
    image_choix_aventurier = pygame.image.load("assets/choix_2.png")
    image_choix_aventurier_donnees = el_boutton(image_choix_bandit_donnees.coordonnees[0], image_choix_bandit_donnees.coordonnees[1] + 181, 59, 69)
    image_choix_sorcier = pygame.image.load("assets/choix_3.png")
    image_choix_sorcier_donnees = el_boutton(image_choix_bandit_donnees.coordonnees[0], image_choix_aventurier_donnees.coordonnees[1] + 181 , 59, 69)
    image_choix_femme = el_boutton(450, 25, 558, 205)
    image_choix_homme = el_boutton(image_choix_femme.coordonnees[0] + 250, image_choix_femme.coordonnees [1], 558, 205)
    choix_1 = pygame.image.load("assets/brouillard_question.png")
    choix_2 = pygame.image.load("assets/brouillard_question.png")
    image_choix_1 = el_boutton((largeur_ecran-1100)/2, (hauteur_ecran-(28*2))/3, 28, 1100)
    image_choix_2 = el_boutton((largeur_ecran-1100)/2, ((hauteur_ecran-(28*2))/3)*2+28, 28, 1100)
    choix_3 = pygame.image.load("assets/brouillard_question.png")
    choix_4 = pygame.image.load("assets/brouillard_question.png")
    image_choix_3 = el_boutton((largeur_ecran - 1100) / 2, ((image_choix_1.y + image_choix_2.y ) / 2), 28, 1100)

# Les images des personnages
    image_bases = pygame.image.load("assets/characters/basesF.png")
    image_bases_2 = pygame.image.load("assets/characters/basesM.png")
    image_1 = image_bases
    image_2 = image_bases_2
    image_bandit = pygame.image.load("assets/characters/banditF.png")
    image_bandit_2 = pygame.image.load("assets/characters/banditM.png")
    image_aventurier_2 = pygame.image.load("assets/characters/aventurierM.png")
    image_aventurier = pygame.image.load("assets/characters/aventurierF.png")
    image_sorcier = pygame.image.load("assets/characters/sorcierF.png")
    image_sorcier_2 = pygame.image.load("assets/characters/sorcierM.png")
    joueurnormal = None
    joueurreflechi = None
    perso1 = None
    perso2 = None
    perso3 = None

# Les images des animaux
    cerbere = pygame.image.load("assets/animals/cerbere.png")
    chat = pygame.image.load("assets/animals/chat.png")
    chauvesouris = pygame.image.load("assets/animals/chauvesouris.png")
    dragon = pygame.image.load("assets/animals/dragon.png")
    griffon = pygame.image.load("assets/animals/griffon.png")
    pheonix = pygame.image.load("assets/animals/phenix.png")
    requinlutin = pygame.image.load("assets/animals/requinlutin.png")
    chupacabra = pygame.image.load("assets/animals/chupacabry.png")

# Les images d'objets
    arc = pygame.image.load("assets/objects/arc.png")
    baguette = pygame.image.load("assets/objects/baguette.png")
    balai = pygame.image.load("assets/objects/balai.png")
    boussole = pygame.image.load("assets/objects/boussole.png")
    epee = pygame.image.load("assets/objects/epee.png")
    gamyris = pygame.image.load("assets/objects/gamyris.png")
    hypolys= pygame.image.load("assets/objects/hypolys.png")
    monnaie1 = pygame.image.load("assets/objects/monnaieA_B.png")
    monnaie2 = pygame.image.load("assets/objects/monnaieS.png")
    orphenea = pygame.image.load("assets/objects/orphénéa.png")
    pistolet = pygame.image.load("assets/objects/pistolet.png")
    rhyseas = pygame.image.load("assets/objects/rhyseas.png")
    potions = pygame.image.load("assets/objects/potions.png")
    hache = pygame.image.load("assets/objects/hache.png")

#image pour le texte
    brouillard = pygame.image.load("assets/brouillard.png")
    brouillard_donnees = image (0, 0)
    brouillard_histoire = pygame.image.load("assets/brouillard_ecrit.png")
    brouillard_histoire_donnees = image(0, 477)
    choisir_un_nom = pygame.image.load("assets/choisir_nom.png")
    choisir_un_nom_donnees = image((largeur_ecran-351)//2, (hauteur_ecran-226)//2)
    image_choix_1_4 = el_boutton((largeur_ecran-1100)/2, (hauteur_ecran-(28*4))/5, 28, 1100)
    image_choix_2_4 = el_boutton((largeur_ecran-1100)/2, ((hauteur_ecran-(28*4))/5)*2+28, 28, 1100)
    image_choix_3_4 = el_boutton((largeur_ecran-1100)/2, ((hauteur_ecran-(28*4))/5)*3+28*2, 28, 1100)
    image_choix_4 = el_boutton((largeur_ecran-1100)/2, ((hauteur_ecran-(28*4))/5)*4+28*3, 28, 1100)
    potion = ""

#décors
    bar = pygame.image.load("assets/backgrounds/bar.png")
    demarrer_image = pygame.image.load("assets/backgrounds/choixperso.png")
    ville_bandit = pygame.image.load("assets/backgrounds/villeB.png")
    ville_aventurier = pygame.image.load("assets/backgrounds/villeA.png")
    ville_sorcier = pygame.image.load("assets/backgrounds/villeS.png")
    marchand_bandit = pygame.image.load("assets/backgrounds/marchandB.png")
    marchand_aventurier = pygame.image.load("assets/backgrounds/marchandA.png")
    marchand_sorcier = pygame.image.load("assets/backgrounds/marchandS.png")
    foret1 = pygame.image.load("assets/backgrounds/foret1.png")
    foret2 = pygame.image.load("assets/backgrounds/foret2.png")
    foret3 = pygame.image.load("assets/backgrounds/foret3.png")

# Les personnages et leurs placements
    Dorareflechi = pygame.image.load("assets/characters/Dorareflechi.png")
    Doranormal = pygame.image.load("assets/characters/Doranormal.png")
    Hazelreflechi = pygame.image.load("assets/characters/Hazelreflechi.png")
    Hazelnormal = pygame.image.load("assets/characters/Hazelnormal.png")
    Merlinreflechi = pygame.image.load("assets/characters/Merlinreflechi.png")
    Merlinnormal = pygame.image.load("assets/characters/Merlinnormal.png")
    Roudolfreflechi = pygame.image.load("assets/characters/Roudolfreflechi.png")
    Roudolfnormal = pygame.image.load("assets/characters/Roudolfnormal.png")
    Snowreflechi = pygame.image.load("assets/characters/Snowreflechi.png")
    Snownormal = pygame.image.load("assets/characters/Snownormal.png")
    Sylasreflechi = pygame.image.load("assets/characters/Sylasreflechi.png")
    Sylasnormal = pygame.image.load("assets/characters/Sylasnormal.png")
    perso_seul = ((largeur_ecran-317)/2, 92)
    perso_deux_1 = ((largeur_ecran-317*2)/3, 92)
    perso_deux_2 = (((largeur_ecran-317*2)/3)*2+317, 92)
    perso_trois_1 = ((largeur_ecran-317*3)/4, 92)
    perso_trois_2 = (((largeur_ecran-317*3)/4)*3+317*2, 92)

#Boucles pour démarrer
    demarrer = True
    choix = False
    bandit = False
    aventurier = False
    sorcier = False
    choix_du_nom = False
    genre = ""

#Le texte
    font = pygame.font.Font('freesansbold.ttf', 32)
    nom = ""
    texte_1 = ""
    texte_2 = ""
    histoire_1 = ""
    histoire_2 = ""
    histoire_3 = ""
    histoire_4 = ""
    histoire_5 = ""
    histoire_6 = ""
    character_6 = ""
    texte_fin = ""
    input_active = True

#On définit le joueur
    joueur = None
    suite = False
    suite_2 = False

#On définit les autres personnages
    bandit_tirage_au_sort = randint(1,10)
    aventurier_tirage_au_sort = randint(1,10)
    sorcier_tirage_au_sort = randint(1,10)

    if bandit_tirage_au_sort%2 == 1:
        bandit_personnage = Snow
        bandit_normal = Snownormal
    else :
        bandit_personnage = Sylas
        bandit_normal = Sylasnormal

    if aventurier_tirage_au_sort%2 == 1:
        aventurier_personnage = Dora
        aventurier_normal = Doranormal
    else :
        aventurier_personnage = Roudolf
        aventurier_normal = Roudolfnormal

    if sorcier_tirage_au_sort %2 == 1:
        sorcier_personnage = Hazel
        sorcier_normal = Hazelnormal
    else :
        sorcier_personnage = Merlin
        sorcier_normal = Merlinnormal

#Les choix du bandit/ bandite. Ils sont définis par les lettres A et B et varient selon les choix.
    A = False
    B = False
    AA = False
    AB = False
    BA = False
    BB = False
    AAA = False
    AAB = False
    ABA = False
    ABB = False
    BAA = False
    BAB = False
    BBA = False
    BBB = False
    AAAA = False
    AAAB = False
    AABA = False
    AABB = False
    ABBA = False
    ABBB = False
    BAAA = False
    BAAB = False
    BBAB = False
    AAAAAA = False
    AABAA = False
    BAAAA = False
    BAAAB = False
    AABBBA = False
    AAAAAB = False
    BABA = False
    AAAAA = False
    AAAAB = False
    AAABB = False
    AABBB = False
    ABBAA = False
    ABBBA = False
    BAABBABB = False
    BAABBABA = False
    BAABBAB = False
    BAABBAA = False
    BAABAAB = False
    BAABAAA = False
    BAAABAB = False
    BAAABAA = False
    BBABBAABBA = False
    BBABBAABB = False
    BBABBAABA = False
    BBABBAAB = False
    BBABBAAA = False
    BBABBAA = False
    AABAAAAB = False
    AABAAAA = False
    AABAABA = False
    AAAAAAA = False
    BBABBA = False
    BBABBB = False
    BAABBA = False
    BAABAA = False
    BAAABA = False
    ABBBAA = False
    AABAAA = False
    AABAAB = False
    AABAAAB = False
    BABAA = False
    BBABB = False
    BAABB = False
    BAABA = False

# Les choix de l'aventurier/ aventurière. Ils sont définis par les lettres C et D et varient selon les choix
    C = False
    D= False
    CC = False
    CD = False
    CCC = False
    CDC = False
    CCD = False
    DCCC = False
    DCDCD = False
    DCDCCD = False
    CDD = False
    CCCC = False
    CCCD = False
    CCDC = False
    CDCC = False
    CDDC = False
    CDDD = False
    CDDCC = False
    CCCCC = False
    CCDCC = False
    CDCD = False
    CDDCD = False
    CDDDC = False
    CDDDD = False
    CDCDD = False
    CDCCD = False
    CDCCDC = False
    CDDCDC = False
    CDDDDD = False
    CDDDDC = False
    CDDDCC = False
    DC = False
    DCC = False
    DCCDD = False
    DCCDDC = False
    DCCDC = False
    DCCDCC = False
    DCCDCCD = False
    DCCDCCC = False
    DCCDCD = False
    DCD = False
    DCDC = False
    DCDCC = False
    DCDCCC = False
    DD = False
    DCDD = False
    DCDDC = False
    DCDCDC = False
    DDC = False
    DDCC = False
    DCDCDCD = False
    DDCDD = False
    DDD = False
    DDCD = False
    DDDC = False
    DDDDC = False


# Les choix de le sorcier/ la sorcière. Ils sont définis par les lettres E et F et varient selon les choix
    EFEEFE = False
    EFFE = False
    EEFE = False
    EFEE = False
    EEEF = False
    E = False
    EE = False
    EF = False
    EEE = False
    EEF = False
    EFE = False
    EFF = False
    EEEE = False
    EFFF = False
    EFFEE = False
    EEEEE = False
    EEFEE = False
    EFEF = False
    EFFEF = False
    EFFFE = False
    EFFFF = False
    EFEFF = False
    EFEEF = False
    EFFEFE = False
    EFFFFF = False
    EFFFFE = False
    EFFFEE = False
    F = False
    FE = False
    FF = False
    FEE = False
    FEF = False
    FFE = False
    FFF = False
    FEFE = False
    FEFF = False
    FFEE = False
    FFEF = False
    FEEFF = False
    FEEFE = False
    FEEE = False
    FEFEF = False
    FEFFE = False
    FEFEE = False
    FFFFE = False
    FEEFFE = False
    FEEFEE = False
    FEEFEF = False
    FEFEFE = False
    FEEFEEF = False
    FEFEEF = False
    FEEFEEE = False
    FEFEEE = False
    FEFEFEF = False
    FFEFF = False
    FFFE = False



# Les deux boucles pour terminer
    perdu = False
    gagner = False
    image_perdu = pygame.image.load("assets/perdu.png")
    image_gagner = pygame.image.load("assets/gagner.png")

#Début du jeu

    while demarrer:
        for evenement in pygame.event.get():
            ecran.blit(demarrer_image, (0,0))
            ecran.blit(image_start, image_start_donnees.coordonnees)
            pygame.display.set_caption("Avant de jouer")
            pygame.display.update()
            souris = pygame.mouse.get_pos()


            if au_revoir_jeu(evenement)== True:
                demarrer = False

            if evenement.type == pygame.MOUSEBUTTONDOWN :
                if image_start_donnees.carre[0] <= souris[0] <= image_start_donnees.carre[1] and image_start_donnees.carre[2] <= souris[1] <= image_start_donnees.carre[3]:
                    demarrer = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():

            ecran.blit(demarrer_image, (0,0))
            pygame.display.set_caption("Faut faire un choix")
            ecran.blit(image_choix_bandit, image_choix_bandit_donnees.coordonnees)
            ecran.blit(image_choix_aventurier, image_choix_aventurier_donnees.coordonnees)
            ecran.blit(image_choix_sorcier, image_choix_sorcier_donnees.coordonnees)
            ecran.blit(image_2, image_choix_homme.coordonnees)
            ecran.blit(image_1, image_choix_femme.coordonnees)
            pygame.display.update()
            souris = pygame.mouse.get_pos()

            if au_revoir_jeu(evenement) == True:
                choix = False

            if evenement.type == pygame.MOUSEBUTTONDOWN :
                if image_choix_bandit_donnees.carre[0] <= souris[0] <= image_choix_bandit_donnees.carre[1] and image_choix_bandit_donnees.carre[2] <= souris[1] <= image_choix_bandit_donnees.carre[3]:
                    image_1 = image_bandit
                    image_2 = image_bandit_2
                    pygame.display.update()

            if evenement.type == pygame.MOUSEBUTTONDOWN :
                if image_choix_aventurier_donnees.carre[0]<=souris[0]<=image_choix_aventurier_donnees.carre[1] and image_choix_aventurier_donnees.carre[2]<=souris[1]<=image_choix_aventurier_donnees.carre[3]:
                    image_1 = image_aventurier
                    image_2 = image_aventurier_2
                    pygame.display.update()

            if evenement.type == pygame.MOUSEBUTTONDOWN :
                if image_choix_sorcier_donnees.carre[0]<=souris[0]<=image_choix_sorcier_donnees.carre[1] and image_choix_sorcier_donnees.carre[2]<=souris[1]<=image_choix_sorcier_donnees.carre[3]:
                    image_1 = image_sorcier
                    image_2 = image_sorcier_2
                    pygame.display.update()

            if image_1 == image_bandit:
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    if image_choix_femme.carre[0] <= souris[0] <= image_choix_femme.carre[1] and image_choix_femme.carre[2] <= souris[1] <= image_choix_femme.carre[3]:
                        choix = False
                        choix_du_nom = True
                        bandit = True
                        genre = "f"

                    if image_choix_homme.carre[0] <= souris[0] <= image_choix_homme.carre[1] and image_choix_homme.carre[2] <= souris[1] <= image_choix_homme.carre[3]:
                        choix = False
                        choix_du_nom = True
                        bandit = True
                        genre = "m"
            if image_1 == image_aventurier:
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    if image_choix_femme.carre[0] <= souris[0] <= image_choix_femme.carre[1] and image_choix_femme.carre[2] <= souris[1] <= image_choix_femme.carre[3]:
                        choix = False
                        choix_du_nom = True
                        aventurier = True
                        genre = "f"

                    if image_choix_homme.carre[0] <= souris[0] <= image_choix_homme.carre[1] and image_choix_homme.carre[2] <= souris[1] <= image_choix_homme.carre[3]:
                        choix = False
                        choix_du_nom = True
                        aventurier = True
                        genre = "m"
            if image_1 == image_sorcier:
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    if image_choix_femme.carre[0] <= souris[0] <= image_choix_femme.carre[1] and image_choix_femme.carre[2] <= souris[1] <= image_choix_femme.carre[3]:
                        choix = False
                        choix_du_nom = True
                        sorcier = True
                        genre = "f"

                    if image_choix_homme.carre[0] <= souris[0] <= image_choix_homme.carre[1] and image_choix_homme.carre[2] <= souris[1] <= image_choix_homme.carre[3]:
                        choix = False
                        choix_du_nom = True
                        sorcier = True
                        genre = "m"
    while choix_du_nom:

        clock.tick(60)
        for evenement in pygame.event.get():
            pygame.display.set_caption("Faut faire un choix")
            ecran.blit(demarrer_image, (0, 0))
            pygame.display.set_caption("Faut faire un choix")
            ecran.blit(image_choix_bandit, image_choix_bandit_donnees.coordonnees)
            ecran.blit(image_choix_aventurier, image_choix_aventurier_donnees.coordonnees)
            ecran.blit(image_choix_sorcier, image_choix_sorcier_donnees.coordonnees)
            ecran.blit(image_2, image_choix_homme.coordonnees)
            ecran.blit(image_1, image_choix_femme.coordonnees)
            ecran.blit(brouillard, brouillard_donnees.coordonnees)
            ecran.blit(choisir_un_nom, choisir_un_nom_donnees.coordonnees)
            pygame.display.update()

            if au_revoir_jeu(evenement) == True:
                choix_du_nom = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                    input_active = True
                    nom = ""
            elif evenement.type == pygame.KEYDOWN and input_active:
                if evenement.key == pygame.K_RETURN and nom != "":
                    input_active = False
                    choix_du_nom = False
                elif evenement.key == pygame.K_BACKSPACE:
                    nom = nom[:-1]
                else:
                    nom += evenement.unicode

            texte_truc = font.render(nom, True, (255, 255, 255))
            ecran.blit(texte_truc, (choisir_un_nom_donnees.coordonnees[0]+60, choisir_un_nom_donnees.coordonnees[1] + 125))
            pygame.display.flip()

#On crée l'instance joueur
    if bandit == True:
        joueur = Bandit(nom, genre)
        if genre == "f":
            joueur.genremasc = "La bandite"
            joueur.genremini = "la bandite"
            joueur.nom_de_ville = "d'Arcanélume"
            joueur.ennemi = sorcier_personnage
            joueur.cible = aventurier_personnage
            joueurnormal = Snownormal
            joueurreflechi = Snowreflechi
        else:
            joueur.genremasc = "Le bandit"
            joueur.genremini = "le bandit"
            joueur.nom_de_ville = "d'Arcanélume"
            joueur.ennemi = sorcier_personnage
            joueur.cible = aventurier_personnage
            joueurnormal = Sylasnormal
            joueurreflechi = Sylasreflechi
    elif aventurier == True:
        joueur = Aventurier(nom, genre)
        if genre == "f":
            joueur.genremasc = "L'aventurière"
            joueur.genremini = "l'aventurière"
            joueur.nom_de_ville = ""
            joueur.ennemi = Snow
            joueur.cible = sorcier_personnage
            joueurnormal = Doranormal
            joueurreflechi = Dorareflechi
            aventurier_normal = Roudolfnormal
        else:
            joueur.genremasc = "L'aventurier"
            joueur.genremini  = "l'aventurier"
            joueur.nom_de_ville = ""
            joueur.ennemi = bandit_personnage
            joueur.cible = sorcier_personnage
            joueurnormal = Roudolfnormal
            joueurreflechi = Roudolfreflechi
            aventurier_normal = Doranormal
    elif sorcier == True:
        joueur = Sorcier(nom, genre)
        if genre == "f":
            joueur.genremasc = "La sorcière"
            joueur.genremini  = "la sorcière"
            joueur.ennemi = aventurier_personnage
            joueur.cible = bandit_personnage
            joueurnormal = Hazelnormal
            joueurreflechi = Hazelreflechi
            sorcier_normal = Merlinnormal
        else:
            joueur.genremasc = "Le sorcier"
            joueur.genremini  = "le sorcier"
            joueur.nom_de_ville = ""
            joueur.ennemi = aventurier_personnage
            joueur.cible = bandit_personnage
            joueurnormal = Merlinnormal
            joueurreflechi = Merlinreflechi
            sorcier_normal = Hazelnormal



# Partie du bandit
    while bandit:
        for evenement in pygame.event.get():
            ecran.blit(demarrer_image, (0,0))
            pygame.display.set_caption("BANDIT")
            perso1 = aventurier_normal
            perso2 = joueurnormal
            perso3 = sorcier_normal
            ecran.blit(perso1, perso_trois_1)
            ecran.blit(perso2, perso_seul)
            ecran.blit(perso3, perso_trois_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Un jour, {joueur.prenom} apprit qu'un célèbre aventurier nommé {joueur.cible.prenom} avait découvert"
            histoire_2 = f"un trésor légendaire caché dans un endroit perdu depuis des siècles. Ce trésor"
            histoire_3 = f"était composé d'objets rare ainsi qu une somme importante d or. {joueur.prenom}, aveuglé"
            histoire_4 = f"par l'appât du gain, décida de tout mettre en œuvre pour s'emparer de ces"
            histoire_5 = f"objets rares et de l’or. Ainsi, dans ce monde fantastique, les destins de {joueur.prenom}"
            histoire_6 = f"de l’aventurier {joueur.cible.prenom} et du {joueur.ennemi.genremini} {joueur.ennemi.prenom} étaient étroitement liés par un"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()

            if au_revoir_jeu(evenement) == True:
                bandit = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    bandit= False
                    suite = True
    while suite:
        for evenement in pygame.event.get():
            ecran.blit(demarrer_image, (0,0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"enchevêtrement d'ambitions, de trésors et de quêtes pour des objets magiques d'une"
            histoire_2 = f"importance cruciale. Les prochains chapitres de leur histoire promettaient"
            histoire_3 = f"des aventures épiques, des confrontations magiques et des choix moraux"
            histoire_4 = f"déchirants."
            histoire_5 = f""
            histoire_6 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                suite = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    suite = False
                    suite_2 = True
    while suite_2:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0,0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            histoire_1 = f"{joueur.genremasc} arrive dans la ville {joueur.nom_de_ville}, sa ville natale et préférée"
            histoire_2 = f"{joueur.prenom} se balade afin de trouver le bar le plus célèbre à cotoyer."
            histoire_3 = f"Après quelques temps de marche, il entre dans le bar en regardant autour"
            histoire_4 = f"de lui."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                suite_2 = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    suite_2 = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            souris = pygame.mouse.get_pos()
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Boire et manger gratuitement"
            choix_2_ecrit = "Demander où est l'aventurier a un villageois"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix= False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    A = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    B = True
    while A:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir bu et manger {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                A = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    A = False
                    choix= True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Partir sans payer"
            choix_2_ecrit = "Payer en partant"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                  choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    AA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    AB = True
    while B:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois avoir eu la reponse, {joueur.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                B = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    choix = True
                    B = False
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Lui donner de l'argent et partir"
            choix_2_ecrit = "L'aider en retour"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    BA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    BB = True
    while AA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois sortit, {joueur.prenom} decide"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Acheter un animal"
            choix_2_ecrit = f"Continuer de boire en cherchant {joueur.cible.genremini}"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    AAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    AAB = True
    while AB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0,0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois sortit {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Essayer de gagner de l'argent en vendant des anciens trésors"
            choix_2_ecrit = "Continuer de voler pour avoir de l'argent"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    ABA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    ABB = True
    while BA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} se balade et:"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Voler le sac de la femme en face"
            choix_2_ecrit = "Voler une sac"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                        choix = False
                        BAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                        choix = False
                        BAB = True
    while BB:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"La dame lui donne 50 euros."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            joueur.argent = joueur.argent + 50
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Partir une fois terminer"
            choix_2_ecrit = "Partir sans payer"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    BBA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    BBA = True
    while ABA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"510 euros de gagner !"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            joueur.argent = joueur.argent + 510
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                ABA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    ABA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Récuperer l'agent pour acheter un animal"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    AABB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    AAA = True
    while AAA:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            ecran.blit(cerbere, (54.2, 93))
            ecran.blit(pheonix, (441.5, 206))
            ecran.blit(dragon, (828.7, 83))
            choix_1_ecrit = "764"
            choix_2_ecrit = "1457"
            choix_3_ecrit = "48985"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (54.2, 421))
            ecran.blit(texte_choix_2, (441.5, 421))
            ecran.blit(texte_choix_3, (828.7, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (114.2, 411))
            ecran.blit(monnaie1, (501.5, 411))
            ecran.blit(monnaie1, (918.7, 411))
            ecran.blit(monnaie1, (60, 439))
            histoire_1 = f"{joueur.prenom} se rend au marchand pour acheter un animal"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAA = False
                    choix = True
    while choix:
         for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            ecran.blit(choix_3, image_choix_3.coordonnees)
            choix_1_ecrit = "Acheter un cerbere"
            choix_2_ecrit = "Acheter un phoenix"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            choix_3_ecrit = "Acheter un dragon"
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_3, image_choix_3.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    AAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    AAAB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_3.carre[0] <= souris[0] <= image_choix_3.carre[1] and image_choix_3.carre[
                                2] <= souris[1] <= image_choix_3.carre[3]:
                    choix = False
                    AAAB = True
    while AAB:
         for evenement in pygame.event.get():
            ecran.blit(bar, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir fini son verre {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            if au_revoir_jeu(evenement) == True:
                AAB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = "Demander à d'autre villageois"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    AABA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                         2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    AABB = True
    while AABA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures sans aucune trace de {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Continuer de chercher"
            choix_2_ecrit = f"Abandonner"
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
                    AABAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Pourquoi abandonner aussi tôt ?"
    while ABB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Recupère l'agent voler et décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                ABB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    ABB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir chercher {joueur.cible.genremini}"
            choix_2_ecrit = "Rester dans sa ville"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                 choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    ABBA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    ABBB = True
    while BAA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Il saisit l'argent et :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                 BAA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Garder l'argent pour acheter un animal"
            choix_2_ecrit = "L'utiliser directement pour d'autres armes"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                  choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                  if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                        choix = False
                        BAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                  if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                         choix = False
                         BAAB = True
    while BBA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après être sortit"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                 BBA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Payer"
            choix_2_ecrit = "Partir sans payer"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                     choix = False
                     BBB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                      choix = False
                      BBB = True
    while BBB:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                 BBB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Utiliser l'argent pour un animal"
            choix_2_ecrit = "Utiliser l'argent pour une arme"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                     choix = False
                     BAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                      choix = False
                      BBAB = True
    while BBAB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            x = 1114 / 3
            ecran.blit(epee, (x, 121))
            ecran.blit(arc, (x*2 + 77 , 310))
            choix_1_ecrit = "1457"
            choix_2_ecrit = "169"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (x, 421))
            ecran.blit(texte_choix_2, (x*2 + 77, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (x+ 60, 411))
            ecran.blit(monnaie1, (x*2 + 137, 411))
            ecran.blit(monnaie1, (60, 439))
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} arrive chez le marchand"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Voler un pistolet"
            choix_2_ecrit = f"Acheter un arc"
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
                    BAB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BBABB = True
                    joueur.argent = joueur.argent - 169
    while BAB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois voler, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir chercher {joueur.cible.genremini}"
            choix_2_ecrit = "Voler le reste des armes"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    BABA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Perdu ! C'est pas ta mission première !"
    while AAAA:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Acheter"
            choix_2_ecrit = "Non, merci"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    joueur.argent = joueur.argent - 764
                    AAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    AAAAB = True
    while AAAAA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            ecran.blit(cerbere, (perso_deux_2[0], 149))
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois être sorti du marchand {joueur.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAAAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            ecran.blit(cerbere, (perso_deux_2[0], 149))
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = "Rester en ville"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[
                    1] <= \
                        image_choix_1.carre[3]:
                    choix = False
                    AAAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[
                    1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    AAAAAB= True
    while AAAAB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois être sorti du marchand {joueur.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAAAAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAAAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = "Acheter un pistolet"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[
                    1] <= \
                        image_choix_1.carre[3]:
                    choix = False
                    AAAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[
                    1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Vous avez perdu. Vous avez utilisé plus que votre argent"
    while AAAB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAAB = False
                    choix = True
    while choix:
         for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Acheter"
            choix_2_ecrit = "Rester raisonnable"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Vous avez perdu. Vous avez utilisé plus que votre argent"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                    2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    AAABB = True
    while AAABB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAABB= False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAABB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Demander à un villageois"
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
                    AAAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    AABB = True
    while AABB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Suite à la réponse de la villageoise, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    choix= True
                    AABB = False
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Partir après plusieurs informations "
            choix_2_ecrit = "Continuer de demander "
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    AABBB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    AABBB = True
    while ABBA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Au bout de quelques heures aucune trace de {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                ABBA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    choix = True
                    ABBA = False
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Continuer de chercher "
            choix_2_ecrit = "Abandonner"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    ABBAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu as perdu ! Faut être plus courageux"
    while ABBB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois être resté dans la ville {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                ABBB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    ABBB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir chercher {joueur.cible.genremini}"
            choix_2_ecrit = "Boire"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    ABBBA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = f"{joueur.ennemi.genremasc} t'a attrapé. Il s'agirait d'arrêter de boire"
    while BAAA:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(griffon, (124.5, 75))
            ecran.blit(requinlutin, (470.5, 155))
            ecran.blit(chupacabra, (926.5, 308))
            choix_1_ecrit = "124356897"
            choix_2_ecrit = "6354"
            choix_3_ecrit = "32"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (124.5, 421))
            ecran.blit(texte_choix_2, (470.5, 421))
            ecran.blit(texte_choix_3, (926.5, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (234.5, 411))
            ecran.blit(monnaie1, (530.5, 411))
            ecran.blit(monnaie1, (986.5, 411))
            ecran.blit(monnaie1, (60, 439))
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} se rend à la boutique du marchand"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAAA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAAA = False
                    choix= True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            ecran.blit(choix_3, image_choix_3.coordonnees)
            choix_1_ecrit = "Acheter un Griffon "
            choix_2_ecrit = "Acheter un requin lutin"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            choix_3_ecrit = "Acheter un chupacabra"
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_3, image_choix_3.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                        2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    BAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                        2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    BAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_3.carre[0] <= souris[0] <= image_choix_3.carre[1] and image_choix_3.carre[
                    2] <= souris[1] <= image_choix_3.carre[3]:
                    choix = False
                    BAAAB = True
    while BAAB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} se rend à la boutique du marchand"
            ecran.blit(pistolet, (370, 328))
            ecran.blit(hache, (826, 278))
            choix_1_ecrit = "4"
            choix_2_ecrit = "98"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (370, 421))
            ecran.blit(texte_choix_2, (826, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (430, 411))
            ecran.blit(monnaie1, (886 , 411))
            ecran.blit(monnaie1, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAAB= False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAAB= False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Acheter un pistolet "
            choix_2_ecrit = "Acheter une hache "
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[
                    1] <= \
                        image_choix_1.carre[3]:
                    choix = False
                    BAABA = True
                    joueur.argent = joueur.argent - 4
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[
                    1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BAABB = True
                    joueur.argent = joueur.argent - 98
    while AAAAAB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            ecran.blit(cerbere, (perso_deux_2[0], 149))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après s'être balader"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAAAAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAAAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            ecran.blit(cerbere, (perso_deux_2[0], 149))
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Rester"
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
                    AAAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Ton objectif c'est pas de faire des petites balades"
    while AABAA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une arme"
            choix_2_ecrit = f"Acheter un animal"
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
                    AABAAB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    AABAAA = True
    while AABBB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois avoir eu sa réponse, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABBB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABBB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir chercher l'aventurier"
            choix_2_ecrit = f"Demander pour éviter de l'affronter"
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
                    AABBBA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'as pas seulement perdu la partie mais aussi ta dignité."
    while AABBBA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Au bout de quelques heures, aucune trace de {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABBBA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABBBA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Continuer à chercher"
            choix_2_ecrit = f"Abandonner"
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
                    ABBAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Va falloir être plus courageux dans la vie"
    while ABBAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois dans la forêt devant {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                ABBAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    ABBAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une arme"
            choix_2_ecrit = f"Partir sans rien"
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
                    AABAAB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    ABBBAA = True
    while ABBBA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures aucune trace de {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                ABBBA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    ABBBA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Continuer de chercher"
            choix_2_ecrit = f"Abandonner"
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
                    ABBBAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu perdu ! Faut être courageux !"
    while BAAAA:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAAAA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Être raisonnable"
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
                    perdu = True
                    texte_fin = "Perdu ! Fallait être raisonnable"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BAAABA = True
    while BAAAB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAAAB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("Faut faire un choix")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas payer"
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
                    BAAABA = True
                    joueur.argent = joueur.argent - 32
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Perdu ! Tu es vraiment un radin"
    while BAABA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois sortit de la boutique {joueur.prenom}:"
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Rester ici afin de voler toutes les armes"
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
                    BAABAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A force de voler, tu en as oublier ton objectif principal"
    while BAABB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois sortit de la boutique {joueur.prenom}:"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Rester ici afin de voler toutes les armes"
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
                    BAABBA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça te sert de voler tout ça ?"
    while BABA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures sans aucune trace de {joueur.cible.genremini}:"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BABA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BABA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Continuer de chercher"
            choix_2_ecrit = f"Abandonner"
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
                    BABAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Perdu ! Fallait continuer"
    while BBABB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois sortie, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Voler le reste des armes"
            choix_2_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
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
                    BBABBB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BBABBA = True
    while BABAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois arrivée dans la forêt, {joueur.cible.genremini} apparait devant toi"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BABAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BABAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ton arme"
            choix_2_ecrit = f"Combattre a main nue"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[1] <= \
                        image_choix_1.carre[3]:
                    choix = False
                    gagner = True
                    texte_fin = "Bravo ! Heureusement que tu ne t'es pas battu à main nue"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu t'es cru pour The Rock ou quoi ?"
    while AAAAAB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après s'être balader {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAAAAB = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAAAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Rester"
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
                    AAAAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu comptes te balader toute ta vie ?"
    while AAAAAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Au bout de quelques heures toujours aucune trace de  {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAAAAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAAAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Continuer de chercher"
            choix_2_ecrit = "Abandonner"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[
                    1] <= \
                        image_choix_1.carre[3]:
                    choix = False
                    AAAAAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[
                    1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu as perdu ! Sois plus courageux"
    while AABAAAB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABAAAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABAAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas acheter"
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
                    perdu = True
                    texte_fin = "Tu n'as pas l'argent illimité non plus."
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    AABAAB = True
    while AABAAB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            ecran.blit(epee, (379, 121))
            ecran.blit(pistolet, (465, 328))
            choix_1_ecrit = "145"
            choix_2_ecrit = "4"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (379, 421))
            ecran.blit(texte_choix_2, (465, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (439, 411))
            ecran.blit(monnaie1, (525 , 411))
            ecran.blit(monnaie1, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABAAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une épée"
            choix_2_ecrit = f"Acheter un pistolet"
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
                    AABAABA = True
                    joueur.argent = joueur.argent - 145
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    AABAABA = True
                    joueur.argent = joueur.argent - 4
    while AABAAA:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            x = 806/3
            ecran.blit(chat, (x, 236))
            ecran.blit(dragon, (x+131, 83))
            choix_1_ecrit = "64"
            choix_2_ecrit = "6894"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (x, 421))
            ecran.blit(texte_choix_2, (x+131, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (x+60, 411))
            ecran.blit(monnaie1, (x+191, 411))
            ecran.blit(monnaie1, (60, 439))
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABAAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter un chat noir"
            choix_2_ecrit = f"Acheter un dragon"
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
                    AABAAAA = True
                    joueur.argent = joueur.argent - 64
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
    while ABBBAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Tu te retrouves face à face avec {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                ABBBAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    ABBBAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser sa force"
            choix_2_ecrit = f"Partir en courant"
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
                    perdu = True
                    texte_fin = "Tu as perdu ! Tu n'as pas assez de force malheureusement."
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu as perdu ! Tu es vraiment qu'un lâche !"
    while BAAABA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois sortit de la boutique {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAAABA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAAABA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Rester en ville"
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
                    BAAABAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = f"Perdu ! Tu dois retrouver {joueur.cible.genremini}"
    while BAABAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après quelques heures sans aucune trace de {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Continuer à chercher"
            choix_2_ecrit = f"Abandonner"
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
                    BAABAAA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Bah alors, comme ça on abandonne."
    while BAABBA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures sans aucunes trace de {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABBA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABBA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Abandonner"
            choix_2_ecrit = f"Continuer"
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
                    perdu = True
                    texte_fin = "Tout ça pour ça..."
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BAABBAA = True
    while BBABBB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABBB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABBB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(marchand_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir chercher l'aventurier"
            choix_2_ecrit = f"Continuer de voler en magasin"
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
                    BBABBA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A force de voler, tu risques de te brûler les ailes"
    while BBABBA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures sans aucunes trace de {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABBA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABBA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Abandonner"
            choix_2_ecrit = f"Continuer"
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
                    perdu = True
                    texte_fin = "Tout ça pour ça..."
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BBABBAA = True
    while AAAAAAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_trois_1)
            ecran.blit(cerbere, (perso_seul[0], 149))
            ecran.blit(perso3, perso_trois_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} rentre dans le forêt et {joueur.cible.prenom} arrive face à {joueur.prenom}."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AAAAAAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AAAAAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_trois_1)
            ecran.blit(cerbere, (perso_seul[0], 149))
            ecran.blit(perso3, perso_trois_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ton cerbère"
            choix_2_ecrit = f"Te battre à main nu"
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
                    gagner = True
                    texte_fin = "Tu as gagné mais tu es pauvre"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu as perdu, arrête de faire ton grand"
    while AABAABA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_deux_1)
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} rentre dans le forêt et {joueur.cible.prenom} arrive faca à {joueur.prenom}."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABAABA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABAABA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_deux_1)
            ecran.blit(perso3, perso_deux_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Se battre à main nu"
            choix_2_ecrit = f"Utiliser l'arme achetée contre lui"
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
                    perdu = True
                    texte_fin = "Pourquoi faire ?"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    gegner = True
                    texte_fin = "Bravo ! Tu as réussi à faire les bon choix"
    while AABAAAA:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABAAAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABAAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Ne pas acheter"
            choix_2_ecrit = f"Acheter"
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
                    perdu = True
                    texte_fin = "Sérieusement ? Tu devrais tenter le concours des rats"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    AABAAAAB = True
    while AABAAAAB:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_trois_1)
            ecran.blit(chat, (perso_seul[0], 292))
            ecran.blit(perso3, perso_trois_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} rentre dans le forêt et {joueur.cible.prenom} arrive faca à {joueur.prenom}."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                AABAAAAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    AABAAAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_trois_1)
            ecran.blit(chat, (perso_seul[0], 292))
            ecran.blit(perso3, perso_trois_2)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser le chat contre lui"
            choix_2_ecrit = f"Le battre à main nu"
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
                    gagner = True
                    texte_fin = "Bravo, tu ne t'es pas méfié des apparences"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Qu'est-ce que tu cherches à prouver"
    while BBABBAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_deux_1)
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} rentre dans le forêt et {joueur.cible.prenom} arrive faca à {joueur.prenom}."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABBAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABBAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_deux_1)
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ton arme"
            choix_2_ecrit = f"Utiliser un animal"
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
                    perdu = True
                    texte_fin = "Un arc sérieux ? En plus tu sais pas viser"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BBABBAAA = True
    while BBABBAAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Mais tu n'as d'animal"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABBAAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABBAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter un animal rapidement"
            choix_2_ecrit = f"Ne pas acheter et combattre {joueur.cible.prenom} à main nue"
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
                    BBABBAAB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'es pas John Cena, évite d'utiliser ta force"
    while BBABBAAB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            x = 833 / 3
            ecran.blit(chauvesouris, (x, 196))
            ecran.blit(chat, (x + 336, 236))
            choix_1_ecrit = "6894"
            choix_2_ecrit = "64"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (x , 421))
            ecran.blit(texte_choix_2, (x + 336, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (x + 60, 411))
            ecran.blit(monnaie1, (x + 396, 411))
            ecran.blit(monnaie1, (60, 439))
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABBAAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABBAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une chauve-souris"
            choix_2_ecrit = f"Acheter un chat noir"
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
                    BBABBAABA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BBABBAABB = True
    while BBABBAABA:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABBAABA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABBAABA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Rester raisonnable"
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
                    perdu = True
                    texte_fin = "Une chauve-souris sérieusement"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'as vraiment pas la notion de l'argent toi"
    while BBABBAABB:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois choisi {joueur.prenom} décide de "
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABBAABB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABBAABB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas le prendre"
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
                    BBABBAABBA = True
                    joueur.argent = joueur.argent - 64
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'aimes pas les chats ?"
    while BBABBAABBA:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_trois_1)
            ecran.blit(chat, (perso_seul[0], 292))
            ecran.blit(perso3, perso_trois_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En sortant de la boutique {joueur.prenom}, croise {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BBABBAABBA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BBABBAABBA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_trois_1)
            ecran.blit(chat, (perso_seul[0], 292))
            ecran.blit(perso3, perso_trois_2)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Le laisser partir"
            choix_2_ecrit = f"Utiliser ton chat"
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
                    perdu = True
                    texte_fin = "Roh la la, tu as perdu des heures et des heures pour ça."
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    gagner = True
                    texte_fin = "Bravoooo! tu ne t'es pas fié aux apparences"
    while BAAABAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après quelques temps de recherche, toujours aucune trace de {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAAABAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAAABAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Abandonner"
            choix_2_ecrit = f"Continuer de chercher"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[1] <= \
                        image_choix_1.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Perdu ! Aucun courage"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BAAABAB = True
    while BAAABAB:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_trois_1)
            ecran.blit(chupacabra, (perso_seul[0], 364))
            ecran.blit(perso3, perso_trois_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après être entrée dans la forêt, {joueur.prenom} apperçoit {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAAABAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAAABAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            perso3 = aventurier_normal
            ecran.blit(perso2, perso_trois_1)
            ecran.blit(chupacabra, (perso_seul[0], 364))
            ecran.blit(perso3, perso_trois_2)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ton chupacabra"
            choix_2_ecrit = f"Utiliser tes poings"
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
                    gagner = True
                    texte_fin = "Wow ! Bravo à vous deux, super bonne équipe"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Roh la la... Perdu ! Arrêtes de vouloir monter ta force !"
    while BAABAAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après quelques heures aucune traces de {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABAAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABAAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Abandonner"
            choix_2_ecrit = f"Continuer de chercher"
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
                    perdu = True
                    texte_fin = "Perdu ! Aucun courage"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    BAABAAB = True
    while BAABAAB:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois arriver dans la forêt, {joueur.prenom} apperçoit {joueur.cible.genremini} au loin."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABAAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABAAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser tes poings"
            choix_2_ecrit = f"Utiliser ton arme"
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
                    perdu = True
                    texte_fin = "Perdu ! Arrête de vouloir prouver !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    gagner = True
                    texte_fin = "Gagner ! Bravo ! Au moins tu es un bandit cool !"
    while BAABBAA:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois dans la forêt. {joueur.cible.genremasc} apparait. {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABBAA = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABBAA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser l'arme"
            choix_2_ecrit = f"Utiliser ses poings"
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
                    BAABBAB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Stop ! Tu n'es pas là pour faire le concours de qui a le plus de force"
    while BAABBAB:
        for evenement in pygame.event.get():
            ecran.blit(foret1, (0, 0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"L'arme ne suffit pas. {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABBAB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABBAB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            ecran.blit(foret1, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une autre arme"
            choix_2_ecrit = f"Se battre à main nu"
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
                    BAABBABA = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Perdu ! C'est pas très malin !"
    while BAABBABA:
        for evenement in pygame.event.get():
            ecran.blit(marchand_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABBABA = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABBABA = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("BANDIT")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter un pistolet"
            choix_2_ecrit = f"Acheter un arc"
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
                    BAABBABB = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Un arc sérieux ? Tu t'es pris pour Robin des bois ?"
    while BAABBABB:
        for evenement in pygame.event.get():
            ecran.blit(ville_bandit, (0, 0))
            pygame.display.set_caption("BANDIT")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} recroise {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                BAABBABB = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    BAABBABB = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("Faut faire un choix")
            ecran.blit(ville_bandit, (0, 0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser le pistolet"
            choix_2_ecrit = f"Le battre à main nu"
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
                    gagner = True
                    texte_fin = "Félicitation ! Au moins tu ne fais pas des choix débiles !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Perdu ! C'est pas un concours de force"





# Partie de l'aventurier
    while aventurier:
        for evenement in pygame.event.get():
            ecran.blit(demarrer_image, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso1 = bandit_normal
            perso2 = joueurnormal
            perso3 = sorcier_normal
            ecran.blit(perso1, perso_trois_1)
            ecran.blit(perso2, perso_seul)
            ecran.blit(perso3, perso_trois_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Pendant ce temps, {joueur.prenom} était en train de tout mettre en œuvre pour"
            histoire_2 = f"retrouver {joueur.cible.prenom}, {joueur.cible.genremini} qui avait dérobé des"
            histoire_3 = f"armes magiques lors de ses méfaits passés. Ces armes étaient essentielles pour"
            histoire_4 = f"{joueur.genremini}, car elles contenaient des indices précieux sur la localisation"
            histoire_5 = f"du grimoire interdit. {joueur.genremasc} avait sombré dans les ténèbres pour"
            histoire_6 = f"obtenir un pouvoir magique incommensurable, et il ne reculerait devant rien"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()

            if au_revoir_jeu(evenement) == True:
                aventurier = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    aventurier = False
                    suite = True
    while suite:
        for evenement in pygame.event.get():
            ecran.blit(demarrer_image, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso1 = bandit_normal
            perso2 = joueurnormal
            perso3 = sorcier_normal
            ecran.blit(perso1, perso_trois_1)
            ecran.blit(perso2, perso_seul)
            ecran.blit(perso3, perso_trois_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"pour retrouver {joueur.cible.prenom} et les armes magiques. Ainsi, dans ce monde"
            histoire_2 = f"fantastique, les destins de {joueur.prenom}, de {joueur.ennemi.genremini} {joueur.ennemi.prenom}"
            histoire_3 = f"et du {joueur.cible.genremini} {joueur.cible.prenom} étaient étroitement liés par un enchevêtrement d'ambitions,"
            histoire_4 = f"de trésors et de quêtes pour des objets magiques d'une importance cruciale."
            histoire_5 = f"Les prochains chapitres de leur histoire promettaient des aventures épiques,"
            histoire_6 = f"des confrontations magiques et des choix moraux déchirants."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                suite = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    suite = False
                    suite_2 = True
    while suite_2:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.genremasc} arrive dans la ville {joueur.nom_de_ville}, sa ville natale et préférée"
            histoire_2 = f"{joueur.prenom} se balade afin de trouver le bar le plus célèbre à cotoyer."
            histoire_3 = f"Après quelques temps de marche, il entre dans le bar en regardant autour"
            histoire_4 = f"de lui."
            histoire_5 = f""
            histoire_6 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                suite_2 = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    suite_2 = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Le laisser partir"
            choix_2_ecrit = "Combattre l'autre aventurier"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    C = True
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    D = True
    while C:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Suite à cette décision {joueur.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                C = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    C = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Demander où se trouve sa boussole"
            choix_2_ecrit = f"Aller s'en racheter une"
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
                    CC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CD = True
    while CC:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après ça, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Prendre l'information de où est {joueur.cible.genremini}"
            choix_2_ecrit = f"Prendre l'information de où est sa carte"
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
                    CCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CCD = True
    while CD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            ecran.blit(boussole, (595, 295))
            choix_1_ecrit = "645"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (595, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (430, 411))
            ecran.blit(monnaie1, (60, 439))
            histoire_1 = f"Après s'être rendu dans la boutique du marchand {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une boussole"
            choix_2_ecrit = f"Ne pas acheter"
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
                    CDC = True
                    joueur.argent = joueur.argent - 645
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CDD = True
    while CCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à sa recherche"
            choix_2_ecrit = f"Acheter une carte"
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
                    CCCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CCCD = True
    while CCD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à ça recherche"
            choix_2_ecrit = f"laisser tomber"
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
                    CCDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Ah ouais... Dès le début tu abandonnes"
    while CDC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois avoir eu sa réponse, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Demander si le marchand à vu {joueur.cible.genremini}"
            choix_2_ecrit = f"Se débrouiller seul"
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
                    EFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFEF = True
    while CDD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} reste afin de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une arme"
            choix_2_ecrit = f"Partir"
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
                    CDDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CDDD = True
    while CCCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois arriver dans sa ville, {joueur.prenom} apperçoit {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CCCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CCCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une arme"
            choix_2_ecrit = f"Le combattre avec ses poings"
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
                    CCCCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin ="Malheureusement tu n'est pas assez fort"
    while CCCD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En sortant du magasin, {joueur.prenom} tombe sur {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CCCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CCCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser sa carte"
            choix_2_ecrit = f"Utiliser sa force"
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
                    gagner = True
                    texte_fin = "Etonnament tu as réussi à étouffer ton adversaire avec la carte"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça sert d'avoir acheter une carte si ce n'est pas pour l'utiliser"
    while CCDC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CCDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CCDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une arme"
            choix_2_ecrit = f"Ne rien acheter"
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
                    CCDCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "C'était gratuit en plus"
    while CDCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois avoir eu sa réponse, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Part après avoir eu sa réponse"
            choix_2_ecrit = f"Rester en ville"
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
                    CDCD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CDCCD = True
    while CDDC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Choisi ton arme !"
            ecran.blit(arc, (184.6, 230))
            ecran.blit(epee, (478.2, 121))
            ecran.blit(hache, (739.8, 278))
            ecran.blit(pistolet, (979.4, 328))
            choix_1_ecrit = "4"
            choix_2_ecrit = "4"
            choix_3_ecrit = "4"
            choix_4_ecrit = "4"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_5 = font.render(choix_4_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (184.6, 421))
            ecran.blit(texte_choix_2, (478.2, 421))
            ecran.blit(texte_choix_3, (739.8, 421))
            ecran.blit(texte_choix_5, (979.4, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (244.6, 411))
            ecran.blit(monnaie1, (538.2, 411))
            ecran.blit(monnaie1, (799.8, 411))
            ecran.blit(monnaie1, (1039.4, 411))
            ecran.blit(monnaie1, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()

            ecran.blit(choix_1, image_choix_1_4.coordonnees)
            ecran.blit(choix_2, image_choix_2_4.coordonnees)
            ecran.blit(choix_3, image_choix_3_4.coordonnees)
            ecran.blit(choix_4, image_choix_4.coordonnees)
            choix_1_ecrit = f"Acheter un arc"
            choix_2_ecrit = f"Acheter une épée"
            choix_3_ecrit = f"Acheter hache"
            choix_4_ecrit = f"Acheter un pistolet"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(choix_4_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1_4.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2_4.coordonnees)
            ecran.blit(texte_choix_3, image_choix_3_4.coordonnees)
            ecran.blit(texte_choix_4, image_choix_4.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[1] <= \
                        image_choix_1.carre[3]:
                    choix = False
                    CDDCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CDDCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_3.carre[0] <= souris[0] <= image_choix_3.carre[1] and image_choix_3.carre[2] <= souris[1] <= \
                        image_choix_3.carre[3]:
                    choix = False
                    CDDCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_4.carre[0] <= souris[0] <= image_choix_4.carre[1] and image_choix_4.carre[2] <= souris[1] <= \
                        image_choix_4.carre[3]:
                    choix = False
                    CDDCC = True
    while CDDD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois sortie de la boutique {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester dans la ville"
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
                    CDDDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CDDDD = True
    while CDDCC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Rester raisonnable"
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
                    CDCD = True
                    joueur.agrent = joueur.argent - 4
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Mais il y avait des réductions"
    while CCCCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En sortant du magasin {joueur.prenom} croise {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CCCCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CCCCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser l'arme'"
            choix_2_ecrit = f"Ne pas l'utiliser"
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
                    gagner = True
                    texte_fin = "Bravo tu as gagné !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça sert d'avoir acheter une arme si ce n'est pas pour l'utiliser"
    while CCDCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En sortant du magasin {joueur.prenom} croise {joueur.cible.penom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CCDCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CCDCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser l'arme'"
            choix_2_ecrit = f"Ne pas l'utiliser"
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
                    gagner = True
                    texte_fin = "Bravo tu as gagné !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça sert d'avoir acheter une arme si ce n'est pas pour l'utiliser"
    while CDCD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Rester en ville"
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
                    CDCDD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'es pas venu pour te balader"
    while CDDCD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas acheter"
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
                    CDDCDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Mais l'arme ne coutait pas cher, il y avait une réduction"
    while CDDDC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures de recherches {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une arme"
            choix_2_ecrit = f"Lancer sa boussole"
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
                    CDDDCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Pourquoi faire ?"
    while CDDDD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Acheter une carte"
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
                    CDDDDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    CDDDDD = True
    while CDDCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de "
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    CDCDD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Ton but n'est pas de faire du tourisme"
    while CDCDD:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois face à {joueur.cible.prenom}, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDCDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDCDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une boussole"
            choix_2_ecrit = f"Le combattre avec les poings"
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
                    CDCCDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Quelle erreur de débutant !"
    while CDCCD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            ecran.blit(boussole, (595, 295))
            choix_1_ecrit = "645"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (595, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (430, 411))
            ecran.blit(monnaie1, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDCCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDCCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter la boussole"
            choix_2_ecrit = f"Ne rien acheter"
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
                    CDCCDC = True
                    joueur.argent = joueur.argent - 645
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu comptes te battre les mains vide ?"
    while CDCCDC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois devant {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDCCDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDCCDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Lui lancer la boussole"
            choix_2_ecrit = f"Ne pas l'utiliser"
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
                    gagner = True
                    texte_fin = "Etonnamment ça a marché..."
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça sert d'acheter un balai pour ne pas l'utiliser"
    while CDDCDC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois devant {joueur.cible.prenom}, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDCDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDCDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser son arme"
            choix_2_ecrit = f"Ne rien faire"
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
                    gagner = True
                    texte_fin = "Bravooo !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu t'es découragé ?"
    while CDDDDD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir acheter une carte {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDDDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDDDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    CDDDDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Ton but n'est pas de devenir un touriste"
    while CDDDDC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDDDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDDDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une arme"
            choix_2_ecrit = f"Utiliser sa carte"
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
                    CDDDCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Sérieusement, une carte ?"
    while CDDDCC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} se retrouve devant {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                CDDDCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    CDDDCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ce que {joueur.prenom} a acheté contre ton {joueur.cible.prenom}"
            choix_2_ecrit = f"Ne rien faire"
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
                    gagner = True
                    texte_fin = "Bravo ! Tu as gagné !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Pourquoi ne rien faire ?"
    while D:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après l'avoir combattu, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                D = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    D = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Prendre l'argent"
            choix_2_ecrit = f"Refuser l'argent"
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
                    DC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= \
                souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    DD = True
    while DC:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois l'argent pris {joueur.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser l'argent pour acheter une arme"
            choix_2_ecrit = f"Ne pas l'utiliser"
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
                    DCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DDC = True
    while DCC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            ecran.blit(arc, (184.6, 230))
            ecran.blit(epee, (478.2, 121))
            ecran.blit(hache, (739.8, 278))
            ecran.blit(pistolet, (979.4, 328))
            choix_1_ecrit = "4"
            choix_2_ecrit = "4"
            choix_3_ecrit = "4"
            choix_4_ecrit = "4"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_5 = font.render(choix_4_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (184.6, 421))
            ecran.blit(texte_choix_2, (478.2, 421))
            ecran.blit(texte_choix_3, (739.8, 421))
            ecran.blit(texte_choix_5, (979.4, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (244.6, 411))
            ecran.blit(monnaie1, (538.2, 411))
            ecran.blit(monnaie1, (799.8, 411))
            ecran.blit(monnaie1, (1039.4, 411))
            ecran.blit(monnaie1, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1_4.coordonnees)
            ecran.blit(choix_2, image_choix_2_4.coordonnees)
            ecran.blit(choix_3, image_choix_3_4.coordonnees)
            ecran.blit(choix_4, image_choix_4.coordonnees)
            choix_1_ecrit = f"Acheter un arc"
            choix_2_ecrit = f"Acheter une épée"
            choix_3_ecrit = f"Acheter une hache"
            choix_4_ecrit = f"Acheter un pistolet"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(choix_4_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1_4.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2_4.coordonnees)
            ecran.blit(texte_choix_3, image_choix_3_4.coordonnees)
            ecran.blit(texte_choix_4, image_choix_4.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1_4.carre[0] <= souris[0] <= image_choix_1_4.carre[1] and image_choix_1_4.carre[2] <= souris[1] <= \
                        image_choix_1_4.carre[3]:
                    choix = False
                    DCCC = True
                    joueur.argent = joueur.argent -4
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2_4.carre[0] <= souris[0] <= image_choix_2_4.carre[1] and image_choix_2_4.carre[2] <= souris[1] <= \
                        image_choix_2_4.carre[3]:
                    choix = False
                    DCCC = True
                    joueur.argent = joueur.argent -4
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_3_4.carre[0] <= souris[0] <= image_choix_3_4.carre[1] and image_choix_3_4.carre[2] <= souris[1] <= \
                        image_choix_3_4.carre[3]:
                    choix = False
                    DCCC = True
                    joueur.argent = joueur.argent -4
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_4.carre[0] <= souris[0] <= image_choix_4.carre[1] and image_choix_4.carre[2] <= souris[1] <= \
                        image_choix_4.carre[3]:
                    choix = False
                    DCCC = True
                    joueur.argent = joueur.argent -4
    while DCCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après être sorti du marchand, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une carte"
            choix_2_ecrit = f"Ne pas acheter"
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
                    DCCDD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DCCDC = True
    while DCCDD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCCDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCCDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Rester en ville"
            choix_2_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
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
                    perdu = True
                    texte_fin = "Ce n'est pas le moment se balader"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DCCDDC = True
    while DCCDDC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} cherche {joueur.cible.prenom} et tombe par hasard sur lui dans la forêt."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCCDDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCCDDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ton arme"
            choix_2_ecrit = f"Le frapper avec ton sac à dos"
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
                    gagner = True
                    texte_fin = "Bravoooo ! Tu as gagné"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "No comments..."
    while DCCDC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir acheter sa carte {joueur.prenom} décide"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCCDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCCDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Rester en ville"
            choix_2_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
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
                    DCCDCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DCCDCD = True
    while DCCDCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de rester en ville"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCCDCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCCDCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir acheter une arme"
            choix_2_ecrit = f"Ne rien faire"
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
                    DCCDCCD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu es un peu flemmard je trouve"
    while DCCDCCD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois à la boutique du marchand {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCCDCCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCCDCCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas acheter"
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
                    DCCDCCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Oh la la, fait un petit effort pour le Black Friday."
    while DCCDCCC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} croise le chemin de {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCCDCCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCCDCCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser sa carte et son arme"
            choix_2_ecrit = f"Fuir le combat"
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
                    gagner = True
                    texte_fin = "Wow ! Bravo !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "BOUH ! T'ES NUL !"
    while DCCDCD:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} part à la recherche de {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCCDCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCCDCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Fuir"
            choix_2_ecrit = f"Utiliser son arme"
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
                    perdu = True
                    texte_fin = "La solution n'est pas la fuite"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    gagner = True
                    texte_fin = "Bravo ! Tu as gagné !"
    while DCD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Suite à cette description {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    DCDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DCDD = True
    while DCDC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures sans aucune trace de {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Chercher à {joueur.nom_de_ville}"
            choix_2_ecrit = f"Continuer de chercher dans la forêt"
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
                    DCDCC= True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DCDCD = True
    while DCDCC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En cherchant dans sa ville {joueur.prenom} croise {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir acheter une arme"
            choix_2_ecrit = f"Fouiller son sac à dos"
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
                    DCDCCD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu as mis trop de temp, ton ennemi à eut le temps de fuir"
    while DCDCD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En cherchant dans la ville {joueur.prenom} croise {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCDCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCDCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir acheter une arme"
            choix_2_ecrit = f"Utiliser ses poings"
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
                    DCDCCD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "C'est triste mais il va falloir plus que ça pour battre ton ennemi"
    while DCDCCD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois chez le marchand, {joueur.prenom} décide de :"
            ecran.blit(epee, (611.5, 121))
            choix_1_ecrit = "145"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (611.5, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (671.5, 411))
            ecran.blit(monnaie1, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCDCCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCDCCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter l'arme'"
            choix_2_ecrit = f"Ne pas l'acheter"
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
                    DCDCCC = True
                    joueur.argent = joueur.argent - 145
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Reprends toi en main, ou tu ne réussiras rien dans la vie"
    while DCDCCC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.cible.prenom} entre dans la boutique lui aussi"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCDCCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCDCCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Le combattre avec l'arme"
            choix_2_ecrit = f"Se cacher"
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
                    gagner = True
                    texte_fin = "You're a winner !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'as plus 4 ans, faut arrêter de jouer à cache-cache"
    while DD:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après ça {joueur.prenom} part :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Se promener dans {joueur.nom_de_ville}"
            choix_2_ecrit = f"Acheter une arme"
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
                    DDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DDD = True
    while DCDD:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En se promenant en ville {joueur.prenom} tombe sur l'autre aventurier"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = aventurier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Demander où se trouve {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    DCDDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "La ville est peut-être jolie, mais bon faut pas oublier ton objectif"
    while DCDDC:
        for evenement in pygame.event.get():
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir eu sa réponse, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCDDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCDDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(ville_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Acheter une boussole"
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
                    DCDCDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DDCC = True
    while DCDCDC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois dans la forêt {joueur.prenom} tombe sur {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCDCDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCDCDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Lui faire une démonstration de force"
            choix_2_ecrit = f"Lui lancer son sac à dos"
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
                    perdu = True
                    texte_fin = "Tu n'es pas bodybuilder"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Euh... Bon... Aucun jugement..."
    while DDC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une boussole"
            choix_2_ecrit = f"Acheter une arme"
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
                    DDCC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    DDD = True
    while DDCC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Un fois chez le marchand {joueur.prenom} décide de"
            ecran.blit(boussole, (595, 295))
            choix_1_ecrit = "645"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (595, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (430, 411))
            ecran.blit(monnaie1, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DDCC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DDCC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas acheter"
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
                    DCDCDCD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Comment veux tu battre ton ennemi maintenant ?"
    while DCDCDCD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir acheter un balai"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DCDCDCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DCDCDCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    DDCDD = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Je ne jugerai pas ton choix..."
    while DDCDD:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois dan la forêt {joueur.prenom} rencontre {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DDCDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DDCDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Lui lancer ta boussole"
            choix_2_ecrit = f"Fuir"
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
                    perdu = True
                    texte_fin = "Tu croyais vraiment survivre qu'avec une boussole ?"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu es un peureux !"
    while DDD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            ecran.blit(arc, (184.6, 230))
            ecran.blit(epee, (478.2, 121))
            ecran.blit(hache, (739.8, 278))
            ecran.blit(pistolet, (979.4, 328))
            choix_1_ecrit = "4"
            choix_2_ecrit = "4"
            choix_3_ecrit = "4"
            choix_4_ecrit = "4"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_5 = font.render(choix_4_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (184.6, 421))
            ecran.blit(texte_choix_2, (478.2, 421))
            ecran.blit(texte_choix_3, (739.8, 421))
            ecran.blit(texte_choix_5, (979.4, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie1, (244.6, 411))
            ecran.blit(monnaie1, (538.2, 411))
            ecran.blit(monnaie1, (799.8, 411))
            ecran.blit(monnaie1, (1039.4, 411))
            ecran.blit(monnaie1, (60, 439))
            histoire_1 = f"{joueur.prenom} se rend dans la boutique du marchand"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DDD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DDD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1_4.coordonnees)
            ecran.blit(choix_2, image_choix_2_4.coordonnees)
            ecran.blit(choix_3, image_choix_3_4.coordonnees)
            ecran.blit(choix_4, image_choix_4.coordonnees)
            choix_1_ecrit = f"Acheter un arc"
            choix_2_ecrit = f"Acheter une épée"
            choix_3_ecrit = f"Acheter une hache"
            choix_4_ecrit = f"Acheter un pistolet"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(choix_4_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1_4.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2_4.coordonnees)
            ecran.blit(texte_choix_3, image_choix_3_4.coordonnees)
            ecran.blit(texte_choix_4, image_choix_4.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1_4.carre[0] <= souris[0] <= image_choix_1_4.carre[1] and image_choix_1_4.carre[2] <= \
                        souris[1] <= \
                        image_choix_1_4.carre[3]:
                    choix = False
                    DDCD = True
                    potion = "l'arc"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2_4.carre[0] <= souris[0] <= image_choix_2_4.carre[1] and image_choix_2_4.carre[2] <= \
                        souris[1] <= \
                        image_choix_2_4.carre[3]:
                    choix = False
                    DDCD = True
                    potion = "l'épée"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_3_4.carre[0] <= souris[0] <= image_choix_3_4.carre[1] and image_choix_3_4.carre[2] <= \
                        souris[1] <= \
                        image_choix_3_4.carre[3]:
                    choix = False
                    DDCD = True
                    potion = "la hache"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_4.carre[0] <= souris[0] <= image_choix_4.carre[1] and image_choix_4.carre[2] <= souris[
                    1] <= \
                        image_choix_4.carre[3]:
                    choix = False
                    DDCD = True
                    potion = "le pistolet"
    while DDCD:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DDCD = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DDCD = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter {potion}"
            choix_2_ecrit = f"Ne pas acheter"
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
                    DDDC = True
                    joueur.argent = joueur.argent - 4
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Les armes n'étaient pas à ton goût?"
    while DDDC:
        for evenement in pygame.event.get():
            ecran.blit(marchand_aventurier, (0,0))
            pygame.display.set_caption("AVENTURIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois avoir choisi {potion}, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DDDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DDDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(marchand_aventurier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    DDDDC = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = f"Et {joueur.cible.prenom} dans tout ça ?"
    while DDDDC:
        for evenement in pygame.event.get():
            ecran.blit(foret2, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois dans la forêt, {joueur.prenom} croise {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                DDDDC = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    DDDDC = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("AVENTURIER")
            ecran.blit(foret2, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ton arme"
            choix_2_ecrit = f"Utiliser ta boussole"
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
                    gagner = True
                    texte_fin = "Bravo ! En utilisant ta potion, tu lui a laissé aucune chance !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Ma question est : pourquoi la boussole ?"





# Partie du sorcier
    while sorcier:
        for evenement in pygame.event.get():
            ecran.blit(demarrer_image, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            perso1 = aventurier_normal
            perso2 = joueurnormal
            perso3 = bandit_normal
            ecran.blit(perso1, perso_trois_1)
            ecran.blit(perso2, perso_seul)
            ecran.blit(perso3, perso_trois_2)
            histoire_1 = f"Pendant ce temps, {joueur.prenom} était en train de tout mettre en œuvre pour"
            histoire_2 = f"retrouver {joueur.cible.prenom}, {joueur.cible.genremini} qui avait dérobé des"
            histoire_3 = f"armes magiques lors de ses méfaits passés. Ces armes étaient essentielles pour"
            histoire_4 = f"{joueur.genremini}, car elles contenaient des indices précieux sur la localisation"
            histoire_5 = f"du grimoire interdit. {joueur.genremasc} avait sombré dans les ténèbres pour"
            histoire_6 = f"obtenir un pouvoir magique incommensurable, et il ne reculerait devant rien"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()

            if au_revoir_jeu(evenement) == True:
                sorcier = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    sorcier = False
                    suite = True
    while suite:
        for evenement in pygame.event.get():
            ecran.blit(demarrer_image, (0,0))
            pygame.display.set_caption("SORCIER")
            perso1 = aventurier_normal
            perso2 = joueurnormal
            perso3 = bandit_normal
            ecran.blit(perso1, perso_trois_1)
            ecran.blit(perso2, perso_seul)
            ecran.blit(perso3, perso_trois_2)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"pour retrouver {joueur.cible.prenom} et les armes magiques. Ainsi, dans ce monde"
            histoire_2 = f"fantastique, les destins de {joueur.prenom}, de {joueur.ennemi.genremini} {joueur.ennemi.prenom}"
            histoire_3 = f"et du {joueur.cible.genremini} {joueur.cible.prenom} étaient étroitement liés par un enchevêtrement d'ambitions,"
            histoire_4 = f"de trésors et de quêtes pour des objets magiques d'une importance cruciale."
            histoire_5 = f"Les prochains chapitres de leur histoire promettaient des aventures épiques,"
            histoire_6 = f"des confrontations magiques et des choix moraux déchirants."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                suite = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    suite = False
                    suite_2 = True
    while suite_2:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.genremasc} arrive dans la ville {joueur.nom_de_ville}, sa ville natale et préférée"
            histoire_2 = f"{joueur.prenom} se balade afin de trouver le bar le plus célèbre à cotoyer."
            histoire_3 = f"Après quelques temps de marche, il entre dans le bar en regardant autour"
            histoire_4 = f"de lui et croise le regard d'un sorcier"
            histoire_5 = f""
            histoire_6 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            texte_truc_2 = font.render(histoire_2, True, (0, 0, 0))
            texte_truc_3 = font.render(histoire_3, True, (0, 0, 0))
            texte_truc_4 = font.render(histoire_4, True, (0, 0, 0))
            texte_truc_5 = font.render(histoire_5, True, (0, 0, 0))
            texte_truc_6 = font.render(histoire_6, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            ecran.blit(texte_truc_2, (0, 505))
            ecran.blit(texte_truc_3, (0, 533))
            ecran.blit(texte_truc_4, (0, 561))
            ecran.blit(texte_truc_5, (0, 589))
            ecran.blit(texte_truc_6, (0, 617))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                suite_2 = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    suite_2 = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            pygame.display.set_caption("SORCIER")
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = "Le laisser partir"
            choix_2_ecrit = "Combattre l'autre sorcier"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix= False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[
                                2] <= souris[1] <= image_choix_1.carre[3]:
                    choix = False
                    E = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[
                                2] <= souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    F = True
    while E:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Suite à cette décision {joueur.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                E = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    E = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Demander où se trouve son balai magique"
            choix_2_ecrit = f"Aller s'en racheter un"
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
                    EE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EF = True
    while EE:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après ça, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Prendre l'information de où est {joueur.cible.genremini}"
            choix_2_ecrit = f"Prendre l'information de où est sa baguette"
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
                    EEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EEF = True
    while EF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après s'être rendu dans la boutique du marchand {joueur.prenom} décide de"
            ecran.blit(balai, (622.5, 248))
            choix_1_ecrit = "854"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (622.5, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie2, (682.5, 411))
            ecran.blit(monnaie2, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter un balai"
            choix_2_ecrit = f"Ne pas acheter"
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
                    EFE = True
                    joueur.argent = joueur.argent - 854
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFF = True
    while EEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à sa recherche"
            choix_2_ecrit = f"Acheter un balai"
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
                    EEEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EEEF = True
    while EEF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à ça recherche"
            choix_2_ecrit = f"laisser tomber"
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
                    EEFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Ah ouais... Dès le début tu abandonnes"
    while EFE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois avoir eu sa réponse, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Demander si le marchand à vu {joueur.cible.genremini}"
            choix_2_ecrit = f"Se débrouiller seul"
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
                    EFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFEF = True
    while EFF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} reste afin de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une potion"
            choix_2_ecrit = f"Partir"
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
                    EFFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFFF = True
    while EEEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois arriver dans sa ville, {joueur.prenom} apperçoit {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EEEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EEEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une potion"
            choix_2_ecrit = f"Le combattre avec sa magie"
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
                    EEEEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin ="Malheureusement ta magie n'est pas assez forte"
    while EEEF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En sortant du magasin, {joueur.prenom} tombe sur {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EEEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EEEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser son balai"
            choix_2_ecrit = f"Utiliser sa magie"
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
                    gagner = True
                    texte_fin = "Bravo ! Tu as réussi rapidement à battre ton adversaire"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça sert d'avoir acheter un balai si ce n'est pas pour l'utiliser"
    while EEFE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de"
            ecran.blit(gamyris, (233.8, 390))
            ecran.blit(hypolys, (506.6, 370))
            ecran.blit(orphenea, (768.4, 365))
            ecran.blit(rhyseas, (1041.2, 385))
            choix_1_ecrit = "10"
            choix_2_ecrit = "10"
            choix_3_ecrit = "10"
            choix_4_ecrit = "10"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_5 = font.render(choix_4_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (233.8, 421))
            ecran.blit(texte_choix_2, (506.6, 421))
            ecran.blit(texte_choix_3, (768.4, 421))
            ecran.blit(texte_choix_5, (1041.2, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie2, (244.6, 411))
            ecran.blit(monnaie2, (538.2, 411))
            ecran.blit(monnaie2, (799.8, 411))
            ecran.blit(monnaie2, (1039.4, 411))
            ecran.blit(monnaie2, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EEFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EEFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une potion"
            choix_2_ecrit = f"Ne rien acheter"
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
                    EEFEE = True
                    joueur.argent = joueur.argent - 10
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Perdu ! Transforme toi en rat à ce rythme là !"
    while EFEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois avoir eu sa réponse, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir après avoir eu sa réponse"
            choix_2_ecrit = f"Rester en ville"
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
                    EFEF = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFEEF = True
    while EFFE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Choisi ta potion !"
            ecran.blit(gamyris, (233.8, 390))
            ecran.blit(hypolys, (506.6, 370))
            ecran.blit(orphenea, (768.4, 365))
            ecran.blit(rhyseas, (1041.2, 385))
            choix_1_ecrit = "10"
            choix_2_ecrit = "10"
            choix_3_ecrit = "10"
            choix_4_ecrit = "10"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_5 = font.render(choix_4_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (233.8, 421))
            ecran.blit(texte_choix_2, (506.6, 421))
            ecran.blit(texte_choix_3, (768.4, 421))
            ecran.blit(texte_choix_5, (1041.2, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie2, (244.6, 411))
            ecran.blit(monnaie2, (538.2, 411))
            ecran.blit(monnaie2, (799.8, 411))
            ecran.blit(monnaie2, (1039.4, 411))
            ecran.blit(monnaie2, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1_4.coordonnees)
            ecran.blit(choix_2, image_choix_2_4.coordonnees)
            ecran.blit(choix_3, image_choix_3_4.coordonnees)
            ecran.blit(choix_4, image_choix_4.coordonnees)
            choix_1_ecrit = f"Acheter hypolys"
            choix_2_ecrit = f"Acheter gamyris"
            choix_3_ecrit = f"Acheter rhyseas"
            choix_4_ecrit = f"Acheter orphénea"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(choix_4_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1_4.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2_4.coordonnees)
            ecran.blit(texte_choix_3, image_choix_3_4.coordonnees)
            ecran.blit(texte_choix_4, image_choix_4.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1.carre[0] <= souris[0] <= image_choix_1.carre[1] and image_choix_1.carre[2] <= souris[1] <= \
                        image_choix_1.carre[3]:
                    choix = False
                    EFFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_3.carre[0] <= souris[0] <= image_choix_3.carre[1] and image_choix_3.carre[2] <= souris[1] <= \
                        image_choix_3.carre[3]:
                    choix = False
                    EFFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_4.carre[0] <= souris[0] <= image_choix_4.carre[1] and image_choix_4.carre[2] <= souris[1] <= \
                        image_choix_4.carre[3]:
                    choix = False
                    EFFEF = True
    while EFFF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois sortie de la boutique {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Rester dans la ville"
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
                    EFFFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFFFF = True
    while EFFEE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Rester raisonnable"
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
                    perdu = True
                    texte_fin = "Tu n'avais pas assez d'argent"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFEF = True
    while EEEEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En sortant du magasin {joueur.prenom} croise {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EEEEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EEEEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser la potion"
            choix_2_ecrit = f"Ne pas l'utiliser"
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
                    gagner = True
                    texte_fin = "Bravo tu as gagné !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça sert d'avoir acheter une potion si ce n'est pas pour l'utiliser"
    while EEFEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En sortant du magasin {joueur.prenom} croise {joueur.cible.penom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EEFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EEFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser la potion"
            choix_2_ecrit = f"Ne pas l'utiliser"
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
                    gagner = True
                    texte_fin = "Bravo tu as gagné !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça sert d'avoir acheter une potion si ce n'est pas pour l'utiliser"
    while EFEF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
            choix_2_ecrit = f"Rester en ville"
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
                    EFEFF = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'es pas venu pour te balader"
    while EFFEF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas acheter"
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
                    EFFEFE = True
                    joueur.argent = joueur.argent - 10
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Mais la potion ne coutait pas cher"
    while EFFFE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures de recherches {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une potion"
            choix_2_ecrit = f"Utiliser sa magie"
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
                    EFFFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = ""
    while EFFFF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Acheter un balai"
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
                    EFFFFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    EFFFFF = True
    while EFFEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de "
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    EFEFF = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Ton but n'est pas de faire du tourisme"
    while EFEFF:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois face à {joueur.cible.prenom}, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFEFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFEFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter un balai"
            choix_2_ecrit = f"Le combattre avec les poings"
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
                    EFEEFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Mais tu as de la magie, pourquoi utiliser ses poings ?"
    while EFEEF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            ecran.blit(balai, (622.5, 248))
            choix_1_ecrit = "854"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (622.5, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie2, (682.5, 411))
            ecran.blit(monnaie2, (60, 439))
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFEEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFEEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter un balai"
            choix_2_ecrit = f"Ne rien acheter"
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
                    EFEEFE = True
                    joueur.argent = joueur.argent - 854
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu comptes te battre les mains vide ?"
    while EFEEFE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois devant {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFEEFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFEEFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser le balai"
            choix_2_ecrit = f"Ne pas l'utiliser"
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
                    gagner = True
                    texte_fin = "Bravooooo ! Tu as gagné !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "A quoi ça sert d'acheter un balai pour ne pas l'utiliser"
    while EFFEFE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois devant {joueur.cible.prenom}, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFEFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFEFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser sa potion"
            choix_2_ecrit = f"Ne rien faire"
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
                    gagner = True
                    texte_fin = "Bravooo !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu t'es découragé ?"
    while EFFFFF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir acheter un balai {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFFFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFFFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    EFFFFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Ton but n'est pas de devenir un touriste"
    while EFFFFE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFFFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFFFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter une potion"
            choix_2_ecrit = f"Utiliser sa magie"
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
                    EFFFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'as pas assez de pouvoirs pour combattre ton ennemi"
    while EFFFEE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} se retrouve devant {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                EFFFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    EFFFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ce que {joueur.prenom} a acheté contre ton {joueur.cible.prenom}"
            choix_2_ecrit = f"Ne rien faire"
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
                    gagner = True
                    texte_fin = "Bravo ! Tu as gagné !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Pourquoi ne rien faire ?"
    while F:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après l'avoir combattu, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                F = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    F = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Prendre l'argent"
            choix_2_ecrit = f"Refuser l'argent"
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
                    FE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= \
                souris[1] <= image_choix_2.carre[3]:
                    choix = False
                    FF = True
    while FE:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois l'argent pris {joueur.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser l'argent pour acheter une potion"
            choix_2_ecrit = f"Ne pas l'utiliser"
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
                    FEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FFE = True
    while FEE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            ecran.blit(gamyris, (233.8, 390))
            ecran.blit(hypolys, (506.6, 370))
            ecran.blit(orphenea, (768.4, 365))
            ecran.blit(rhyseas, (1041.2, 385))
            choix_1_ecrit = "10"
            choix_2_ecrit = "10"
            choix_3_ecrit = "10"
            choix_4_ecrit = "10"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_5 = font.render(choix_4_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (233.8, 421))
            ecran.blit(texte_choix_2, (506.6, 421))
            ecran.blit(texte_choix_3, (768.4, 421))
            ecran.blit(texte_choix_5, (1041.2, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie2, (244.6, 411))
            ecran.blit(monnaie2, (538.2, 411))
            ecran.blit(monnaie2, (799.8, 411))
            ecran.blit(monnaie2, (1039.4, 411))
            ecran.blit(monnaie2, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1_4.coordonnees)
            ecran.blit(choix_2, image_choix_2_4.coordonnees)
            ecran.blit(choix_3, image_choix_3_4.coordonnees)
            ecran.blit(choix_4, image_choix_4.coordonnees)
            choix_1_ecrit = f"Acheter hypolys"
            choix_2_ecrit = f"Acheter gamyris"
            choix_3_ecrit = f"Acheter rhyseas"
            choix_4_ecrit = f"Acheter orphénea"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(choix_4_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1_4.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2_4.coordonnees)
            ecran.blit(texte_choix_3, image_choix_3_4.coordonnees)
            ecran.blit(texte_choix_4, image_choix_4.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1_4.carre[0] <= souris[0] <= image_choix_1_4.carre[1] and image_choix_1_4.carre[2] <= souris[1] <= \
                        image_choix_1_4.carre[3]:
                    choix = False
                    FEEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2_4.carre[0] <= souris[0] <= image_choix_2_4.carre[1] and image_choix_2_4.carre[2] <= souris[1] <= \
                        image_choix_2_4.carre[3]:
                    choix = False
                    FEEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_3_4.carre[0] <= souris[0] <= image_choix_3_4.carre[1] and image_choix_3_4.carre[2] <= souris[1] <= \
                        image_choix_3_4.carre[3]:
                    choix = False
                    FEEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_4.carre[0] <= souris[0] <= image_choix_4.carre[1] and image_choix_4.carre[2] <= souris[1] <= \
                        image_choix_4.carre[3]:
                    choix = False
                    FEEE = True
    while FEEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après être sorti du marchand, {joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas acheter"
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
                    joueur.argent = joueur.argent -10
                    FEEFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FEEFF = True
    while FEEFF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEEFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEEFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Rester en ville"
            choix_2_ecrit = f"Partir à la recherche de {joueur.cible.genremini}"
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
                    perdu = True
                    texte_fin = "Ce n'est pas le moment se balader"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FEEFFE = True
    while FEEFFE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} cherche {joueur.cible.prenom} et tombe par hasard sur lui dans la forêt."
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEEFFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEEFFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ta potion"
            choix_2_ecrit = f"Le battre avec ta magie"
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
                    gagner = True
                    texte_fin = "Bravoooo ! Tu as gagné"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Et la potion que tu as acheté ?"
    while FEEFE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir acheter sa potion {joueur.prenom} décide"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEEFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEEFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Rester en ville"
            choix_2_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
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
                    FEEFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FEEFEF = True
    while FEEFEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de rester en ville"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEEFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEEFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir acheter un balai"
            choix_2_ecrit = f"Ne rien faire"
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
                    FEEFEEF = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu es un peu flemmard je trouve"
    while FEEFEEF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois à la boutique du marchand {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEEFEEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEEFEEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas acheter"
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
                    FEEFEEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu es quel personnage dans les Ratz ?"
    while FEEFEEE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} croise le chemin de {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEEFEEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEEFEEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser le balai et la potion"
            choix_2_ecrit = f"Fuir le combat"
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
                    gagner = True
                    texte_fin = "Wow ! Bravo !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "BOUH ! T'ES NUL !"
    while FEEFEF:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} part à la recherche de {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEEFEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEEFEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Fuir"
            choix_2_ecrit = f"Utiliser la potion"
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
                    perdu = True
                    texte_fin = "La solution n'est pas la fuite"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    gagner = True
                    texte_fin = "Bravo ! Tu as gagné !"
    while FEF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Suite à cette description {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    FEFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FEFF = True
    while FEFE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après des heures sans aucune trace de {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Chercher à {joueur.nom_de_ville}"
            choix_2_ecrit = f"Continuer de chercher dans la forêt"
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
                    FEFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FEFEF = True
    while FEFEE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En cherchant dans sa ville {joueur.prenom} croise {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir acheter une potion"
            choix_2_ecrit = f"Utiliser sa magie"
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
                    FEFEEF = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "C'est triste mais il va falloir plus que ça pour battre ton ennemi"
    while FEFEF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En cherchant dans la ville {joueur.prenom} croise {joueur.cible.genremini}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir acheter une potion"
            choix_2_ecrit = f"Utiliser sa magie"
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
                    FEFEEF = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "C'est triste mais il va falloir plus que ça pour battre ton ennemi"
    while FEFEEF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois chez le marchand, {joueur.prenom} décide de :"
            ecran.blit(potions, (618, 307))
            choix_1_ecrit = "40"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (618, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie2, (678, 411))
            ecran.blit(monnaie2, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFEEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFEEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter les potions"
            choix_2_ecrit = f"Ne pas l'acheter"
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
                    FEFEEE = True
                    joueur.argent = joueur.argent - 40
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu voulais juste faire les boutiques ?"
    while FEFEEE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.cible.prenom} entre dans la boutique lui aussi"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFEEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFEEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Lui lancer la potion"
            choix_2_ecrit = f"Se cacher"
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
                    gagner = True
                    texte_fin = "You're a winner !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu n'as plus 4 ans, faut arrêter de jouer à cache-cache"
    while FF:
        for evenement in pygame.event.get():
            ecran.blit(bar, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après ça {joueur.prenom} part :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(bar, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Se promener dans {joueur.nom_de_ville}"
            choix_2_ecrit = f"Acheter une potion"
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
                    FFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FFF = True
    while FEFF:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"En se promenant en ville {joueur.prenom} tombe sur l'autre sorcier"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = sorcier_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Demander où se trouve {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    FEFFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "La ville est peut-être jolie, mais bon faut pas oublier ton objectif"
    while FEFFE:
        for evenement in pygame.event.get():
            ecran.blit(ville_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir eu sa réponse, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(ville_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Acheter un balai"
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
                    FEFEFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FFEE = True
    while FEFEFE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois dans la forêt {joueur.prenom} tombe sur {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFEFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFEFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser sa magie"
            choix_2_ecrit = f"Utiliser son balai cassé"
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
                    perdu = True
                    texte_fin = "Malheureusement tu n'as pas assez de magie"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Mais il est cassé, tu ne peux pas l'utiliser"
    while FFE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"{joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter un balai"
            choix_2_ecrit = f"Acheter une potion"
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
                    FFEE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    FFF = True
    while FFEE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Un fois chez le marchand {joueur.prenom} décide de"
            ecran.blit(balai, (622.5, 248))
            choix_1_ecrit = "854"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (622.5, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie2, (682.5, 411))
            ecran.blit(monnaie2, (60, 439))
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FFEE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FFEE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter"
            choix_2_ecrit = f"Ne pas acheter"
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
                    FEFEFEF = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Comment veux tu battre ton ennemi maintenant ?"
    while FEFEFEF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Après avoir acheter le balai"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FEFEFEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FEFEFEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    FFEFF = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Je ne jugerai pas ton choix..."
    while FFEFF:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois dan la forêt {joueur.prenom} rencontre {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FFEFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FFEFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ton balai"
            choix_2_ecrit = f"Fuir"
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
                    gagner = True
                    texte_fin = "Bravoooo !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Tu es un peureux !"
    while FFF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            ecran.blit(gamyris, (233.8, 390))
            ecran.blit(hypolys, (506.6, 370))
            ecran.blit(orphenea, (768.4, 365))
            ecran.blit(rhyseas, (1041.2, 385))
            choix_1_ecrit = "10"
            choix_2_ecrit = "10"
            choix_3_ecrit = "10"
            choix_4_ecrit = "10"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_5 = font.render(choix_4_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(str(joueur.argent), True, (0, 0, 0))
            ecran.blit(texte_choix_1, (233.8, 421))
            ecran.blit(texte_choix_2, (506.6, 421))
            ecran.blit(texte_choix_3, (768.4, 421))
            ecran.blit(texte_choix_5, (1041.2, 421))
            ecran.blit(texte_choix_4, (0, 449))
            ecran.blit(monnaie2, (244.6, 411))
            ecran.blit(monnaie2, (538.2, 411))
            ecran.blit(monnaie2, (799.8, 411))
            ecran.blit(monnaie2, (1039.4, 411))
            ecran.blit(monnaie2, (60, 439))
            histoire_1 = f"{joueur.prenom} se rend dans la boutique du marchand"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FFF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FFF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1_4.coordonnees)
            ecran.blit(choix_2, image_choix_2_4.coordonnees)
            ecran.blit(choix_3, image_choix_3_4.coordonnees)
            ecran.blit(choix_4, image_choix_4.coordonnees)
            choix_1_ecrit = f"Acheter hypolys"
            choix_2_ecrit = f"Acheter gamyris"
            choix_3_ecrit = f"Acheter rhyseas"
            choix_4_ecrit = f"Acheter orphénea"
            texte_choix_1 = font.render(choix_1_ecrit, True, (0, 0, 0))
            texte_choix_2 = font.render(choix_2_ecrit, True, (0, 0, 0))
            texte_choix_3 = font.render(choix_3_ecrit, True, (0, 0, 0))
            texte_choix_4 = font.render(choix_4_ecrit, True, (0, 0, 0))
            ecran.blit(texte_choix_1, image_choix_1_4.coordonnees)
            ecran.blit(texte_choix_2, image_choix_2_4.coordonnees)
            ecran.blit(texte_choix_3, image_choix_3_4.coordonnees)
            ecran.blit(texte_choix_4, image_choix_4.coordonnees)
            pygame.display.flip()
            if au_revoir_jeu(evenement) == True:
                choix = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_1_4.carre[0] <= souris[0] <= image_choix_1_4.carre[1] and image_choix_1_4.carre[2] <= \
                        souris[1] <= \
                        image_choix_1_4.carre[3]:
                    choix = False
                    FFEF = True
                    potion = "hypolys"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2_4.carre[0] <= souris[0] <= image_choix_2_4.carre[1] and image_choix_2_4.carre[2] <= \
                        souris[1] <= \
                        image_choix_2_4.carre[3]:
                    choix = False
                    FFEF = True
                    potion = "gamyris"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_3_4.carre[0] <= souris[0] <= image_choix_3_4.carre[1] and image_choix_3_4.carre[2] <= \
                        souris[1] <= \
                        image_choix_3_4.carre[3]:
                    choix = False
                    FFEF = True
                    potion = "rhyseas"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_4.carre[0] <= souris[0] <= image_choix_4.carre[1] and image_choix_4.carre[2] <= souris[
                    1] <= \
                        image_choix_4.carre[3]:
                    choix = False
                    FFEF = True
                    potion = "orphénea"
    while FFEF:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f""
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FFEF = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FFEF = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Acheter {potion}"
            choix_2_ecrit = f"Ne pas acheter"
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
                    FFFE = True
                    joueur.argent = joueur.argent - 10
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "perdu ! Il faut arrêter d'être radin"
    while FFFE:
        for evenement in pygame.event.get():
            ecran.blit(marchand_sorcier, (0,0))
            pygame.display.set_caption("SORCIER")
            perso2 = joueurnormal
            ecran.blit(perso2, perso_seul)
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois avoir choisi {potion}, {joueur.prenom} décide de :"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FFFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FFFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(marchand_sorcier, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_seul)
            souris = pygame.mouse.get_pos()
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Partir à la recherche de {joueur.cible.prenom}"
            choix_2_ecrit = f"Rester en ville"
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
                    FFFFE = True
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = f"Et {joueur.cible.prenom} dans tout ça ?"
    while FFFFE:
        for evenement in pygame.event.get():
            ecran.blit(foret3, (0,0))
            perso2 = joueurnormal
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            pygame.display.set_caption("SORCIER")
            ecran.blit(brouillard_histoire, brouillard_histoire_donnees.coordonnees)
            histoire_1 = f"Une fois dans la forêt, {joueur.prenom} croise {joueur.cible.prenom}"
            texte_truc_1 = font.render(histoire_1, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                FFFFE = False

            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RETURN:
                    FFFFE = False
                    choix = True
    while choix:
        for evenement in pygame.event.get():
            pygame.display.set_caption("SORCIER")
            ecran.blit(foret3, (0,0))
            perso2 = joueurreflechi
            ecran.blit(perso2, perso_deux_1)
            perso3 = bandit_normal
            ecran.blit(perso3, perso_deux_2)
            ecran.blit(choix_1, image_choix_1.coordonnees)
            ecran.blit(choix_2, image_choix_2.coordonnees)
            choix_1_ecrit = f"Utiliser ta potion"
            choix_2_ecrit = f"Utiliser ta magie"
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
                    gagner = True
                    texte_fin = "Bravo ! En utilisant ta potion, tu lui a laissé aucune chance !"
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if image_choix_2.carre[0] <= souris[0] <= image_choix_2.carre[1] and image_choix_2.carre[2] <= souris[1] <= \
                        image_choix_2.carre[3]:
                    choix = False
                    perdu = True
                    texte_fin = "Malheureusement tu connais pas aussez de sort pour ça."



#Les boucles de fin
    while perdu:
        for evenement in pygame.event.get():
            ecran.blit(image_perdu, (0, 0))
            pygame.display.set_caption("PERDU !!!")
            texte_truc_1 = font.render(texte_fin, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                perdu = False
    while gagner:
        for evenement in pygame.event.get():
            ecran.blit(image_gagner, (0, 0))
            pygame.display.set_caption("GAGNER !!!")
            texte_truc_1 = font.render(texte_fin, True, (0, 0, 0))
            ecran.blit(texte_truc_1, (0, 477))
            pygame.display.update()
            if au_revoir_jeu(evenement) == True:
                gagner = False

jeu()
