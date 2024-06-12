from Affirmation import Vérité, Mensonge, Affirmation
from TableDeVérité import TableDeVérité

class CalculateurDeVérité:
    def __init__(self):
        self.table_verite = TableDeVérité()

    def calculer_vérité(self, affirmation1, opérateur, affirmation2=None):
        if affirmation2 is None:
            valeur1 = affirmation1.get_valeur_de_vérité()
            valeur2 = opérateur.get_valeur_de_vérité()
        else:
            valeur1 = affirmation1.get_valeur_de_vérité()
            valeur2 = affirmation2.get_valeur_de_vérité()

        if opérateur == "ou":
            return self.table_verite.ou(valeur1, valeur2)
        elif opérateur == "et":
            return self.table_verite.et(valeur1, valeur2)
        elif opérateur == "donc":
            return self.table_verite.donc(valeur1, valeur2)
        else:
            raise ValueError("Opérateur non supporté")


vérité_1 = Vérité("Lou est beau.")
mensonge_1 = Mensonge("Lou est pauvre.")
affirmation_1 = Affirmation("Lou est généreux.")

calculateur = CalculateurDeVérité()

resultat = calculateur.calculer_vérité(vérité_1, "et", affirmation_1)
print(resultat)
