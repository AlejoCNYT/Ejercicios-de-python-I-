'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Autor: Daniel Alejandro Acero Varela
Lenguaje: Python

Ejemplo 9.3. Averiguar si un número entero e pertenece a la diferencia de los conjuntos formados por los números
             que pertenecen a los intervalos (a, b] y [c, d).
'''

def pertenece_interseccion_interv ( ):
    print ("Averiguar si un número entero e pertenece a la diferencia de los conjuntos formados por los números")
    print ("que pertenecen a los intervalos (a, b] y [c, d).")
    e = int (input ("e = "))
    a = int (input ("a = "))
    b = int (input ("b = "))
    c = int (input ("c = "))
    d = int (input ("d = "))
    print ("Dados los intervalos (", a, ",", b, "] y [5,", c, "):")
    if (e > a and e <= b) and (e < c or e >= d):
        print (e, "pertenece a la diferencia.")
    if (e <= a or e > b) or (e >= c and e < d):
        print (e, "NO pertenece a la diferencia.")
    print ("Fin.")

pertenece_interseccion_interv ( )
