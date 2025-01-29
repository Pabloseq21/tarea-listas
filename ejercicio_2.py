#       desarrolle un programa que determine si un elemento de una lista es una cadena palindrome.
#        si la cadena existe debe imprimirla y si no existe debe imprimir "la cadena no existe"

def elemento_es_palindrome(lista):
    for i in lista:
        if i == i [::-1]:
            return True 
        return False
    
def palindromos_lista(lista):
        palindromos = []
        for s in lista:
            if elemento_es_palindrome([s]):
                palindromos.append(s)
        return palindromos
lista= ['ana', 'oso', 'casa', 'calle', 'reconocer', 'hola', 'mundo', 'oso']

print (palindromos_lista(lista))