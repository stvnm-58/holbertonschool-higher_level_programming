#!/usr/bin/env python3
"""Module pour convertir des données au format CSV vers le format JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Lit un fichier CSV et convertit son contenu en un fichier JSON.

    Chaque ligne du CSV est transformée en dictionnaire grâce à DictReader,
    puis la liste complète est sauvegardée dans 'data.json'.

    Args:
        csv_filename (str): Le nom du fichier CSV source à lire.

    Returns:
        bool: True si la conversion a réussi, False en cas d'erreur (ex: fichier introuvable).
    """
    try:
        # 1. Lecture du fichier CSV d'origine
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            # DictReader utilise la première ligne du CSV comme clés de dictionnaire
            csv_reader = csv.DictReader(csv_file)

            # Conversion du reader en une vraie liste de dictionnaires Python
            data_list = list(csv_reader)

        # 2. Écriture et sérialisation dans le fichier data.json
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            # json.dump convertit la liste de dictionnaires en texte JSON
            json.dump(data_list, json_file)

        return True

    except (FileNotFoundError, OSError):
        # Renvoie False si le fichier source n'existe pas ou s'il y a un problème d'accès
        return False
