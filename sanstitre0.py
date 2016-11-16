# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:24:10 2016

@author: Actif
"""

import xlrd
# ouverture du fichier Excel 
wb = xlrd.open_workbook('fichier test.xlsx')
 
# feuilles dans le classeur
print (wb.sheet_names())

 
# lecture des données dans la première feuille
sh = wb.sheet_by_name(u'Feuil1')
for rownum in range(sh.nrows):
    print (sh.row_values(rownum))
    
colonne1 = sh.col_values(0)
print (colonne1)