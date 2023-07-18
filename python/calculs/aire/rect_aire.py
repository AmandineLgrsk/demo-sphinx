"""
Ce fichier n'est composé que d'une seule fonction :
    * rect_aire.py

Pour calculer l'aire d'un rectangle, on va faire appel
à la fonction multiplier(a, b) du module operations.

Il faut donc indiquer le chemin vers "operations".
"""

import sys

sys.path.append('/home/onyxia/work/demo-sphinx/python/operations')

import operations as op


def calculer_aire_rectangle(longueur, largeur):
    """
    Calcule l'aire d'un rectangle.

    Args:
        longueur (int ): La longueur du rectangle.
        largeur (int): La largeur du rectangle.

    Returns:
        int: L'aire du rectangle.
    """
    return op.multiplier(longueur, largeur)
