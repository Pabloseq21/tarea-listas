#                primer problema ejercicios programacion de computadores 
#   desarrollar un programa que detecte si en una lista no existan elementos repetidos 

def obtener_lista():
    lista = []
    while True: 
        valor = input("Ingrese un valor a la lista o 'fin' para terminar: ") 
        if valor.lower() == 'fin':
            break
        lista.append(valor)
    return lista 

def repetidos_en_lista(x):
    for i in x:
        if x.count(i) > 1:
            return True
    return False

lista = obtener_lista()

if repetidos_en_lista(lista):
    print("La lista tiene elementos repetidos")
else:
    print("La lista no tiene elementos repetidos")