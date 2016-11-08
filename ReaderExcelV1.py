# -*- coding: utf-8 -*-
"""
Premier fichier Projet Innovation : reader d'Excel 
fonction 

"""

import xlrd



wb = xlrd.open_workbook('fichier test.xlsx')

def fonction_retour_element(colonne, ligne):
    ensemble_feuilles = wb.sheet_names()
    feuille1 = wb.sheet_by_name(u'Feuil1')
    col = ensemble_feuilles.col_values(colonne)
    return (col[ligne])
    
print (fonction_retour_element(0,0))
    