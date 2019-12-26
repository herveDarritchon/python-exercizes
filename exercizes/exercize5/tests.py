import unittest

from exercizes.exercize5.main import inverse_list, decale_un_cran_gauche, decale_n_fois_gauche, decale_un_cran_droite, \
    decale_n_fois_droite, decale_n_fois_droite_optimise


class OperationListTest(unittest.TestCase):
    liste_initiale = [1, 2, 3, 4, 5, 6, 7]

    def test_rotation_list(self):
        resultat_attendu = [7, 6, 5, 4, 3, 2, 1]
        resultat = inverse_list(self.liste_initiale)
        self.assertEqual(resultat_attendu, resultat, "pb lors de l'inversion de la liste")

    def test_rotation_list_aleatoire(self):
        liste_initiale_aleatoire = [2, 3, 6, 12, 7, 8]
        resultat_attendu = [8, 7, 12, 6, 3, 2]
        resultat = inverse_list(liste_initiale_aleatoire)
        self.assertEqual(resultat_attendu, resultat, "pb lors de l'inversion de la liste aléatoire")

    def test_rotation_list_deux_fois(self):
        resultat = inverse_list(self.liste_initiale)
        resultat = inverse_list(resultat)
        self.assertEqual(self.liste_initiale, resultat, "pb lors de la double inversion de la liste")

    def test_decalage_gauche_un_cran(self):
        resultat_attendu = [2, 3, 4, 5, 6, 7, 1]
        resultat = decale_un_cran_gauche(self.liste_initiale)
        self.assertEqual(resultat_attendu, resultat, "pb lors de décalage d'un cran vers la gauche")

    def test_decalage_gauche_deux_crans(self):
        resultat_attendu = [3, 4, 5, 6, 7, 1, 2]
        resultat = decale_un_cran_gauche(self.liste_initiale)
        resultat = decale_un_cran_gauche(resultat)
        self.assertEqual(resultat_attendu, resultat, "pb lors de décalage de deux crans vers la gauche")
        resultat = decale_n_fois_gauche(self.liste_initiale, 2)
        self.assertEqual(resultat_attendu, resultat,
                         "pb lors de décalage de deux crans vers la gauche de manière générique")

    def test_decalage_gauche_un_cycle(self):
        resultat = decale_n_fois_gauche(self.liste_initiale, len(self.liste_initiale))
        self.assertEqual(self.liste_initiale, resultat, "pb lors de décalage de deux crans vers la gauche")

    def test_decalage_droite_un_cran(self):
        resultat_attendu = [7, 1, 2, 3, 4, 5, 6]
        resultat = decale_un_cran_droite(self.liste_initiale)
        self.assertEqual(resultat_attendu, resultat, "pb lors de décalage d'un cran vers la droite")

    def test_decalage_doite_deux_crans(self):
        resultat_attendu = [6, 7, 1, 2, 3, 4, 5]
        resultat = decale_un_cran_droite(decale_un_cran_droite(self.liste_initiale))
        self.assertEqual(resultat_attendu, resultat, "pb lors de décalage de deux crans vers la droite")
        resultat = decale_n_fois_droite(self.liste_initiale, 2)
        self.assertEqual(resultat_attendu, resultat, "pb lors de décalage de deux crans vers la droite")
        resultat = decale_n_fois_droite_optimise(self.liste_initiale, 2)
        self.assertEqual(resultat_attendu, resultat, "pb lors de décalage de deux crans vers la droite, version optimisée")
