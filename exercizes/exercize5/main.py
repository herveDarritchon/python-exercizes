def inverse_list(liste_initiale):
    resultat = []
    for i in range(len(liste_initiale)):
        resultat.append(liste_initiale[len(liste_initiale) - i - 1])
    return resultat


def decale_un_cran_gauche(liste_initiale):
    resultat = []
    for i in range(len(liste_initiale)):
        if i + 1 >= len(liste_initiale):
            resultat.append(liste_initiale[0])
        else:
            resultat.append(liste_initiale[i + 1])
    return resultat


def decale_n_fois_gauche(liste_initiale, nb_cran):
    resultat = liste_initiale
    for i in range(nb_cran):
        resultat = decale_un_cran_gauche(resultat)
    return resultat


def decale_un_cran_droite(liste_initiale):
    resultat = []
    for i in range(len(liste_initiale)):
        if i + 1 >= len(liste_initiale):
            resultat.append(liste_initiale[i - 1])
        else:
            resultat.append(liste_initiale[i - 1])
    return resultat


def decale_n_fois_droite(liste_initiale, nb_cran):
    resultat = liste_initiale
    for i in range(nb_cran):
        resultat = decale_un_cran_droite(resultat)
    return resultat


def decale_n_fois_droite_optimise(liste_initiale, nb_cran):
    resultat = liste_initiale.copy()
    for i in range(len(liste_initiale)):
        u = (i + nb_cran) % len(liste_initiale)
        resultat[u] = liste_initiale[i]
    return resultat
