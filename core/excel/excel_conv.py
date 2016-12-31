# -*- coding: utf-8 -*-

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

def strToBool(text):
    return text.lower()=="true"
