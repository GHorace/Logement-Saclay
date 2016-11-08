# -*- coding: utf-8 -*-
"""
Premier fichier Projet Innovation : reader d'Excel 
fonction 

"""

import xlrd

wb = xlrd.open_workbook('.xls')

class eleve :
    
    def _init_(self):
        self.critere1 = 0