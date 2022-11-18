'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Apellidos Nombre

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

3.  Escribir las primeras n potencias de p.

    Ejemplo. n igual a 6 y p igual a 5

    Las primeras 6 potencias de 5 son: 1 5 25 125 625 3125

Datos de entrada: b, a
Datos de salida: primeras n potencias
'''

def n_potencias():
    print("Yo imprimo las primeras n potencias de a^n.", end = " ")
    n = int (input("n = "))
    p = int (input("p = "))
    num = 0
    print("Las primeras", n, "potencias de", p, "son: ")

    while num != n:
        print(p ** num, end = " ")
        num = num + 1

    print("\nFin.")

n_potencias()
 
