import xlrd
from xlwt import Workbook

def lire_excel(nom_excel, numero_feuille, colonne, ligne):
    wb = xlrd.open_workbook(nom_excel)
    feuilles = wb.sheet_names()
    #jusqu'ici tout est clair cependant noter que le numéro de feuille, de colonne et de ligne ira de 1 à n et non de 0 à n
    feuille_i = wb.sheet_by_name(feuilles[numero_feuille -1])
    colonne_i=feuille_i.col_values(colonne -1)
    return colonne_i[ligne-1]


def lire_nom_feuille(nom_excel):
    wb = xlrd.open_workbook(nom_excel)
    return wb.sheet_names()

def lire_excel_col(nom_excel, numero_feuille, colonne):
    wb = xlrd.open_workbook(nom_excel)
    feuilles = wb.sheet_names()
    #jusqu'ici tout est clair cependant noter que le numéro de feuille, de colonne et de ligne ira de 1 à n et non de 0 à n
    feuille_i = wb.sheet_by_name(feuilles[numero_feuille -1])
    colonne_i=feuille_i.col_values(colonne -1)
    return colonne_i

class excel_gestion():

    def __init__(self, nom_feuille1) :
        self.book = Workbook()
        self.feuilles = []
        self.feuilles.append(self.book.add_sheet(nom_feuille1))

    def ecrire_excel(self, numero_feuille, ligne, colonne, element):
        lignei = self.feuilles[numero_feuille-1].row(ligne-1)
        lignei.write(colonne-1,element)

    def ajout_feuille(self, nom_feuille):
        self.feuilles.append(self.book.add_sheet(nom_feuille))

    def creation (self, nom):
        self.book.save(nom)

print("Test")

print(lire_excel("Test3", 1, 1, 1))

print(lire_excel("Test3", 2, 2, 2))

print (lire_nom_feuille("Test3"))
Excel = excel_gestion ("feuille1")
Excel.ajout_feuille("feuille2")
Excel.ecrire_excel(1,1,1, "TOTO")
Excel.ecrire_excel(2,2,2,"TITI")
Excel.creation("Test4")
