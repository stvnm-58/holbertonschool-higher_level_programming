#!/usr/bin/env python3
"""Module pour sérialiser et désérialiser des données au format XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire Python au format XML et le sauvegarde.

    Args:
        dictionary (dict): Le dictionnaire contenant les paires clé-valeur.
        filename (str): Le nom du fichier XML de sortie.
    """
    # Création de l'élément racine <data>
    root = ET.Element("data")

    # Parcours du dictionnaire pour ajouter chaque clé-valeur comme enfant
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # Le texte du nœud XML doit obligatoirement être une chaîne (str)
        child.text = str(value)

    # Création de l'arbre XML à partir de la racine
    tree = ET.ElementTree(root)

    # Écriture de l'arbre dans le fichier avec l'encodage approprié
    with open(filename, mode="wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Lit un fichier XML et le reconstruit sous forme de dictionnaire Python.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        dict: Un dictionnaire contenant les données lues du XML.
    """
    try:
        # Analyse du fichier XML pour obtenir l'arbre
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstitution du dictionnaire en parcourant les enfants de la racine
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except (FileNotFoundError, ET.ParseError, OSError):
        # Sécurité en cas de fichier introuvable ou XML malformé
        return None
