# Encodage : UTF8
# Python 3.9
# Auteur : Estelle Bandhavong

class Personnage:
    def __init__(self,  prenom: str, sexe: str):
        """ sexe est attendu sous la forme "f" ou "h"."""

        self.prenom = prenom
        self.sexe = sexe
        self.amis = []


