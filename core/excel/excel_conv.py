# -*- coding: utf-8 -*-

#convertit une string en list
def strToList(text):
    n=len(text)
    if n<=2:
        return []
    compteur=1
    result=[]
    while compteur <n:
        result.append(int(text[compteur]))
        compteur+=2
    return result

#convertit une string en bool
def strToBool(text):
    return text.lower()=="true"
