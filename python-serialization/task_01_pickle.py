#!/usr/bin/env python3
"""Module pour la sérialisation d'objets personnalisés avec pickle.

Ce module définit la classe CustomObject qui sait s'afficher,
se sérialiser dans un fichier binaire et se désérialiser.
"""

import pickle


class CustomObject:
    """Une classe personnalisée représentant un profil d'individu."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialise les attributs de l'objet.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
            is_student (bool): Statut étudiant (Vrai/Faux).
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet selon le format attendu."""
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Is Student: {self.is_student}"
        )

    def serialize(self, filename):
        """Sérialise l'instance actuelle de l'objet dans un fichier binaire.

        Args:
            filename (str): Le nom du fichier de sortie.

        Returns:
            None ou int: Renvoie None en cas d'erreur ou si tout se passe bien.
        """
        try:
            # Ouverture en mode écriture binaire ("wb")
            with open(filename, "wb") as f:
                # pickle.dump écrit l'objet entier (self) dans le fichier f
                pickle.dump(self, f)
        except (Oscorror, pickle.PickleError):
            # Capture des erreurs de fichier ou de sérialisation
            return None

    @classmethod
    def deserialize(cls, filename):
        """Charge et renvoie une instance de CustomObject depuis un fichier.

        Args:
            filename (str): Le nom du fichier binaire à lire.

        Returns:
            CustomObject ou None: L'objet reconstruit, ou None en cas d'erreur.
        """
        try:
            # Ouverture en mode lecture binaire ("rb")
            with open(filename, "rb") as f:
                # pickle.load lit les octets et recrée l'objet d'origine
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError, AttributeError):
            # Capture si le fichier n'existe pas ou est corrompu
            return None
