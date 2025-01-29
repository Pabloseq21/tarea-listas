# ejercicios complementarios
# desarrollar un programa que determine si en una lista se encuetra un numero con dos o mas digitos pares 

def contador(n):
    count = 0
    while n > 0:
        digito = n % 10
        if digito % 2 == 0:
            count += 1
        n = n // 10
    return count

def numero(lista):
    numeros = []
    for numero in lista:
        if contador(numero) >= 2:
            numeros.append(numero)
            if numeros:
                print (numeros)
            else:
                print ("no hay numeros con dos o mas digitos pares")

lista = [123, 456, 789, 246, 135, 2468]

print ("si hay numeros con dos o mas digitos pares" if numero(lista) else "no hay numeros con dos o mas digitos pares")