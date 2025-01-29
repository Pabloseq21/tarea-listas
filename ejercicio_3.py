#   desarrolle un programa que determine si en una lista se encuentra una cadena de caracteres de dos o mas vocales.
#           si la cadena existe debe imprimirla y si no existe debe imprimir "la cadena no existe"
vocales = ['a','e','i','o','u']
lista = ['camilo','juanito','samuel','jose']

def vocales_cadena(cadena):
    
    for i in range(len(cadena) - 1):
        if cadena [i] in vocales and cadena [i+1] in vocales: 
            return True
    return False 

def Vocales_lista(lista):
    vocales =[]
    for cadena in lista:
        if vocales_cadena(cadena):
            vocales.append(cadena)
    return vocales

print(Vocales_lista(lista)) 