'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo
Estudiante: Acero Varela Daniel alejandro
Lenguaje: Python

Ejemplo 5. Escribir la tabla de multiplicar del entero que diga el usuario.
           Debe construir una función que escriba la tabla de multiplicar que le indique
           el parámetro que recibe.

'''
def tabla_multiplicar(n):
    print("Tabla del: ", n)
    for mult in range(10):
        print(n, "x", mult, "=", n*mult)

def main ( ):
    print ("\nEscribo la tabla de multiplicar del entero positivo que me indique.\n")
    n = int(input())
    tabla_multiplicar(n)
    print ("\nFin.\n\n")
    
main ( )
