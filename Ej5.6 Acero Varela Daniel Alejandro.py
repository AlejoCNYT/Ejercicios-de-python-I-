'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Acero Varela Daniel Alejandro
Lenguaje: Python

Ejemplo 6. Escribe las tablas de multiplicar en el rango de números enteros positivos
           que especifique el usuario.

'''

def pide_interv_e ():
    li = 1
    ls = 0
    while li > ls:
        li = int (input ("\nLímite inferior: "))
        ls = int (input ("Límite superior: "))
    print("\nEl límite es [", li, ",", ls, "].")
    return [li, ls]

def tabla_multiplicar(n):
    print("\nTabla del", n, "\n")
    for mult in range(10):
        print(n, "x", mult, "=", n*mult)

def tabla_multiplicar_interv(a, b):
    for num in range(a, b+1):
        tabla_multiplicar(num)
        input("\n\nPresione Enter para continuar ")

def main ( ):
    print ("\nEscribo las tablas de multiplicar que hay en el rango de números enteros")
    print ("que me indique.\n")
    print ("Por ejemplo: Las tablas de multiplicar en el rango [10, 12] serían las del 10, 11 y 12.")
    [a, b] = pide_interv_e ()
    tabla_multiplicar_interv(a, b)
    print ("\n\nFin.\n\n")
    
main ( )
