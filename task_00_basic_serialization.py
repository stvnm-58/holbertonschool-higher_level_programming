#!/usr/bin/env python3
"""Module de sérialisation de base.

Ce module fournit des fonctions pour sauvegarder un dictionnaire Python
dans un fichier au format JSON, et pour charger un fichier JSON
afin de reconstruire le dictionnaire d'origine.
"""

import json


def serialize_and_save_to_file(data, filename):
    """Sérialise un dictionnaire Python et le sauvegarde dans un fichier JSON.

    Args:
        data (dict): Le dictionnaire Python contenant les données à sérialiser.
        filename (str): Le nom du fichier JSON de sortie.
    """
    # Ouverture du fichier en mode écriture ("w") avec encodage UTF-8
    with open(filename, mode="w", encoding="utf-8") as f:
        # json.dump convertit le dictionnaire en texte JSON et l'écrit dans f
        json.dump(data, f)


def load_and_deserialize(filename):
    """Charge un fichier JSON et le désérialise en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier JSON d'entrée à lire.

    Returns:
        dict: Le dictionnaire Python reconstruit avec les données du fichier.
    """
    # Ouverture du fichier en mode lecture ("r") avec encodage UTF-8
    with open(filename, mode="r", encoding="utf-8") as f:
        # json.load lit le texte JSON depuis f et le convertit en dictionnaire
        return json.load(f)
