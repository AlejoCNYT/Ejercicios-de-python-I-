'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Lenguaje: Python

Ejemplo 9.1. Averiguar si un número entero e pertenece a la unión de los conjuntos formados por los números
             que pertenecen a los intervalos (a, b] y [5, c).
'''

def pertenece_union_interv ( ):
    print ("Averiguar si un número entero e pertenece a la unión de los conjuntos formados por los números")
    print ("que pertenecen a los intervalos (a, b] y [5, c)")
    e = int (input ("e = "))
    a = int (input ("a = "))
    b = int (input ("b = "))
    c = int (input ("c = "))
    print ("Dados los intervalos (", a, ",", b, "] y [5,", c, "):")
    if (e > a and e <= b) or (e >= 5 and e < c):
        print (e, "pertenece a la unión.")
    if (e <= a or e > b) and (e < 5 or e >= c):
        print (e, "NO pertenece a la unión.")
    print ("Fin.")

pertenece_union_interv ( )


