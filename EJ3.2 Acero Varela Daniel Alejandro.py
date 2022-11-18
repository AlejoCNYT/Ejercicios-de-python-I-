'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Apellidos Nombre

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

1.  Escribir las primeras n potencias de 2.

    Ejemplo. n igual a 6

    Las primeras 6 potencias de 2 son: 1 2 4 8 16 32

Datos de entrada: b, a
Datos de salida: primeras n potencias
'''

def main():
    print("Yo imprimo las primeras n potencias de a^n.")
    n = int (input("n = "))
    num = 0
    print("Las primeras 6 potencias de 2 son: ")

    while num != n:
        print(2 ** num)
        num = num + 1
    print("Fin.")
    
main()
 

