#       Ejercicios complementarios
#   desarrollar un programa que determine si una lista esta ordenada de forma ascendente

def lista_ordenada(lista):
    for i in range(len(lista)-1):
                   if lista[i]>lista [i+1]:
                        return False
                   return True
    
def lista_creada():
        lista=[]
        while True:
            valor = input ("ingrese un valor a la lista o 'fin' si desea terminar la lista: ")
            if valor.lower() == 'fin':
                   break
            lista.append(valor)
        return lista
lista = lista_creada()

print ("la lista esta ordenada de forma ascendente"if lista_ordenada(lista) else "la lista no esta ordenada de forma ascendente")