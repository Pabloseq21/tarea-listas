#   ejercicios complementarios
#   desarrollar un programa que determine si un elemento de la lista es un numero primo 

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):  
        if numero % i == 0:
            return False
    return True

def lista_primos (lista):
     primos = []
     for i in lista:
          if primo(i):
               primo.append(i)
     return primos


def lista1 ():
     lista =[]
     while True:
          valor =input("ingrese un valor a la lista o 'fin' si desea terminar la lista: ")
          if valor.lower() == 'fin':
               break 
          lista.append(int(valor))
          return lista 
lista = lista1()

#print ("si hay numeros primos" if primo(lista) else "no hay numeros primos")
#print (lista_primos(lista))