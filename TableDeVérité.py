from Affirmation import *

class TableDeVérité():
    def __init__(self):
        pass

    def ou(self, valeur1, valeur2):
        if valeur1 == "vraie" or valeur2 == "vraie":
            return "vraie"
        elif valeur1 == "fausse" and valeur2 == "fausse":
            return "fausse"
        else:
            return "je ne sais pas"

    def et(self, valeur1, valeur2):
        if valeur1 == "vraie" and valeur2 == "vraie":
            return "vraie"
        elif valeur1 == "fausse" or valeur2 == "fausse":
            return "fausse"
        else:
            return "je ne sais pas"

    def donc(self, valeur1, valeur2):
        if valeur1 == "vraie" and valeur2 == "fausse":
            return "fausse"
        else:
            return "vraie"
