# -*- coding: utf-8 -*-
"""
Premier fichier Projet Innovation : définition class

"""

class resident:
    nombre_resident=0
    def __init__(self,parametre_resident_1):
        self.id_resident=resident.nombre_resident
        resident.nombre_resident +=1
        self.parametre_resident_1=parametre_resident_1

class chambre:
    nombre_chambre=0
    def __init__(self,liste_id_resident,parametre_chambre_1):
        self.id_chambre=chambre.nombre_chambre
        chambre.nombre_chambre+=1
        self.id_resident=liste_id_resident
        self.parametre_chambre_1=parametre_chambre_1

class groupement:
    nombre_groupement=0
    def __init__(self,liste_id_chambre):
        groupement.id_groupement=groupement.nombre_groupement
        groupement.nombre_groupement+=1
        self.taille=len(liste_id_chambre)
        self.liste_id_chambre=liste_id_chambre

class batiment:
    nombre_batiment=0
    def __init__(self,liste_id_groupement):
        batiment.id_batiment=batiment.nombre_batiment
        batiment.liste_id_groupement=liste_id_groupement

class residence:
    def __init__(self,liste_id_batiement):
        residence.liste_id_batiement=liste_id_batiement


        
        
        
print(3)


