"""
Ce fichier est constitué de deux fonctions :
    * cercle_perimetre_rayon(r)
    * cercle_perimetre_diametre(d)

Ces deux fonctions permettent de calculer le périmètre
d'un cercle en fonction de soit le rayon soit le
diamètre.
"""
import numpy as np


def perimetre_cercle_rayon(r):
    """
    Calcule le périmètre d'un cercle connaissant son rayon.

    Args:
        r (float): Le rayon du cercle.

    Returns:
        float: Le périmètre du cercle.
    """
    return 2 * np.pi * r


def perimetre_cercle_diametre(d):
    """
    Calcule le périmètre d'un cercle connaissant son diamètre.

    Args:
        d (float): Le diamètre du cercle.

    Returns:
        float: Le périmètre du cercle.
    """
    return np.pi * d
