# Encodage : UTF8
# Python 3.9
# Auteur : Estelle Bandhavong

from Personnage import Personnage

#Les joueurs
class Bandit(Personnage):
    def __init__(self, prenom : str, sexe: str, ennemi : str = None, cible : str = None, genremini : str = None, genremasc : str = None, nom_de_ville : str = None):
        """ sexe est attendu sous la forme "f" ou "h"."""
        super().__init__(prenom, sexe)
        self.prenom = prenom
        self.sexe = sexe
        self.armes = []
        self.argent = 764
        self.sac_a_dos = []
        self.ennemi = ennemi
        self.cible = cible
        self.genremini = genremini
        self.genremasc = genremasc
        self.nom_de_ville = nom_de_ville


class Aventurier(Personnage):
    def __init__(self, prenom : str, sexe: str, ennemi : str = None, cible : str = None, genremini : str = None, genremasc : str = None, nom_de_ville : str = None):
        """ sexe est attendu sous la forme "f" ou "h"."""
        super().__init__(prenom, sexe)
        self.prenom = prenom
        self.sexe = sexe
        self.argent = 10000
        self.sac_a_dos = ["carte_nulle", "trésor"]
        self.ennemi = ennemi
        self.cible = cible
        self.genremini = genremini
        self.genremasc = genremasc
        self.nom_de_ville = nom_de_ville
        
        
class Sorcier(Personnage):
    def __init__(self, prenom : str, sexe: str, ennemi : str = None, cible : str = None, genremini : str = None, genremasc : str = None, nom_de_ville : str = None):
        """ sexe est attendu sous la forme "f" ou "h"."""
        super().__init__(prenom, sexe)
        self.prenom = prenom
        self.sexe = sexe
        self.argent = 1123
        self.inventaire = ["grimoire"]
        self.ennemi = ennemi
        self.cible = cible
        self.genremini=genremini
        self.genremasc = genremasc
        self.nom_de_ville = nom_de_ville

Snow = Bandit("Snow","f","C", "D", "la bandite", "La bandite")
Sylas = Bandit("Sylas", "m", "C", "D", "le bandit", "Le bandit")
Dora = Aventurier("Dora", "f", "C", "D", "l'aventurière", "L'aventurière")
Roudolf = Aventurier("Roudolf", "f", "C", "D", "l'aventurier", "L'aventurier")
Hazel = Sorcier("Hazel", "f","D","E","la sorcière", "La sorcière")
Merlin = Sorcier("Merlin","m","A","B","le sorcier", "Le sorcier")


