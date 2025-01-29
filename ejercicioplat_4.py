#       ejercicios complementarios
#   desarrolle un programa que determine si una lista es 'unimodal'
#    una lista es unimodal si primero aumenta y luego disminuye 

def unimodal(lista):
    if len(lista) < 3:  
        return "No es unimodal"
    i = 0
    while i < len(lista) - 1 and lista[i] <= lista[i + 1]:
        i += 1

    while i < len(lista) - 1 and lista[i] >= lista[i + 1]:
        i += 1

    if i == len(lista) - 1:
        return "Es unimodal"
    else:
        return "No es unimodal"
    
def obtener_lista():
    lista = []
    while True: 
        valor = input("Ingrese un valor a la lista o 'fin' para terminar: ") 
        if valor.lower() == 'fin':
            break
        lista.append(valor)
    return lista 

lista = obtener_lista()

print("es unimodal" if unimodal(lista) else "no es unimodal")

