from Affirmation import Vérité, Mensonge, Affirmation
from TableDeVérité import TableDeVérité

class CalculateurDeVérité:
    def __init__(self):
        self.table_verite = TableDeVérité()

    def calculer_vérité(self, affirmation1, opérateur, affirmation2=None):
        if affirmation2 is None:
            return affirmation1
        
        if (affirmation1 == "vraie" or affirmation1 == "fausse" or affirmation1 == "je ne sais pas"):
            valeur1 = affirmation1
        else:
            valeur1 = affirmation1.get_valeur_de_vérité()
        
        if (affirmation2 == "vraie" or affirmation2 == "fausse" or affirmation2 == "je ne sais pas"):
            valeur2 =  affirmation1
        else:
            valeur2 = affirmation2.get_valeur_de_vérité()

        if opérateur == "ou":
            return self.table_verite.ou(valeur1, valeur2)
        elif opérateur == "et":
            return self.table_verite.et(valeur1, valeur2)
        elif opérateur == "donc":
            return self.table_verite.donc(valeur1, valeur2)
        else:
            raise ValueError("Opérateur inexistant")

vérité_1 = Vérité("Lou est beau.")
mensonge_1 = Mensonge("Lou est pauvre.")
affirmation_1 = Affirmation("Lou est généreux.")

calculateur = CalculateurDeVérité()

resultat = calculateur.calculer_vérité(mensonge_1, "et", affirmation_1)
resultat1 = calculateur.calculer_vérité(vérité_1, "donc", mensonge_1)
resultat2 = calculateur.calculer_vérité(mensonge_1, "donc", affirmation_1)
composition = calculateur.calculer_vérité(vérité_1, "ou", affirmation_1)
resultat3 = calculateur.calculer_vérité(composition, "donc", mensonge_1)
resultat4 =  calculateur.calculer_vérité(mensonge_1, "ou", affirmation_1)
composition1 = calculateur.calculer_vérité(resultat3, "ou", resultat4)

print(resultat)
print(resultat1)
print(resultat2)
print(resultat3)
print(composition1)