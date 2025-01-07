# Encodage : UTF8
# Python 3.9
# Auteur : Estelle Bandhavong

class image:
    def __init__(self,x : int or float, y: int or float):
        """ sexe est attendu sous la forme "f" ou "h"."""
        self.coordonnees = (x, y)


class el_boutton(image):
    def __init__(self, x : int or float, y: int or float, hauteur : int or float, largeur :int or float):
        """ sexe est attendu sous la forme "f" ou "h"."""
        super().__init__(y, x)
        self.coordonnees = (x, y)
        x_largeur = x + largeur
        y_hauteur = y + hauteur
        self.x = x
        self.y = y
        self.carre = (x, x_largeur, y, y_hauteur)


