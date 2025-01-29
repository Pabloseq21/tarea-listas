#                            desarrolle un programa que determine si una lista es palindrome.
#   una lista es palindrome si el elemento en la posicion i es igual al elemento en la posicion n-i-1 con n la longitud de la lista 

def lista_palindrome(lista):
    for i in range(len(lista)//2):
        if lista[i] != lista[-i-1]:
            return False
    return True

lista = [1, 2, 3, 4, 3, 2, 1]

print("la lista es palindrome" if lista_palindrome(lista) else "la lista no es palindrome")