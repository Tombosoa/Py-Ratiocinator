class Affirmation:
    def __init__(self, phrase):
        self.phrase = phrase
        self.valeur = "je ne sais pas"

    def get_valeur_de_vérité(self):
        return self.valeur

class Vérité(Affirmation):
    def __init__(self, phrase):
        super().__init__(phrase)
        self.valeur = "vraie"

class Mensonge(Affirmation):
    def __init__(self, phrase):
        super().__init__(phrase)
        self.valeur = "fausse"
