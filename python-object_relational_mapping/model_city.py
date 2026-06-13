#!/usr/bin/python3
"""Contient la définition de la classe City."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Représente une ville pour une base de données MySQL.

    Attributs:
        id (int): L'identifiant unique de la ville (Clé primaire).
        name (str): Le nom de la ville.
        state_id (int): L'identifiant de l'état associé (Clé étrangère).
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
